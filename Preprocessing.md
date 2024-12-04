### Preprocessing

First we load the analytic dataset used in prior steps. This data is a cross-sectional dataset of Census tracts in New York City, from 2019 through 2022. The dataset includes demographic data, median income, school attendance data, and counts of evictions in those years.

The data is in long format, with years repeating for each Census tract. In order to retain information, we define a function to reshape specific variables into wide format. This function is applied to the eviction counts, Home Value Index, and Sales Price variables. For missing values, the function uses a linear interpolation method to fill in the gaps. After reshaping, the data is merged back into an aggregated dataset, resulting in a wide format dataset with one row per Neighborhood.

We also use the demographic data to create a categorical variable that indicates whether a neighborhood is minority dominated. A neighborhood is considered minority dominated if the percentage of minority residents is greater than 50%.  

### Preprocessing Pipeline

After the initial reshaping and creation of new variables, the data can be standardized and prepared for modeling. We use the `SimpleImputer` function from the `sklearn.impute` module to fill in missing values with their median. We then use the `StandardScaler` function to standardize the numeric data, and the `OneHotEncoder` to binarize the categorical variables.

### Principal Component Analysis

We use Principal Component Analysis (PCA) to reduce the dimensionality of the dataset. This is done by projecting the data onto a lower-dimensional space, while retaining as much variance as possible. We use the `PCA` function from the `sklearn.decomposition` module to perform PCA. The number of components is chosen based on the cumulative explained variance ratio. 

Showing the cumulative explained variance ratio for each number of components, we can determine the optimal number of components to use. We chose to use 5 components, capturing over 70% of the variance in the data.


