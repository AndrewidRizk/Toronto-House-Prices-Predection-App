import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset with encoding specified
df = pd.read_csv('../data/HouseListings-Top45Cities-10292023-kaggle.csv', encoding='ISO-8859-1')

# Filter the data to include only rows for Toronto
toronto_df = df[df['City'] == 'Toronto']

# Display the first few rows of Toronto data to check the data structure
print(toronto_df.head())

# Check for missing values in the Toronto data
print("\nMissing values in each column (Toronto rows only):")
print(toronto_df.isnull().sum())

# Fill missing values in 'Number_Beds' and 'Number_Baths' with the median
toronto_df['Number_Beds'].fillna(toronto_df['Number_Beds'].median(), inplace=True)
toronto_df['Number_Baths'].fillna(toronto_df['Number_Baths'].median(), inplace=True)

# Drop rows where 'Price' is missing
toronto_df = toronto_df.dropna(subset=['Price'])

# Check for outliers in 'Price'
print("\nSummary statistics for Price (Toronto rows only):")
print(toronto_df['Price'].describe())

# Optionally, remove outliers if Price > $5 million (adjust threshold as needed)
toronto_df = toronto_df[toronto_df['Price'] < 5000000]


# Plotting a boxplot to visually inspect price outliers
plt.boxplot(toronto_df['Price'])
plt.title('Boxplot of House Prices in Toronto')
plt.show()

# Save the cleaned Toronto data to a new CSV file
toronto_df.to_csv('cleaned_toronto_real_estate.csv', index=False)
print("Cleaned Toronto data saved as 'cleaned_toronto_real_estate.csv'.")
