## Toronto Housing Prices Prediction App
This repository contains the Toronto Housing Prices Prediction App, a Flask-based web application that allows users to explore historical housing prices in various neighborhoods of Toronto and predict future prices based on different building types. It uses machine learning models trained on historical data to provide insights into housing trends and forecasts.

## 🔍 What is the App?
The Toronto Housing Prices Prediction App is designed to help users gain insight into Toronto's real estate market by displaying historical prices and predicting future prices for various neighborhoods and building types. The app allows users to:

View historical housing prices from 2022 and 2023.
- Predict housing prices for 2024 and 2025.
- Explore price trends across different Toronto communities for various building types such as detached houses, apartments, townhouses, and more.
- Interact with an intuitive map that allows users to select neighborhoods and see detailed data about housing prices.
## 📊 Learning and Dataset
The historical data used to train the model comes from a publicly available Toronto real estate dataset containing details about:

- Neighborhoods (e.g., Agincourt North, Bayview Village, etc.)
- Building Types (e.g., Detached, Semi-Detached, Apartments)
- Historical Prices for 2022 and 2023
The dataset was carefully cleaned and processed to remove outliers and fill in missing values. It was then used to train a regression model to predict housing prices based on location and building type. The cleaned dataset can be found here.

## 📈 Model Used
To predict the housing prices, we used a Random Forest Regressor model, a robust ensemble learning technique that combines multiple decision trees. This model was chosen due to its ability to handle complex datasets and its flexibility in capturing nonlinear relationships between features.

Key Features of the Model:
- Features Used:
  - Year (2024, 2025 for predictions)
  - Community (neighborhoods one-hot encoded)
  - Building type (detached, apartment, etc.)
- Model Training: The Random Forest model was trained using sklearn's RandomForestRegressor, which provides high accuracy for regression tasks while mitigating overfitting by combining multiple trees.
## 🚀 How to Use the App?
1. Explore the Map: Use the interactive map to select a Toronto neighborhood. The map displays markers for different communities across the city.
2. Select a Neighborhood: Click on any marker to see detailed historical data and price predictions for various building types.
3. View Predictions: After selecting a neighborhood, the app will display historical prices (2022, 2023) and predicted prices for 2024 and 2025.
4. Analyze the Data: You can scroll through different building types and see trends in the housing market.
## 🛠 Installing the App
To run the app locally, follow these steps:
1. Clone the Repository
```bash
git clone https://github.com/androrizk/toronto-housing-prices-app.git
cd toronto-housing-prices-app/api
```
2. Install the Required Dependencies
First, create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
```
Next, install the dependencies listed in the requirements.txt file:
```bash
pip install -r requirements.txt
```

3. Prepare the Model and Dataset
Ensure that the trained machine learning model (`housing_price_predictor_rf_model.pkl`) and the dataset (`price_forecast.csv`) are available in the `./data` folder. You can retrain the model if necessary using the script provided.

4. Run the Application
Start the Flask development server:
```bash
python app.py
```
5. Access the App
Visit the app in your browser at http://127.0.0.1:5001 (or whatever port you specify) and start exploring Toronto's housing market trends.

## 📂 Project Structure
```
📂 Toronto-Housing-Prices-Prediction-App/
├── 📂 api/                  # Flask API source code
│   ├── app.py               # Main Flask app
│   ├── requirements.txt     # Python dependencies
├── 📂 data/                 # Model and dataset storage
│   ├── housing_price_predictor_rf_model.pkl
│   ├── price_forecast.csv
└── README.md                # Project description```
```
## 🔧 Technologies Used
- Backend: Flask, Python
- Machine Learning: Scikit-learn, Pandas, Joblib
- Frontend: React (or insert the relevant frontend tech stack), Google Maps API
- Visualization: Matplotlib, Plotly
- Hosting: Heroku, Vercel (or whichever platform you're using)

## 📝 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the app as needed.

## 💡 Author
Created with ❤️ by [Andro Rizk](https://www.androrizk.com). Connect with me on [LinkedIn](https://www.linkedin.com/in/andrewrizk3030/) or explore more of my work on [GitHub](https://github.com/AndrewidRizk)!
