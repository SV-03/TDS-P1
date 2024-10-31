import pandas as pd

# Load the users.csv file
users_df = pd.read_csv('repositories.csv')  # Update with the actual file path

# Drop rows with missing license_name and count the occurrences of each license
license_counts = users_df['license_name'].dropna().value_counts()

# Select the top 3 most common licenses and join them in a comma-separated string
top_licenses = ','.join(license_counts.head(3).index)
print("3 most popular licenses:", top_licenses)
