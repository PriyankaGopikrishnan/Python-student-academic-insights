import pandas as pd

# 📥 Step 1: Load the cleaned student dataset
students = pd.read_csv('students_clean.csv')

# 🔄 Step 2: Convert Age column to string
# This ensures we can use string functions like isnumeric(), and avoids errors with NaN or mixed types
students['Age'] = students['Age'].astype(str)

# 🔍 Step 3: Create a mask for values in Age that are NOT numeric
# ~ is used to invert the mask from isnumeric() so we can detect problematic (non-numeric) entries
non_numeric_mask = ~students['Age'].str.isnumeric()

# ✅ Step 4: Check if any non-numeric age values exist
if non_numeric_mask.any():
    # If there are bad values, print a warning and display those rows
    print("⚠️ Invalid Age values found!\n")
    print(students.loc[non_numeric_mask, ['StudentID', 'Age']])  # Show student IDs and their invalid Age values

    # Show only the unique problematic values to understand the type of errors (e.g., "N/A", "seventeen", "")
    print("\n🧹 Unique invalid Age entries:")
    print(students.loc[non_numeric_mask, 'Age'].unique())
else:
    # If everything is clean, confirm it
    print("✅ All Age values are valid (numeric).")
