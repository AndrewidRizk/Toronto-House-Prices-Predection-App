import pandas as pd

# Load the dataset
df = pd.read_csv('../data/price_forecast.csv')

# Assuming the dataset has 'community' and 'average_price' columns
# Extracting the unique communities
communities = df['community'].unique()

# Print or return the unique communities
print(communities)
