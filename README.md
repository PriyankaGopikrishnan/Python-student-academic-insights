# Python-student-academic-insights
 # 📊 Student Performance Analysis

A comprehensive end-to-end data analysis project using PYTHON & TABLEAU, based on synthetic student data representing real-world educational scenarios. This project covers data generation, data cleaning, EDA (Exploratory Data Analysis), and visual storytelling.

---

## 📁 Project Structure

Python-Student-Academic-Insights/
│
├── 📁 data/
│   ├── students.csv
│   ├── student_scores.csv
│   ├── attendance.csv
│   ├── health.csv
│   └── subjects.csv
│
├── 📁 scripts/
│   ├── generate_clean_dataset.py
│   ├── inject_unclean_dataset.py
│   ├── data_cleaning.py
│   ├── eda_students.py
│   ├── eda_scores.py
│   ├── eda_attendance.py
│   ├── eda_health.py
│   └── combined_analysis.py
│
├── 📁 notebooks/                  ← (optional if you convert to .ipynb)
│   ├── 01_data_generation.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_outlier_report.ipynb
│   ├── 04_eda_students.ipynb
│   └── 05_combined_analysis.ipynb
│
├── 📁 outputs/
│   ├── student_score_summary.csv
│   ├── outliers_report.csv
│   └── visualizations/           ← charts/images (PNG, SVG, etc.)
│
├── 📄 README.md                   ← Project overview & usage instructions
├── 📄 requirements.txt            ← List of libraries (e.g., pandas, matplotlib)
└── 📄 .gitignore                  ← To ignore __pycache__/, .ipynb_checkpoints/
---

## 🚀 Overview

### ✅ Step 1: Data Generation

* Created **5 synthetic tables** using Python Faker and NumPy libraries:

  * `students`, `subjects`, `student_scores`, `attendance`, `health`

### ✅ Step 2: Data Corruption Simulation

* Injected nulls, outliers, and unrealistic values to simulate real-world dirty data.

### ✅ Step 3: Data Cleaning

* Removed nulls, handled outliers, corrected unrealistic health scores.
* Ensured valid data types for all columns.

### ✅ Step 4: Outlier & Data Validation Reports

* Generated outlier report for `student_scores` and `health`.
* Checked data types, missing values, and duplicates.

---

## 🔎 Exploratory Data Analysis (EDA)

### 🎓 Students Table

* Count of students by:

  * Age group
  * Address type (Urban/Rural)
  * Parent education level
  * Gender
* Visualizations: Bar charts and count plots
* Generated a full **Student Demographics Report**

### 🧠 Health Table

* Health Score Distribution (1 to 5)
* Health Score by:

  * Gender
  * Address Type
  * Age
  * Flagged low health scores (≤2)

### 📘 Student Scores Table

* Average score per subject
* Score distribution and histogram
* Identify:

  * Failures (score < 40)
  * Top scorers (score > 90)
  * Gender-wise score trends

### 🗓 Attendance Table

* Average absences by study time
* Absences statistics (min, max, mean)
* Identify:

  * Zero absentees
  * Students with high absences
* Study time distribution and duplicate detection

---

## 🔗 Cross-Table Analysis

* **Health Score vs Academic Score**
* **Health vs Parent Education**
* **Absences vs Performance**
* **Study Time vs Average Score**
* **Gender-wise Subject Performance**
* **Score Trends by Age Group**

---

## 📊 Tableau Dashboard

Created an interactive **Tableau dashboard** to showcase:

* Demographics
* Performance trends
* Absence vs Score impact
* Health insights

> ✅ 

---

## 🛠️ Tools Used

* **Python**: Pandas, NumPy, Seaborn, Matplotlib
* **Tableau**: Interactive dashboard visualizations


---

## 📌 Key Learnings

* ETL Process Simulation (Extract, Transform, Load)
* Real-world data cleaning strategies
* Multidimensional EDA across 5 related tables
* Storytelling through data visualizations
* Preparing data for business dashboard reporting

---



## ✨ Contact

**Author:Priyanka Gopikrishnan
📧 mailto:pinkyvais@gmail.com
📍 India
🔗 https://www.linkedin.com/in/priyanka-t-g-46723666/
