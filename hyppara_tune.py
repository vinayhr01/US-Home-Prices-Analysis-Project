import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_csv('normalized_data.csv')
df.set_index("DATE", inplace=True)

features = df.columns.tolist()

features = [feature for feature in features if feature != 'CSUSHPISA']

X = df[features]

y = df['CSUSHPISA']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define hyperparameter grids for each algorithm
param_grid_lr = {
    'fit_intercept': [True, False],
    'n_jobs': [1, 2, 3, 10]
}

param_grid_dt = {
    'max_depth': [None, 1, 2, 3, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 5, 10, 20],
    'max_leaf_nodes': [2, 3, 10, 20, 30],
    'max_features': [1, 2, 3, 5, 10, 20, 30]
}

param_grid_rf = {
    'n_estimators': [50, 100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10, 20, 30],
    'max_features': [2, 5, 10, 20, 30],
    'max_leaf_nodes': [2, 5, 10]
}

param_grid_svr = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf', 'poly'],
    'gamma': ['scale', 'auto']
}

param_grid_mlp = {
    'hidden_layer_sizes': [(50,), (100,), (50, 50), (100, 50)],
    'activation': ['relu', 'tanh', 'logistic'],
    'alpha': [0.001, 0.01]
}

# Create models
models = {
    'Linear Regression': (LinearRegression(), param_grid_lr),
    'Decision Tree Regression': (DecisionTreeRegressor(), param_grid_dt),
    'Random Forest Regression': (RandomForestRegressor(), param_grid_rf),
    'SVR': (SVR(), param_grid_svr),
    'MLP Regression': (MLPRegressor(), param_grid_mlp)
}

# Hyperparameter tuning and evaluation
for model_name, (model, param_grid) in models.items():
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    print(f"{model_name}:")
    print(f"Best Parameters: {grid_search.best_params_}")
    print(f"Mean Squared Error: {mse}")

