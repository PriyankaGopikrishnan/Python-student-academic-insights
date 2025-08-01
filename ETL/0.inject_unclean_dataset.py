# 📦 Import Libraries
import pandas as pd
import numpy as np
import random

# 🔄 Load clean data
students = pd.read_csv('students.csv')
attendance = pd.read_csv('attendance.csv')
health = pd.read_csv('health.csv')
student_scores = pd.read_csv('student_scores.csv')

# 📋 Make copies for unclean versions
students_unclean = students.copy()
attendance_unclean = attendance.copy()
health_unclean = health.copy()
student_scores_unclean = student_scores.copy()

# 🎲 Set seed for reproducibility
np.random.seed(42)

# 🚫 Introduce NULLS
students_unclean.loc[np.random.choice(students_unclean.index, 20, replace=False), 'Parent_Education'] = np.nan
students_unclean.loc[np.random.choice(students_unclean.index, 10, replace=False), 'Gender'] = np.nan
attendance_unclean.loc[np.random.choice(attendance_unclean.index, 15, replace=False), 'Absences'] = np.nan
health_unclean.loc[np.random.choice(health_unclean.index, 12, replace=False), 'Health'] = np.nan
student_scores_unclean.loc[np.random.choice(student_scores_unclean.index, 40, replace=False), 'Score'] = np.nan

# 💥 Add OUTLIERS
# Add extreme scores
outlier_scores = [300, -50, 999]  # unrealistic values
score_outlier_indices = np.random.choice(student_scores_unclean.index, len(outlier_scores), replace=False)
for i, idx in enumerate(score_outlier_indices):
    student_scores_unclean.loc[idx, 'Score'] = outlier_scores[i]

# Add unrealistic health ratings
outlier_health = [0, 10, 15]  # outside typical health scale
health_outlier_indices = np.random.choice(health_unclean.index, len(outlier_health), replace=False)
for i, idx in enumerate(health_outlier_indices):
    health_unclean.loc[idx, 'Health'] = outlier_health[i]

# 🔡 Convert AGE to STRING
students_unclean['Age'] = students_unclean['Age'].astype(str)

# 🔍 Check for issues
print("\n🔍 Nulls in Students:\n", students_unclean.isnull().sum())
print("\n🔍 Nulls in Attendance:\n", attendance_unclean.isnull().sum())
print("\n🔍 Nulls in Health:\n", health_unclean.isnull().sum())
print("\n🔍 Nulls in Student Scores:\n", student_scores_unclean.isnull().sum())

# 💾 Save updated uncleaned files
students_unclean.to_csv('students_unclean.csv', index=False)
attendance_unclean.to_csv('attendance_unclean.csv', index=False)
health_unclean.to_csv('health_unclean.csv', index=False)
student_scores_unclean.to_csv('student_scores_unclean.csv', index=False)

print("\n✅ Unclean data (with nulls, outliers, and datatype issues) generated and saved.")
