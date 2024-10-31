import pandas as pd
import statsmodels.api as sm

# Load the CSV file
csv_file = 'users.csv'  # Ensure this path is correct

# Load the CSV into a DataFrame
df = pd.read_csv("users.csv")

# Check the first few rows and the data types of the DataFrame
print("DataFrame Overview:")
print(df.head())
print("\nDataFrame Info:")
print(df.info())

# Filter out users without bios
df = df[df['bio'].notnull()]

# Calculate the length of each bio in words
df['bio_word_count'] = df['bio'].str.split().str.len()

# Prepare the independent variable (X) and dependent variable (y)
X = df['bio_word_count']
y = df['followers']  # Adjust the column name as per your dataset

# Add a constant to the independent variable (for the intercept)
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Get the slope (coefficient of the bio_word_count)
slope = model.params['bio_word_count']

# Print the regression slope rounded to three decimal places
print(f"\nRegression slope of followers on bio word count: {slope:.3f}")