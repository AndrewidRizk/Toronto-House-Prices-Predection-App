# model_training.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the cleaned and encoded dataset
df_encoded = pd.read_csv('cleaned_toronto_housing_prices_encoded.csv')

# Define the features (X) and target (y)
X = df_encoded.drop(columns=['average_price'])  # Features (all except average price)
y = df_encoded['average_price']  # Target variable

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model building: Choose between Linear Regression or Random Forest
# 1. Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# 2. Random Forest model (alternative)
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predict and evaluate the Linear Regression model
y_pred_linear = linear_model.predict(X_test)
print("\nLinear Regression Model Performance:")
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred_linear)}")
print(f"R-squared Score: {r2_score(y_test, y_pred_linear)}")

# Predict and evaluate the Random Forest model
y_pred_rf = rf_model.predict(X_test)
print("\nRandom Forest Model Performance:")
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred_rf)}")
print(f"R-squared Score: {r2_score(y_test, y_pred_rf)}")

# Save the Random Forest model (or Linear Regression) as a joblib file for future use in the Flask API
joblib.dump(rf_model, 'housing_price_predictor_rf_model.pkl')

feature_columns = X_train.columns.tolist()
joblib.dump(feature_columns, 'model_feature_columns.pkl')
print("Model saved as 'housing_price_predictor_rf_model.pkl'.")
