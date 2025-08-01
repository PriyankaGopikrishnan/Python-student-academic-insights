import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and merge data
subjects_file = pd.read_csv('subjects.csv')
score_file = pd.read_csv('student_scores_clean.csv')
merge_table = pd.merge(score_file, subjects_file, on='Subject_ID')

# Set style
sns.set(style="whitegrid")

# 🔴 Failed Scores (Score < 50)
failed_scores = merge_table[merge_table['Score'] < 50]
fail_count_by_subject = failed_scores['Subject_ID'].value_counts().reset_index()
fail_count_by_subject.columns = ['Subject_ID', 'Fail_Count']
fail_count_by_subject = pd.merge(fail_count_by_subject, subjects_file, on='Subject_ID')

# 🟢 High Scores (Score > 90)
passed_scores = merge_table[merge_table['Score'] > 90]
pass_count_by_subject = passed_scores['Subject_ID'].value_counts().reset_index()
pass_count_by_subject.columns = ['Subject_ID', 'Pass_Count']
pass_count_by_subject = pd.merge(pass_count_by_subject, subjects_file, on='Subject_ID')

# 📊 Create subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# 🔴 Plot Failures
sns.barplot(data=fail_count_by_subject, x='Subject_Name', y='Fail_Count', color='salmon', ax=axes[0])
axes[0].set_title('Students Scored < 50 by Subject')
axes[0].set_xlabel('Subject')
axes[0].set_ylabel('Fail Count')
axes[0].tick_params(axis='x', rotation=45)

# 🟢 Plot High Scores
sns.barplot(data=pass_count_by_subject, x='Subject_Name', y='Pass_Count', color='lightgreen', ax=axes[1])
axes[1].set_title('Students Scored > 90 by Subject')
axes[1].set_xlabel('Subject')
axes[1].set_ylabel('High Score Count')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
