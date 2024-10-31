

import pandas as pd

# Load the users.csv file
users_df = pd.read_csv('users.csv')

# Ensure created_at column is in datetime format
users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# Filter for users located in Austin and sort by created_at in ascending order
austin_users = users_df[users_df['location'].str.contains('Austin', case=False, na=False)]
earliest_users = austin_users.sort_values(by='created_at').head(5)

# Output the logins of the 5 earliest users as a comma-separated string
earliest_logins = ','.join(earliest_users['login'])
print("5 earliest registered GitHub users in Austin:", earliest_logins)


