# 📊 CSV Summary Analyzer

A lightweight **Python command-line application** that analyzes any CSV file and generates a clean, readable summary report. It provides dataset shape, column information, missing value analysis, and descriptive statistics for numeric data.

**Built with:** Python 3 · Pandas · argparse

---

## ✨ Features

* Analyze any valid CSV file from the terminal
* Display total rows and columns
* Show column names and data types
* Detect missing values with counts and percentages
* Calculate mean, median, minimum, maximum, and standard deviation
* Save the report as a `.txt` file
* Graceful error handling for missing, empty, and invalid CSV files
* Clean, modular, and reusable Python code

---

## 📁 Project Structure

```text
csv-summary-analyzer/
├── data/
│   └── student_dataset.csv
├── reports/
│   └── example_report.txt
├── csv_summary_analyzer.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

```bash
git clone https://github.com/dusa-neeraj/csv-summary-analyzer.git
cd csv-summary-analyzer

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

---

## 💻 Usage

Run the analyzer:

```bash
python csv_summary_analyzer.py data/student_dataset.csv
```

Save the report:

```bash
python csv_summary_analyzer.py data/student_dataset.csv --output reports/report.txt
```

---

## 📋 Sample Output

```text
============================================================
               CSV SUMMARY ANALYZER REPORT
============================================================
File Analyzed : data/student_dataset.csv
============================================================

1. DATASET OVERVIEW
----------------------------------------
Total Rows    : 100
Total Columns : 7

2. COLUMN NAMES & DATA TYPES
----------------------------------------
student_id                object
name                      object
age                       int64
cgpa                      float64
attendance                float64
city                      object
join_date                 object

3. MISSING VALUES PER COLUMN
----------------------------------------
cgpa                      3        (3.00%)
attendance                2        (2.00%)

4. NUMERIC COLUMN STATISTICS
----------------------------------------
Age  → Mean: 20.35
CGPA → Mean: 7.71
============================================================
```

---

## ⚠️ Error Handling

The application handles common failures gracefully:

* File not found
* Empty CSV files
* Invalid or corrupted CSV files
* Datasets without numeric columns

---

## 🛠️ Technologies Used

* Python 3
* Pandas
* argparse
* Git & GitHub

---

## 👨‍💻 Author

**Neeraj Dusa**

B.Tech CSE (Data Science) • Aspiring Software Developer
