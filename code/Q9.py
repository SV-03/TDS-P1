import pandas as pd

def main():
    # Load the user data from the CSV file
    users_df = pd.read_csv('users.csv')

    # Check if necessary columns exist
    if 'location' not in users_df.columns or 'followers' not in users_df.columns or 'public_repos' not in users_df.columns:
        print("The required columns are missing from the users data.")
        return

    # Filter users based in Austin
    austin_users = users_df[users_df['location'].str.contains("Austin", na=False)]

    # Extract followers and public_repos columns
    followers = austin_users['followers']
    public_repos = austin_users['public_repos']

    # Calculate the correlation
    correlation = followers.corr(public_repos)

    # Print the correlation result up to 3 decimal places
    print(f"The correlation between the number of followers and the number of public repositories among users in Austin is {correlation:.3f}.")

if __name__ == "__main__":
    main()
