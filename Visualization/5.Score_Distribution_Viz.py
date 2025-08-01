import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📥 Step 1: Load the cleaned score and student datasets
# - score_file includes Student_ID, Subject_ID, and Score
# - student_file includes Student_ID, Gender, Age, and other demographic info
score_file = pd.read_csv('student_scores_clean.csv')
student_file = pd.read_csv('students_clean.csv')

# 🔗 Step 2: Merge both datasets on 'Student_ID'
# This combines student demographic data with their score records
merge_table = pd.merge(student_file, score_file, on='Student_ID')

# 🖨️ Step 3: Print merged column names to verify structure
print(merge_table.columns)

# 🎨 Step 4: Set visual style and plot the histogram
sns.set(style="dark")  # Apply a dark background style for better contrast

# 🟦 Step 5: Create histogram of the Score column with KDE (smooth curve)
sns.histplot(
    merge_table['Score'],   # Data to plot
    bins=10,                # Number of bins (intervals) in the histogram
    kde=True                # Overlay Kernel Density Estimate curve
)

# 🏷️ Step 6: Add plot title and axis labels
plt.title('Score Distribution - Overall', fontsize=16)
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.tight_layout()  # Adjust layout for clean display

# 📊 Step 7: Show the final plot
plt.show()
