import pandas as pd

# Step 1: Load the cleaned student data
student_df = pd.read_csv('students_clean.csv')

# Step 2: Write EDA summary to a text file with UTF-8 encoding
with open("student_eda_report.txt", "w", encoding='utf-8') as report:

    report.write("🎓 STUDENT DATA EXPLORATORY REPORT\n")
    report.write("="*50 + "\n\n")

    # Count by Gender
    report.write("📌 Count of Students by Gender\n")
    report.write("-"*40 + "\n")
    gender_count = student_df['Gender'].value_counts()
    report.write(gender_count.to_string())
    report.write("\n\n")

    # Count by Parent Education Level
    report.write("📌 Count by Parent Education Level\n")
    report.write("-"*40 + "\n")
    parent_education_count = student_df['Parent_Education'].value_counts()
    report.write(parent_education_count.to_string())
    report.write("\n\n")

    # Count by Address
    report.write("📌 Count of Students by Address\n")
    report.write("-"*40 + "\n")
    address_count = student_df['Address'].value_counts()
    report.write(address_count.to_string())
    report.write("\n\n")

    # Count by Age
    report.write("📌 Count of Students by Age\n")
    report.write("-"*40 + "\n")
    age_count = student_df['Age'].value_counts().sort_index()
    report.write(age_count.to_string())
    report.write("\n\n")

print("✅ Report saved as 'student_eda_report.txt'")
