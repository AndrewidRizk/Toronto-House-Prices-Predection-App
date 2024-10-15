import joblib
import pandas as pd

# Load the trained model
model = joblib.load('housing_price_predictor_rf_model.pkl')

# Load the saved feature columns used during training
feature_columns = joblib.load('model_feature_columns.pkl')

# Example input data (replace these with actual input values)
input_data = {
    'year': 2023, 
    'quarter': 3,
    'community_Agincourt North': 1,  # Example: testing Agincourt North
    'building_type_Detached': 1
}

# Convert the input data into a DataFrame
input_df = pd.DataFrame([input_data])

# Find missing columns that were part of training but are not in the input data
missing_cols = set(feature_columns) - set(input_df.columns)

# Convert the missing columns set to a list
missing_cols = list(missing_cols)

# Create a DataFrame with the missing columns set to 0
missing_df = pd.DataFrame(0, index=input_df.index, columns=missing_cols)

# Concatenate the input data with the missing columns
input_df = pd.concat([input_df, missing_df], axis=1)

# Ensure the columns are in the same order as during training
input_df = input_df[feature_columns]

# Use the model to make a prediction
predicted_price = model.predict(input_df)

# Print the predicted price
print(f"Predicted Price: ${predicted_price[0]:,.2f}")
