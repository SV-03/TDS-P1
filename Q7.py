import pandas as pd

def main():
    # Load the repository data from the CSV file
    repositories_df = pd.read_csv('repositories.csv')

    # Check for valid data
    if 'language' not in repositories_df.columns or 'stargazers_count' not in repositories_df.columns:
        print("The required columns are missing from the repositories data.")
        return

    # Group by language and calculate the average stars per repository
    average_stars_per_language = repositories_df.groupby('language')['stargazers_count'].mean()

    # Identify the language with the highest average stars
    highest_average_language = average_stars_per_language.idxmax()
    highest_average_stars = average_stars_per_language.max()

    # Print the result
    print(f"The language with the highest average number of stars per repository is '{highest_average_language}' with an average of {highest_average_stars:.2f} stars.")

if __name__ == "__main__":
    main()
