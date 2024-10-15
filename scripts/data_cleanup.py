import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace with the actual file path)
df = pd.read_csv('toronto_real_estate.csv')

# Display the first few rows to check the data structure
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Fill missing values in 'Number_Beds' and 'Number_Baths' with the median
df['Number_Beds'].fillna(df['Number_Beds'].median(), inplace=True)
df['Number_Baths'].fillna(df['Number_Baths'].median(), inplace=True)

# Drop rows where 'Price' is missing
df = df.dropna(subset=['Price'])

# Check for outliers in 'Price'
print("\nSummary statistics for Price:")
print(df['Price'].describe())

# Plotting a boxplot to visually inspect price outliers
plt.boxplot(df['Price'])
plt.title('Boxplot of House Prices')
plt.show()

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_toronto_real_estate.csv', index=False)
print("Cleaned data saved as 'cleaned_toronto_real_estate.csv'.")
