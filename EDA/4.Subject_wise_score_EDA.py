import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📥 Step 1: Load subject and score datasets
subjects_file = pd.read_csv('subjects.csv')                  # Contains Subject_ID, Subject_Name
score_file = pd.read_csv('student_scores_clean.csv')         # Contains Student_ID, Subject_ID, Score

# 🔗 Step 2: Merge both datasets on 'Subject_ID' to include subject names with scores
merge_table = pd.merge(score_file, subjects_file, on='Subject_ID')

# 📊 Step 3: Calculate average score per subject
# - Group by Subject_ID and take the mean of scores
# - Reset index to convert Series to DataFrame
# - Sort by score in ascending order
subject_wise_score_avg = merge_table.groupby('Subject_ID')['Score'].mean()
subject_wise_score_avg = subject_wise_score_avg.reset_index()
subject_wise_score_avg = subject_wise_score_avg.sort_values(by='Score', ascending=True)

# 🖨️ Step 4: Print average score per subject
print("📊 Average Score by Subject:")
print(subject_wise_score_avg)

# ----------------------------------------------
# ❌ FAILED SCORE ANALYSIS (Score < 50)
# ----------------------------------------------

# 🔍 Step 5: Filter only failed scores (< 50)
failed_scores = merge_table[merge_table['Score'] < 50]

# 🔢 Step 6: Count number of failures per subject
fail_count_by_subject = failed_scores['Subject_ID'].value_counts()

# 🥇 Step 7: Identify subject with most failures
most_failed_subject = fail_count_by_subject.idxmax()
fail_count = fail_count_by_subject.max()

# 🖨️ Step 8: Display the subject with most failed students
print("📌 Most Failed Subject ID:", most_failed_subject)
print("❌ Number of students who scored < 50:", fail_count)

# ----------------------------------------------
# 🟢 HIGH PERFORMER ANALYSIS (Score > 90)
# ----------------------------------------------

# 🔍 Step 9: Filter only passed scores (> 90)
passed_scores = merge_table[merge_table['Score'] > 90]

# 🔢 Step 10: Count number of high scores per subject
pass_count_by_subject = passed_scores['Subject_ID'].value_counts()

# 🥇 Step 11: Identify subject with most high scores
most_passed_subject = pass_count_by_subject.idxmax()
pass_count = pass_count_by_subject.max()

# 🖨️ Step 12: Display the subject with most students scoring > 90
print("📌 Most Passed Subject ID:", most_passed_subject)
print("✅ Number of students who scored > 90:", pass_count)

