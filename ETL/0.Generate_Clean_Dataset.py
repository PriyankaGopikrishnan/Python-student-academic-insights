import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# 1. 🎓 Students Table
student_ids = list(range(1001, 2001))
genders = np.random.choice(['Male', 'Female'], size=1000)
ages = np.random.randint(15, 19, size=1000)
addresses = np.random.choice(['Urban', 'Rural'], size=1000)
parent_education = np.random.choice(['High School', 'Bachelor', 'Masters', 'PhD'], size=1000)

students = pd.DataFrame({
    'Student_ID': student_ids,
    'Gender': genders,
    'Age': ages,
    'Address': addresses,
    'Parent_Education': parent_education
})

# 2. 📘 Subjects Table
subjects = pd.DataFrame({
    'Subject_ID': [1, 2, 3, 4, 5, 6],
    'Subject_Name': ['Math', 'Chemistry', 'Physics', 'Computers', ' English', 'Tamil']
})

# 3. 📊 Student Scores Table (Each student has 3 subject scores)
student_scores = pd.DataFrame([
    {'Student_ID': sid, 'Subject_ID': sub_id, 'Score': np.random.randint(40, 100)}
    for sid in student_ids
    for sub_id in [1, 2, 3, 4, 5, 6]
])

# 4. 📅 Attendance Table
absences = np.random.poisson(lam=3, size=1000)
study_time = np.random.choice(['<1 hour', '1-2 hours', '2-4 hours', '>4 hours'], size=1000)

attendance = pd.DataFrame({
    'Student_ID': student_ids,
    'Absences': absences,
    'Study_Time': study_time
})

# 5. ❤️ Health Table
health_ratings = np.random.randint(1, 6, size=1000)

health = pd.DataFrame({
    'Student_ID': student_ids,
    'Health': health_ratings
})

# 🎉 DONE! Now display a preview of each
print("STUDENTS\n", students.head(), "\n")
print("SUBJECTS\n", subjects, "\n")
print("STUDENT SCORES\n", student_scores.head(10), "\n")
print("ATTENDANCE\n", attendance.head(), "\n")
print("HEALTH\n", health.head(), "\n")

# Optional: Save to CSV for SQL or Tableau
students.to_csv('students.csv', index=False)
subjects.to_csv('subjects.csv', index=False)
student_scores.to_csv('student_scores.csv', index=False)
attendance.to_csv('attendance.csv', index=False)
health.to_csv('health.csv', index=False)
