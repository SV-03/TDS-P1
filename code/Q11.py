import pandas as pd

# Load the repositories.csv file
repos_df = pd.read_csv('repositories.csv')  # Replace with the path to repositories.csv

# Calculate the correlation between has_projects and has_wiki
correlation = repos_df['has_projects'].astype(int).corr(repos_df['has_wiki'].astype(int))

# Print the correlation rounded to 3 decimal places
print("Correlation between projects and wiki enabled:", round(correlation, 3))
