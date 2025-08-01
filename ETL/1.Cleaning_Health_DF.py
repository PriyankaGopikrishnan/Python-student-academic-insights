import pandas as pd

# Step 1: Read the unclean health dataset
health_file = pd.read_csv('health_unclean.csv')

# Step 2: Display the dataset (optional, for debugging or review)
print(health_file)

# Step 3: Check how many null values are present in each column
print(health_file.isnull().sum())

# Step 4: View only the rows where 'Health' column is null
print(health_file[health_file['Health'].isnull()])

# Step 5: Print the total number of rows before cleaning
print("Before cleaning:", health_file.shape[0], "rows")

# Step 6: Calculate the median value of 'Health' column
median_health = health_file['Health'].median()

# Step 7: Replace missing values in 'Health' column with the median
health_file['Health'] = health_file['Health'].fillna(median_health)

# Step 8: Print the number of rows after cleaning and check remaining nulls
print("After cleaning Nulls:", health_file.shape[0], "rows")
print(health_file.isnull().sum())

# Step 9: Convert 'Health' column to integer type (optional for consistency)
health_file['Health'] = health_file['Health'].astype(int)

# Step 10: Display the cleaned dataset (first few rows)
print(health_file.head())

# Step 11: Save the cleaned DataFrame to a new CSV file
health_file.to_csv('health_clean.csv', index=False)
