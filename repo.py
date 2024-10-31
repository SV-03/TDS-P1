import requests
import pandas as pd
import time

# GitHub API token for authentication
TOKEN = "my token"
HEADERS = {"Authorization": f"token {TOKEN}"}

# Load unique users from users.csv
users_df = pd.read_csv("users.csv")
unique_logins = users_df['login'].unique()  # Ensure only unique logins
repository_data = []

# Loop through each unique user login
for login in unique_logins:
    page = 1
    repo_count = 0

    while repo_count < 500:
        # Fetch repositories for the user, sorted by most recently pushed
        repo_url = f"https://api.github.com/users/{login}/repos"
        params = {
            "sort": "pushed",
            "per_page": 100,
            "page": page
        }
        response = requests.get(repo_url, headers=HEADERS, params=params)

        # Check for errors in response
        if response.status_code != 200:
            print("Error:", response.status_code, response.text)
            break

        repos = response.json()
        if not repos:
            break  # Stop if no more repositories

        # Process each repository
        for repo in repos:
            if repo_count >= 500:
                break  # Stop after collecting 500 repositories

            repository_data.append({
                "login": login,
                "full_name": repo.get("full_name", ""),
                "created_at": repo.get("created_at", ""),
                "stargazers_count": repo.get("stargazers_count", 0),
                "watchers_count": repo.get("watchers_count", 0),
                "language": repo.get("language", ""),
                "has_projects": "true" if repo.get("has_projects") else "false",
                "has_wiki": "true" if repo.get("has_wiki") else "false",
                "license_name": repo["license"]["key"] if repo.get("license") else ""
            })
            repo_count += 1

        page += 1
        time.sleep(1)  # Optional: sleep to avoid rate limiting

# Convert list of dictionaries to DataFrame
df_repos = pd.DataFrame(repository_data)

# Save DataFrame to repositories.csv
df_repos.to_csv("repositories.csv", index=False)
print("Data saved to repositories.csv")
