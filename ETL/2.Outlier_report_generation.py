import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
student_scores_file = pd.read_csv('student_scores_clean.csv')
health_file = pd.read_csv('health_clean.csv')

# Create subplots: 1 row, 2 columns
fig, axes = plt.subplots(1, 2, figsize=(10, 5))  # Wider figure

# --------------------------
# Plot 1: Score by Subject (Seaborn)
# --------------------------
sns.boxplot(x='Subject_ID',
            y='Score',
            data=student_scores_file, ax=axes[0],
            flierprops=dict(marker='o', markerfacecolor='red', markersize=6, linestyle='none')  # 🔴 Red circles)
            )
axes[0].set_title('Score Distribution by Subject')
axes[0].set_xlabel('Subject ID')
axes[0].set_ylabel('Score')

# --------------------------
# Plot 2: Health Scores (Matplotlib)
# --------------------------
axes[1].boxplot(health_file['Health'],
                patch_artist=True,
                boxprops=dict(facecolor='lightblue'),
                flierprops=dict(marker='*', markerfacecolor='red', markersize=8))
axes[1].set_title('Health Score Outlier Detection')
axes[1].set_xlabel('Health')
axes[1].set_ylabel('Value')

# --------------------------
# Show both plots together
# --------------------------
plt.tight_layout()
plt.show()
