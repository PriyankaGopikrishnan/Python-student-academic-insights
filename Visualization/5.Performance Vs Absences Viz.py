import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 🔹 Step 1: Load cleaned datasets
student_df = pd.read_csv('student_scores_clean.csv')       # Contains Student_ID, Subject_ID, and Score
attendance_df = pd.read_csv('attendance_clean.csv')        # Contains Student_ID, Absences, Study_Time

# 🔹 Step 2: Merge datasets on Student_ID to combine score and attendance info
student_performance = pd.merge(student_df, attendance_df, on='Student_ID')
print(student_performance)

# 🔍 Step 3: Display the correlation between Absences and Score
print("\n🔍 Correlation between Absences and Score:")
print(student_performance[['Absences', 'Score']].corr())

# 📊 Step 4: Create a scatter plot to visualize the relationship between Absences and Score
plt.figure(figsize=(10, 6))  # Set figure size for better clarity
sns.scatterplot(x='Absences', y='Score', data=student_performance)

# 🏷️ Step 5: Add title and axis labels to the plot
plt.title('📉 Student Performance vs Absences')
plt.xlabel('Number of Absences')
plt.ylabel('Score')
plt.grid(True)  # Optional: add grid lines to improve readability

# 🎯 Step 6: Show the plot
plt.tight_layout()
plt.show()

# 📈 Step 7: Calculate and display average score by number of absences
avg_score_by_absence = student_performance.groupby('Absences')['Score'].mean().reset_index()
print("\n📊 Average score by number of absences:")
print(avg_score_by_absence)

# 📈 Step 8: Calculate and display average score by study time
avg_score_by_study_time = student_performance.groupby('Study_Time')['Score'].mean().reset_index()
print("\n📊 Average score by study time:")
print(avg_score_by_study_time)
