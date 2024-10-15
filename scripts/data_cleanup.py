import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the dataset
df = pd.read_csv('../data/price_forecast.csv')

# Display first few rows to inspect the dataset
print("Initial Dataset Head:")
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Handle missing values if necessary (assuming there are no missing values in 'average_price')
df = df.dropna(subset=['average_price'])

# Convert '_date' to datetime format
df['_date'] = pd.to_datetime(df['_date'].str.replace('Q', '-'), format='%Y-%m')

# Create time-based features: year and quarter
df['year'] = df['_date'].dt.year
df['quarter'] = df['_date'].dt.quarter

# Drop the original '_date' column as it has been broken into 'year' and 'quarter'
df = df.drop(columns=['_date'])

# Encoding categorical features (community and building_type) using one-hot encoding
df_encoded = pd.get_dummies(df, columns=['community', 'building_type'], drop_first=True)

# Define the features (X) and target (y)
X = df_encoded.drop(columns=['average_price'])  # Features (all except average price)
y = df_encoded['average_price']  # Target variable

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model building: You can choose between Linear Regression or Random Forest
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
print("Model saved as 'housing_price_predictor_rf_model.pkl'.")

# Optional: Save the cleaned and encoded data for future reference
df_encoded.to_csv('cleaned_toronto_housing_prices_encoded.csv', index=False)
print("Cleaned and encoded data saved as 'cleaned_toronto_housing_prices_encoded.csv'.")
