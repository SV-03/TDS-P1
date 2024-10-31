import pandas as pd
import statsmodels.api as sm

def main():
    # Load the user data from the CSV file
    users_df = pd.read_csv('users.csv')

    # Check if necessary columns exist
    if 'followers' not in users_df.columns or 'public_repos' not in users_df.columns:
        print("The required columns are missing from the users data.")
        return

    # Prepare the data for regression
    X = users_df['public_repos']  # Independent variable
    y = users_df['followers']      # Dependent variable

    # Add a constant to the independent variable (for intercept)
    X = sm.add_constant(X)

    # Perform OLS regression
    model = sm.OLS(y, X).fit()

    # Print the regression results
    print(model.summary())

    # Get the coefficient for public_repos
    additional_followers_per_repo = model.params['public_repos']
    print(f"Estimated additional followers per additional public repository: {additional_followers_per_repo:.3f}")

if __name__ == "__main__":
    main()
