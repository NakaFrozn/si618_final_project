# reshape data
# reshape data to have one row per neighborhood
# take evictions, hvi, and median sale price and reshape by year
# everything else can be aggregated by mean
# convert year to no decimal string before reshape
data['year'] = data['year'].astype(int).astype(str)
# define function to pull variables and reshape to wide format
# also interpolates missing values
def reshape_data(data, value_col, index_col, columns_col):
    # Create the pivot table
    data_pivot = data.pivot_table(index=[index_col], columns=columns_col, values=value_col)
    # Interpolate missing values
    data_pivot = data_pivot.interpolate(method='linear', axis=1)    
    data_pivot.reset_index(inplace=True)    
    # Rename columns to include the value_col prefix for clarity
    data_pivot.columns = [index_col] + [f'{value_col}_{col}' for col in data_pivot.columns[1:]]    
    return data_pivot


evict_pivot = reshape_data(data, 'num_evictions', 'nta_name', 'year')
hvi_pivot = reshape_data(data, 'hvi', 'nta_name', 'year')
sale_price_pivot = reshape_data(data, 'median_sale_price', 'nta_name', 'year')

# print head for each
# print(evict_pivot.head())
# print(hvi_pivot.head())
# print(sale_price_pivot.head())

# Collapse to one row for each neighborhood
data.drop(columns=['GEOID'], inplace=True)
data = data.groupby(['nta_name', 'borough']).agg({
    'pct_attendance': 'mean',
    'pct_chronically_absent': 'mean',
    'total_population': 'mean',
    'median_income': 'mean',
    'white_pct': 'mean',
    'black_pct': 'mean',
    'american_indian_alaska_native_pct': 'mean',
    'asian_pct': 'mean',
    'hawaiian_pacific_islander_pct': 'mean',
    'multiple_race_pct': 'mean',
    'other_race_pct': 'mean'
}).reset_index()

# Merge in reshaped data
data = data.merge(evict_pivot, on='nta_name', how='left')
data = data.merge(hvi_pivot, on='nta_name', how='left')
data = data.merge(sale_price_pivot, on='nta_name', how='left')

print(data.head())