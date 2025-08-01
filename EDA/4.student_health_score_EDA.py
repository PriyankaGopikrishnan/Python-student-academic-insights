import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📥 Step 1: Load cleaned datasets
health_file = pd.read_csv('health_clean.csv')               # Contains Student_ID and Health rating (ideally 1–5)
score_file = pd.read_csv('student_scores_clean.csv')        # Contains Student_ID, Subject_ID, and Score

# 🔗 Step 2: Merge datasets on 'Student_ID' to analyze scores along with health ratings
merge_file = pd.merge(score_file, health_file, on='Student_ID')

# 🧹 Step 3: Filter out rows with invalid health ratings (e.g., 10, 15)
merge_file = merge_file[merge_file['Health'] < 6]

# 🧾 Optional: Print merged data for verification
print(merge_file)

# 📊 Step 4: Count number of students in each health score category (1 to 5)
health_distribution = merge_file['Health'].value_counts().sort_index()

# 🎨 Step 5: Create a bar chart to visualize the distribution of health scores
plt.figure(figsize=(8, 5))  # Set figure size
sns.barplot(x=health_distribution.index, y=health_distribution.values, palette='viridis')  # Colorful bars

# 🏷️ Customize the chart with title and axis labels
plt.title('🩺 Health Score Distribution of Students')
plt.xlabel('Health Rating (1 = Poor, 5 = Excellent)')
plt.ylabel('Number of Students')

# ➕ Add gridlines on y-axis for better readability
plt.grid(axis='y')

# 🎯 Step 6: Final layout adjustment and display the plot
plt.tight_layout()
plt.show()
