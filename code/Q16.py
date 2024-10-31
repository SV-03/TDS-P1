import pandas as pd
from collections import Counter

# Load the users.csv file
users_df = pd.read_csv('users.csv')  # Replace with the path to users.csv

# Drop rows where 'name' is missing
users_df = users_df[users_df['name'].notna()]

# Extract surnames
surnames = users_df['name'].str.strip().str.split().str[-1]

# Count occurrences of each surname
surname_counts = Counter(surnames)

# Find the most common surname(s)
most_common_count = max(surname_counts.values())
most_common_surnames = [surname for surname, count in surname_counts.items() if count == most_common_count]

# Sort surnames alphabetically
most_common_surnames.sort()

# Print the result
print(f"Most common surname(s): {', '.join(most_common_surnames)}")
print(f"Number of users with the most common surname: {most_common_count}")
