from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model and feature columns
model = joblib.load('../data/housing_price_predictor_rf_model.pkl')
feature_columns = joblib.load('../data/model_feature_columns.pkl')
df = pd.read_csv('../data/price_forecast.csv')  # Replace with your actual file path

def encode_input(data):
    # Build a DataFrame for the input
    df = pd.DataFrame([data])

    # Find missing columns that were part of training but are not in the input data
    missing_cols = set(feature_columns) - set(df.columns)
    
    # Convert the set of missing columns into a list
    missing_cols = list(missing_cols)

    # Create a DataFrame with the missing columns set to 0
    missing_df = pd.DataFrame(0, index=df.index, columns=missing_cols)

    # Concatenate the input data with the missing columns
    df = pd.concat([df, missing_df], axis=1)

    # Ensure the columns are in the same order as during training
    df = df[feature_columns]
    
    return df


@app.route('/community-data', methods=['POST'])
def community_data():
    # Extract input data from the POST request
    data = request.json
    community = data.get('community')

    if not community:
        return jsonify({'error': 'Community is required'}), 400

    # Fetch historical data for the given community
    filtered_data = df[df['community'] == community]

    if filtered_data.empty:
        return jsonify({'error': f'No data found for community: {community}'}), 404

    # Ensure the _date column contains the year (adjust this if needed)
    filtered_data['_year'] = pd.to_datetime(filtered_data['_date']).dt.year

    # Initialize the dictionary to hold building types data
    building_types_data = {}

    # For each building type, collect historical data and make predictions
    building_types = filtered_data['building_type'].unique()

    for building_type in building_types:
        building_data = filtered_data[filtered_data['building_type'] == building_type]
        historical_data = {}

        # Get prices for 2022 and 2023, ensure keys are strings
        for year in [2022, 2023]:
            year_data = building_data[building_data['_year'] == year]
            if not year_data.empty:
                price = year_data['average_price'].values[0]
                historical_data[str(year)] = f"CAD${round(price, 2)}"
            else:
                historical_data[str(year)] = "No data available"

        # Predict combined prices for 2024/2025
        input_data = {
            'year': 2024,
            'quarter': 1,
            f"community_{community}": 1,  # One-hot encode community
            f"building_type_{building_type}": 1  # One-hot encode building type
        }

        encoded_input_2024 = encode_input(input_data)
        predicted_price_2024 = model.predict(encoded_input_2024)[0]

        input_data['year'] = 2025  # Predict for 2025
        encoded_input_2025 = encode_input(input_data)
        predicted_price_2025 = model.predict(encoded_input_2025)[0]

        # Calculate average of predicted 2024 and 2025 prices
        combined_predicted_price = (predicted_price_2024 + predicted_price_2025) / 2
        historical_data['Predicted 2024/2025'] = f"CAD${round(combined_predicted_price, 2)}"

        # Add the building type data to the main dictionary
        building_types_data[building_type] = historical_data

    return jsonify(building_types_data)




if __name__ == '__main__':
    app.run(debug=True)
