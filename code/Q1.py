import pandas as pd

# Load the user data from the CSV file
users_df = pd.read_csv('users.csv')

# Filter for users located in Austin and sort by followers in descending order
austin_users = users_df[users_df['location'].str.contains('Austin', case=False, na=False)]
top_users = austin_users.sort_values(by='followers', ascending=False).head(5)

# Output the top 5 users' logins as a comma-separated string
top_logins = ','.join(top_users['login'])
print("Top 5 users in Austin by followers:", top_logins)
