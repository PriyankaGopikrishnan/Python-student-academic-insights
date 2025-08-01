import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the attendance.csv file using Pandas
score_file = pd.read_csv('student_scores_clean.csv')
print(score_file.head())

# Step 2 & 3: Group by Subject_ID and get average score
average_score_by_subject = score_file.groupby('Subject_ID')['Score'].mean().reset_index()

# Step 4 : Sort by average score
average_score_by_subject = average_score_by_subject.sort_values(by='Score', ascending=False)

# Step 5 (Optional): Display result
print(average_score_by_subject)
