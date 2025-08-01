import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 📥 Step 1: Load the cleaned attendance data
attendance_file = pd.read_csv('attendance_clean.csv')

print('--'*30)
print('Attendance_Table')
print('--'*30)
print(attendance_file.head())  # Show the first few rows

# 📊 Step 2: Basic statistical summary of numeric columns
print('--'*30)
print('Statistical summary')
print('--'*30)
print(attendance_file.describe())

# 🔍 Step 3: Check for duplicate rows

duplicate_count = attendance_file.duplicated().sum()
print('--'*30)
print(f"Total duplicate rows in attendance table: {duplicate_count}")
print('--'*30)


# 📌 Step 4: Count of students by number of absences
print('--'*30)
print('Count of students by number of absences')
print('--'*30)
stu_absences = attendance_file['Absences'].value_counts().reset_index()
print(stu_absences)

# 📌 Step 5: Count of students by study time category
print('--'*30)
print('Count of students by study time category')
print('--'*30)
study_time_count = attendance_file['Study_Time'].value_counts().reset_index()
study_time_count.columns = ['Study_Time', 'Count']  # Rename columns for clarity
print(study_time_count)

# 📈 Step 6: Calculate average absences for each study time group
print('--'*30)
print('Average absences for each study time group')
print('--'*30)
avg_absences = attendance_file.groupby('Study_Time')['Absences'].mean().reset_index()
print(avg_absences)


# 🎯 Step 7: Identify students who never missed class (Absences == 0)
print('--'*30)
zero_absent_students = attendance_file[attendance_file['Absences'] == 0]
print('Number of Students who never missed class!: ', zero_absent_students['Student_ID'].count())
print('--'*30)
print('Students who never missed class ')
print('--'*30)
print(zero_absent_students)

# 🔺 Step 8: Identify high absentee students (above 90th percentile)
print('--'*30)
print('High Absentees')
print('--'*30)
threshold = attendance_file['Absences'].quantile(0.90)
high_absentees = attendance_file[attendance_file['Absences'] > threshold]
print(high_absentees.head())
print('Students who are absences above the threshold: ', high_absentees['Student_ID'].count())

# 🔢 Step 9: Count of unique students in the table
print(f"Unique Students: {attendance_file['Student_ID'].nunique()}")

# 📊 Step 10:  Combine pie chart and bar chart into one figure
fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns

# 📌 Pie chart for Study Time Distribution
attendance_file['Study_Time'].value_counts().plot(kind='pie', ax=axes[0], autopct='%1.1f%%', startangle=90)
axes[0].set_title('Study Time Distribution')
axes[0].set_ylabel('')  # Hide y-axis label

# 📌 Bar chart for Average Absences by Study Time
sns.barplot(x='Study_Time', y='Absences', data=avg_absences, ax=axes[1])
axes[1].set_title('Average Absences by Study Time')
axes[1].set_xlabel('Study Time')
axes[1].set_ylabel('Average Absences')

# 📷 Display the combined plots
plt.tight_layout()
plt.show()
