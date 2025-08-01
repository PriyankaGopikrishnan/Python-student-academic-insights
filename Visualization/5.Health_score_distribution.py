import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📥 Step 1: Load cleaned student demographic and health datasets

health_file = pd.read_csv('health_clean.csv')          # Contains Student_ID, Health (e.g., health rating score)
score_file = pd.read_csv('student_scores_clean.csv')
# 🔗 Step 2: Merge both datasets on 'Student_ID' to combine health data with student demographics
merge_file = pd.merge(score_file, health_file, on='Student_ID')
merge_file = merge_file[merge_file['Health']<6]
print(merge_file)

health_distribution = merge_file['Health'].value_counts().sort_index()

plt.figure(figsize=(8, 5))
sns.barplot(x=health_distribution.index, y=health_distribution.values, palette='viridis')
plt.title('🩺 Health Score Distribution of Students')
plt.xlabel('Health Rating (1 = Poor, 5 = Excellent)')
plt.ylabel('Number of Students')
plt.grid(axis='y')

# 🎯 Step 6: Show the plot
plt.tight_layout()
plt.show()



