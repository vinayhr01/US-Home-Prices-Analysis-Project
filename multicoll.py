#Tries to solve multicollinearity problem where 2 variables are highly correlated by finding out variance inflation

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load your dataset
data = pd.read_csv('norm.csv')

data['DATE'] = pd.to_datetime(data['DATE'])
data.set_index('DATE', inplace=True)

features = data.columns.tolist()

# Define your dependent variable (Y) and independent variables (X)
#features = [feature for feature in features if feature != 'CSUSHPISA']
Y = data['CSUSHPISA']
X = data[features]

# Add a constant term to the independent variables matrix (required for statsmodels)
X = sm.add_constant(X)

# Calculate VIF for each independent variable
vif = pd.DataFrame()
vif["Variable"] = X.columns
vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# Display the VIF values
print(vif)
