import pandas as pd

# Step 1: Load the unclean student_scores data
scores_file = pd.read_csv('student_scores_unclean.csv')

# Step 2: Display the dataset shape and missing value summary
print("🔍 Dataset preview:")
print(scores_file.head())

print("\n📌 Missing values before cleaning:\n", scores_file.isnull().sum())

# Step 3: Show only rows where 'Score' is null
print("\n🧹 Rows with missing 'Score':")
print(scores_file[scores_file['Score'].isnull()])

# Step 4: Print number of rows before cleaning
print("\n📊 Number of rows before cleaning:", scores_file.shape[0])

# Step 5: Replace missing 'Score' values with the median
median_score_all = scores_file['Score'].median()
scores_file['Score'] = scores_file['Score'].fillna(median_score_all)

# Step 6: Convert Score to integer (if needed)
scores_file['Score'] = scores_file['Score'].astype(int)

# Step 7: Confirm nulls are handled
print("\n✅ Missing values after cleaning:\n", scores_file.isnull().sum())

# Step 8: Save a copy before any outlier edits
original_df = scores_file.copy()

# Step 9: Detect outliers (Score > 100)
outlier = scores_file[scores_file['Score'] > 100]

# Step 10: Display BEFORE values for each affected Student + Subject
print("\n🔍 Showing records BEFORE outlier treatment:\n")
for idx, row in outlier.iterrows():
    sid = row['Student_ID']
    subid = row['Subject_ID']
    before = original_df[(original_df['Student_ID'] == sid) & (original_df['Subject_ID'] == subid)]
    print("📌 Student ID:", sid, "| Subject ID:", subid)
    print(before)
    print("-" * 40)

# Step 11: Replace outlier Scores (>100) with median of valid scores (<=100)
valid_median = scores_file['Score'][scores_file['Score'] <= 100].median()
scores_file.loc[scores_file['Score'] > 100, 'Score'] = valid_median

# Step 12: Display AFTER values for each affected Student + Subject
print("\n✅ Showing records AFTER outlier treatment:\n")
for idx, row in outlier.iterrows():
    sid = row['Student_ID']
    subid = row['Subject_ID']
    after = scores_file[(scores_file['Student_ID'] == sid) & (scores_file['Subject_ID'] == subid)]
    print("✅ Student ID:", sid, "| Subject ID:", subid)
    print(after)
    print("=" * 40)

# Step 13: Drop rows where Score < 0
scores_file = scores_file[scores_file['Score'] >= 0]

# Confirm the change
print("✅ Negative score records removed.")


# Step 14: Save the cleaned dataset to a new CSV
scores_file.to_csv('student_scores_clean.csv', index=False)
print("\n📁 Cleaned data saved to: 'student_scores_clean.csv'")
