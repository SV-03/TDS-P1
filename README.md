# TDS-P1
Austin Users and Repositories

The Python script scrapes GitHub user and repository data for users in Austin with over 100 followers, saving the information into CSV files, includeing functions for cleaning data, fetching user details, and managing pagination while adhering to API rate limits for efficient data retrieval.

Interesting findings: Many users work at major tech companies like Google and Microsoft, with 'getify' having the highest follower count; JavaScript, Python, TypeScript, and Go are the most preferred languages, and the highest repository creation year was 2016, with around 3,800 repositories.

Recommendation: Developers should focus on creating or contributing to repositories that emphasize collaborative features, as these are popular in Austin.


Scraping details:

This code collects user data and repository information from GitHub, focusing on users located in Austin with over 100 followers and saving it into two CSV files: 'users.csv' for user data and 'repositories.csv' for repository details.
- The code systematically collects user and repository data, handling pagination and rate limiting, and saves the cleaned, structured data to CSV files for analysis.
- Error Handling: It checks response status for each request, printing errors if encountered, and manages edge cases like missing license data.
- Output: Two CSV files, users.csv and repositories.csv, ready for further analysis.

- Here’s how it was done:

1. User Data Collection (users.csv)

The first part of the script gathers user profile information:

- Imports and Setup: It uses 'requests' to access the GitHub API and 'pandas' for handling data storage. The script is authenticated using a GitHub API token.
- Pagination and Querying Users:
  - It starts by constructing a search query targeting users based in Austin with more than 100 followers.
  - The script handles pagination to go through all available pages until no more users are returned.
  - For each user, it makes an additional API call to gather details like username, name, company, location, email, hireability status, biography, and follower/following counts.
  - Data cleaning is done for fields like 'company' to standardize formatting, and hireability is stored as "true", "false", or "" (missing data).
- Data Storage: The script appends all user data to a list (user_data) and, once complete, converts this list to a DataFrame, saving it to 'users.csv'.

2. Repository Data Collection (repositories.csv)

The second part of the script gathers repository information for each user from 'users.csv':

- Loading User Data: It reads 'users.csv' and filters unique user logins.
- Pagination and Querying Repositories:
  - For each user, it queries up to 500 repositories, sorted by the most recently pushed.
  - It paginates through results, processing up to 100 repositories per page.
  - Each repository's details, including name, creation date, stars, watchers, language, project and wiki settings, and license, are recorded.
- Rate Limiting**: The script uses 'time.sleep(1)' between requests to avoid GitHub’s rate-limiting restrictions.
- Data Storage**: Finally, the repository data is converted to a DataFrame and saved to 'repositories.csv'.
