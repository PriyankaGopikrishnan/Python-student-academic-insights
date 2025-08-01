import pandas as pd

# Step 1: Load the unclean students data
students_file = pd.read_csv('students_unclean.csv')

# Step 2: Display the dataset (optional)
print(students_file)

# Step 3: Show how many nulls are present in each column
print("Missing values before cleaning:\n", students_file.isnull().sum())

# Step 4: View only the rows where 'Gender' or 'Parent_Education' is missing
print(students_file[students_file['Gender'].isnull() | students_file['Parent_Education'].isnull()])

# Step 5: Fill missing 'Gender' with the mode (most frequent value)
mode_gender = students_file['Gender'].mode()[0]
students_file['Gender'] = students_file['Gender'].fillna(mode_gender)

# Step 6: Fill missing 'Parent_Education' with the mode (or median if it's numeric)
mode_education = students_file['Parent_Education'].mode()[0]
students_file['Parent_Education'] = students_file['Parent_Education'].fillna(mode_education)

# Step 7: Confirm that null values are handled
print("Missing values after cleaning:\n", students_file.isnull().sum())

# Step 8: Preview cleaned data
print(students_file.head())

# Step 9: Save the cleaned DataFrame to a new CSV file
students_file.to_csv('students_clean.csv', index=False)
