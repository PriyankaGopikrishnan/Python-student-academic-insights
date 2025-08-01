import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the cleaned student data
student_df = pd.read_csv('students_clean.csv')

# Step 2: Count the number of students by gender
# value_counts() gives frequency of each gender
# reset_index() turns it into a DataFrame
gender_count = student_df['Gender'].value_counts().reset_index()
print(gender_count)
# 🔍 At this stage, columns are named like: ['index', 'Gender']
# Rename them properly for clarity
gender_count.columns = ['Gender', 'Count']


# Step 3: Set 'Gender' as index to use as x-axis labels in the bar chart
gender_count.set_index('Gender', inplace=True)

# Step 4: Create the bar plot
gender_count.plot(kind='bar', title='Student Count by Gender', legend=False)

# Step 5: Add axis labels
plt.xlabel('Gender')
plt.ylabel('Count')

# Step 6: Show the plot
plt.show()