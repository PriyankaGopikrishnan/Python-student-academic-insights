import pandas as pd

# 📥 Step 1: Load the cleaned score and student datasets
score_file = pd.read_csv('student_scores_clean.csv')     # Contains Student_ID, Subject_ID, Score
student_file = pd.read_csv('students_clean.csv')         # Contains Student_ID, Gender, etc.

# 🔗 Step 2: Merge both datasets on 'Student_ID' to combine student details with scores
merge_table = pd.merge(student_file, score_file, on='Student_ID')
print(merge_table)
import pandas as pd

# 📥 Step 1: Load the cleaned datasets for scores and students
score_file = pd.read_csv('student_scores_clean.csv')     # Columns: Student_ID, Subject_ID, Score
student_file = pd.read_csv('students_clean.csv')         # Columns: Student_ID, Gender, Age, etc.

# 🔗 Step 2: Merge both datasets on 'Student_ID' to combine student details with their scores
merge_table = pd.merge(student_file, score_file, on='Student_ID')
print(merge_table)

# 📉 Step 3: Display the minimum and maximum scores from the score data
print("Minimum Score:", score_file['Score'].min())
print("Maximum Score:", score_file['Score'].max())

# 📊 Step 4: Calculate and display the average score grouped by gender
student_score = merge_table.groupby('Gender')['Score'].mean().reset_index()
print('Student average score by gender:\n')
print(student_score)

# 📊 Step 5: Calculate and display the average score grouped by subject
subject_wise_score_avg = merge_table.groupby('Subject_ID')['Score'].mean().reset_index()
print('\nAverage score by subject:\n')
print(subject_wise_score_avg)

# 🚨 Step 6: Filter and count students who scored less than 50
low_scores = merge_table[merge_table['Score'] < 50]
print('Number of students who got less than 50:', low_scores['Student_ID'].nunique())

# 📊 Step 7: Count of low-score students grouped by subject
low_score_by_subject = low_scores.groupby('Subject_ID')['Student_ID'].nunique()

# 🗃️ Step 8: Convert to DataFrame and rename column for clarity
low_score_by_subject_df = low_score_by_subject.reset_index()
low_score_by_subject_df = low_score_by_subject_df.rename(columns={'Student_ID': 'Low_Score_Student_Count'})

# 🖨️ Step 9: Display the number of students who scored less than 50, by subject
print('\n📊 Number of students who got less than 50 by subject:\n')
print(low_score_by_subject_df)

# 🏅 Step 10: Filter and count students who scored more than 90
high_scores = merge_table[merge_table['Score'] > 90]
print('Number of students who got more than 90:', high_scores['Student_ID'].nunique())

# 📊 Step 11: Count of high-score students grouped by subject
high_score_by_subject = high_scores.groupby('Subject_ID')['Student_ID'].nunique()

# 🗃️ Step 12: Convert to DataFrame and rename column
high_score_by_subject_df = high_score_by_subject.reset_index()
high_score_by_subject_df = high_score_by_subject_df.rename(columns={'Student_ID': 'High_Score_Student_Count'})

# 🖨️ Step 13: Display the number of students who scored more than 90, by subject
print('\n📊 Number of students who got more than 90 by subject:\n')
print(high_score_by_subject_df)

# ⚖️ Step 14: Filter and count students who scored between 50 and 90 (exclusive)
avg_score = merge_table[(merge_table['Score'] < 90) & (merge_table['Score'] > 50)]
print('Number of students who got less than 90 & greater than 50:', avg_score['Student_ID'].nunique())

# 📊 Step 15: Count of mid-score students grouped by subject
avg_score_by_subject = avg_score.groupby('Subject_ID')['Student_ID'].nunique()

# 🗃️ Step 16: Convert to DataFrame and rename column
avg_score_by_subject_df = avg_score_by_subject.reset_index()
avg_score_by_subject_df = avg_score_by_subject_df.rename(columns={'Student_ID': 'Mid_Score_Student_Count'})

# 🖨️ Step 17: Display the number of students who scored between 50 and 90, by subject
print('\n📊 Number of students who got less than 90 & greater than 50 by subject:\n')
print(avg_score_by_subject_df)

# 📊 Step 18: Calculate and display average score grouped by student age
age_wise_score = merge_table.groupby('Age')['Score'].mean().reset_index()
print('Student average score by Age:\n')
print(age_wise_score)

# 📊 Step 19: Calculate and display average score grouped by student's Parent_Education
avg_score_by_parent_education = merge_table.groupby('Parent_Education')['Score'].mean().reset_index()
print(avg_score_by_parent_education)
