import requests
import pandas as pd

# GitHub API token for authentication
TOKEN = "my token"
HEADERS = {"Authorization": f"token {TOKEN}"}

# API base URL for users in Austin with over 100 followers
BASE_URL = "https://api.github.com/search/users"
USER_DETAILS_URL = "https://api.github.com/users/"

# Initialize an empty list to store user data
user_data = []

# Pagination loop
page = 1
while True:
    # Search query
    params = {
        "q": "location:Austin followers:>100",
        "per_page": 30,
        "page": page
    }
    response = requests.get(BASE_URL, headers=HEADERS, params=params)

    # Check for errors in response
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        break

    users = response.json().get('items', [])
    print(f"Page {page}, Users found: {len(users)}")  # Debugging: check user count

    # Stop if there are no more users
    if not users:
        break

    # Fetch detailed information for each user
    for user in users:
        user_response = requests.get(USER_DETAILS_URL + user['login'], headers=HEADERS)

        # Check for errors in user detail response
        if user_response.status_code != 200:
            print("Error fetching user:", user['login'], user_response.text)
            continue

        user_info = user_response.json()

        # Format data as per specifications
        user_data.append({
            "login": user_info.get("login", ""),
            "name": user_info.get("name", ""),
            "company": (user_info.get("company", "").replace('@', '').strip().upper()
                        if user_info.get("company") else ""),
            "location": user_info.get("location", ""),
            "email": user_info.get("email", ""),
            "hireable": "true" if user_info.get("hireable") else "false" if user_info.get("hireable") is not None else "",
            "bio": user_info.get("bio", ""),
            "public_repos": user_info.get("public_repos", 0),
            "followers": user_info.get("followers", 0),
            "following": user_info.get("following", 0),
            "created_at": user_info.get("created_at", "")
        })

    # Move to the next page
    page += 1

# Check if user_data is populated
print("Total users collected:", len(user_data))

# Convert list of dictionaries to DataFrame and check for data presence before saving
if user_data:
    df = pd.DataFrame(user_data)
    df.to_csv("users.csv", index=False)
    print("Data saved to users.csv")
else:
    print("No data to save.")
