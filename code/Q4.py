import pandas as pd

# Load the users.csv file
users_df = pd.read_csv('users.csv')  # Replace with the path to users.csv

# Drop missing values in the company column
companies = users_df['company'].dropna()

# Find the most common company
top_company = companies.value_counts().idxmax()
print("Company with the majority of developers:", top_company)
