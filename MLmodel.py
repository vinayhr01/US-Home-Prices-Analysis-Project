import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.max_open_warning'] = 50

'''
# Handles 7 missing values in dataset and that has been filled using mean imputation for final_merged_data.csv file

from sklearn.impute import SimpleImputer
import pandas as pd
merged_data = pd.read_csv('INTDSRUSM193N.csv')

imputer = SimpleImputer(strategy='mean')
merged_data['INTDSRUSM193N'] = imputer.fit_transform(merged_data[['INTDSRUSM193N']])

merged_data = merged_data.reset_index(drop=True)
merged_data.to_csv('INTDSRUSM193N.csv', index=False)
'''

df = pd.read_csv('final_merged_data.csv')

target = 'CSUSHPISA'

df['DATE'] = pd.to_datetime(df['DATE'])
df.set_index('DATE', inplace=True)

features = df.columns.tolist()

for column in features:
    df[column] = pd.to_numeric(df[column], errors='coerce') # preprocessing data to numeric form

z_scores = stats.zscore(df) # z_scores determine how far a data point is from the mean of that data in terms of standard deviation, given by Z = (X - mean) / std. deviation, positive Z-score means data point is above the mean.

df_no_outliers = df[(z_scores < 3).all(axis=1)] # handling outliers, if any gets eliminated considering a threshold of 3 standard deviations from the mean for every data point

# Feature scaling using StandardScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df_no_outliers)

# Convert scaled_data back to a DataFrame with column names
scaled_df = pd.DataFrame(scaled_data, columns=df_no_outliers.columns, index=df_no_outliers.index)

scaled_df.to_csv('normalized_data.csv')

df1 = pd.read_csv('final_Factors.csv')
df1 = df1[df1['Factors'] != 'CSUSHPISA']
df1.reset_index(inplace=True)

scaled_df['QUARTER'] =scaled_df.index.to_period('Q')
scaled_df['QUARTER'] =scaled_df['QUARTER'].astype(str)

for i in range(len(df1)):
    scaled_df[[df1['Factors'][i], 'CSUSHPISA']]
    grouped_data = scaled_df.groupby('QUARTER').agg({df1['Factors'][i]: 'sum', 'CSUSHPISA': 'mean'}).reset_index()
    grouped_data = grouped_data.sort_values('QUARTER')
    plt.figure(figsize=(20, 12))

    plt.bar(grouped_data['QUARTER'], grouped_data[df1['Factors'][i]], label=df1['Description'][i], width=0.4, alpha=0.5, color='blue')
    plt.plot(grouped_data['QUARTER'], grouped_data['CSUSHPISA'], marker='o', linestyle='-', color='black', label='CSUSHPISA')

    plt.title(f'{df1["Description"][i]} ({df1["Factors"][i]}) \n vs \n S&P/Case-Shiller U.S. National Home Price Index CSUSHPISA (Normalized)')
    plt.xlabel('Quarter')
    plt.ylabel('Normalized Values')
    plt.legend()

    plt.grid(True)  # Add gridlines
    plt.xticks(rotation=45, ha='right')  # Rotate and align x-axis tick labels for better readability
    plt.tight_layout()
    os.makedirs('./images', exist_ok=True)
    plt.savefig(f'./images/{df1["Factors"][i]}.png', bbox_inches='tight')
    plt.close()
#plt.show()

features = [feature for feature in features if feature != 'CSUSHPISA']

X_train, X_test, y_train, y_test = train_test_split(scaled_df[features], scaled_df[target], test_size=0.2, random_state=42)


models = {
    'Linear Regression': LinearRegression(fit_intercept=False, n_jobs=1),#fit_intercept=False chosen based on file hyppara_tun.py determining hyper parameter tuning for LR
    'Decision Tree': DecisionTreeRegressor(max_depth=None, max_features=20, min_samples_split=2, min_samples_leaf=1, max_leaf_nodes=20),
    'Random Forest': RandomForestRegressor(max_depth=None, max_features=20, max_leaf_nodes=10, min_samples_split=5, n_estimators=50),
    'Support Vector Regression': SVR(C=1, gamma='scale', kernel='linear'),
    'Neural Network': MLPRegressor(activation='relu', alpha=0.001, hidden_layer_sizes=(100,50))
}

# Taking best values of parameters to reduce mean error using hyper parameter tuning

results = {}
for model_name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
    mse_scores = -scores
    avg_mse = mse_scores.mean()
    results[model_name] = avg_mse


best_model = min(results, key=results.get)
best_model_instance = models[best_model]

best_model_instance.fit(X_train, y_train)

predictions = best_model_instance.predict(X_test)
mse = mean_squared_error(y_test, predictions)

print("Model Selection Results:")
for model, mse_score in results.items():
    print(f"{model}: MSE={mse_score}")  

print(f"\nBest Model: {best_model}")
print(f"Best Model MSE on Testing Set: {mse}")

r2 = r2_score(y_test, predictions)

print(f"R-squared score of best model which is {best_model}: {r2}")

best_model_instance.fit(X_train, y_train)

coefficients = best_model_instance.coef_

print("Coefficients:")
for feature, coefficient in zip(features, coefficients):
    print(f"{feature}: {coefficient}")

# Assuming 'y' is your target variable
mean_y = np.mean(scaled_df['CSUSHPISA'])
median_y = np.median(scaled_df['CSUSHPISA'])

# Create baseline predictions
baseline_mean_predictions = np.full_like(y_test, mean_y)
baseline_median_predictions = np.full_like(y_test, median_y)

mse_mean_baseline = mean_squared_error(y_test, baseline_mean_predictions)

# Calculate Mean Squared Error for the median baseline
mse_median_baseline = mean_squared_error(y_test, baseline_median_predictions)

print(f"Mean Baseline MSE: {mse_mean_baseline}")
print(f"Median Baseline MSE: {mse_median_baseline}")

print(f"Best Model MSE on Testing Set: {mse}")
print(f"Comparison between baseline and testing set significance difference indicates no overfitting or underfitting of data")