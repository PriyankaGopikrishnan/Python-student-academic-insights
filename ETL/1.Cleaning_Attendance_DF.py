import pandas as pd


# Step 1: Load the unclean attendance data from CSV into a DataFrame
attendance_file = pd.read_csv('attendance_unclean.csv')

# Step 2: (Optional) Display all rows where 'Absences' is missing (NaN)
print(attendance_file[attendance_file['Absences'].isnull()])

# Step 3: Print total number of rows before cleaning
print("Before cleaning:", attendance_file.shape[0], "rows")

# Step 4: Show how many missing values are in each column
print("Missing values before cleaning:\n", attendance_file.isnull().sum())

# Step 5: Replace missing 'Absences' values with the median of the column
median_absences = attendance_file['Absences'].median()
attendance_file['Absences'] = attendance_file['Absences'].fillna(median_absences)

# Step 6: Convert the 'Absences' column to integer type now that NaNs are gone
attendance_file['Absences'] = attendance_file['Absences'].astype(int)

# Step 7: Print total number of rows after filling nulls
print("After cleaning:", attendance_file.shape[0], "rows")

# Step 8: Confirm there are no nulls left
print("Null counts after cleaning:\n", attendance_file.isnull().sum())

# Step 9: Save the cleaned DataFrame to a new CSV file
attendance_file.to_csv('attendance_clean.csv', index=False)

# Optional: Preview cleaned data
print(attendance_file.head())