import pandas as pd

# 📥 Step 1: Load cleaned student demographic and health datasets
student_file = pd.read_csv('students_clean.csv')       # Contains columns like Student_ID, Gender, Age, Address
health_file = pd.read_csv('health_clean.csv')          # Contains Student_ID and Health rating (ideally 1 to 5)

# 🔗 Step 2: Merge both datasets on 'Student_ID' to combine student info with health ratings
merge_file = pd.merge(student_file, health_file, on='Student_ID')

# 🧾 Step 3: Check the merged dataset's structure and filter out invalid health ratings (>5)
print("📋 Columns in merged dataset:", merge_file.columns)

# 🔍 Remove any rows with invalid health ratings (greater than 5)
merge_file = merge_file[merge_file['Health'] < 6]

# 👀 Preview the cleaned and merged data
print("\n✅ Merged data after removing invalid health scores:\n")
print(merge_file)

# 📊 Step 4: Calculate and print average health rating grouped by Gender
gender_wise_health_rating = merge_file.groupby('Gender')['Health'].mean().reset_index()
print("\n📊 Average Health Rating by Gender:")
print(gender_wise_health_rating)

# 📊 Step 5: Calculate and print average health rating grouped by Age
age_wise_health_rating = merge_file.groupby('Age')['Health'].mean().reset_index()
print("\n📊 Average Health Rating by Age:")
print(age_wise_health_rating)

# 📊 Step 6: Calculate and print average health rating grouped by Address type (Urban/Rural)
address_wise_health_rating = merge_file.groupby('Address')['Health'].mean().reset_index()
print("\n📊 Average Health Rating by Address:")
print(address_wise_health_rating)
