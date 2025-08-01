import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the cleaned student data from CSV
student_df = pd.read_csv('students_clean.csv')

# Step 2: Display the column names to confirm structure
print(student_df.columns)

print('__' * 30)
print('Count of students by gender')
print('__' * 30)
# Step 3: Count of students by Gender
gender_count = student_df['Gender'].value_counts().reset_index()
print(gender_count)

print('__' * 30)
print('Count by Parent Education Level')
print('__' * 30)
# Step 4: Count of students by Parent Education Level
parent_education_count = student_df['Parent_Education'].value_counts().reset_index()
print(parent_education_count)

print('__' * 30)
print('Count of students by Address')
print('__' * 30)
# Step 5: Count of students by Address (Urban/Rural/etc.)
address_wise_student_count = student_df['Address'].value_counts().reset_index()
print(address_wise_student_count)

print('__' * 30)
print('Count of students by Age')
print('__' * 30)
# Step 6: Count of students by Age
age_wise_student_count = student_df['Age'].value_counts().reset_index()
print(age_wise_student_count)

print('__' * 30)
