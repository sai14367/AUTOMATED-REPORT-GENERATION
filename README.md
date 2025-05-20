# AUTOMATED REPORT GENERATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MASANAM VENKATA SAI KUMAR

*INTERN ID*: CT04DM174

*DOMAIN*: Python Programming 

 *DURATION*: 4 WEEEKS

*MENTOR*: NEELA SANTOSH

### 📌 Internship Project Submission

## 📘 Project Description

This project demonstrates how to automate the creation of professional PDF reports from raw data using Python. By combining data extraction, analysis, and report formatting in a single script, this project addresses the need for consistent and repeatable reporting workflows in academic, corporate, and research settings.

The script reads a CSV file containing structured data (like names and scores), processes it to extract summary statistics, and then generates a styled, structured PDF report. The PDF includes tables and statistical summaries presented in a clean, readable format. The main Python library used is `fpdf`, which enables simple yet powerful PDF creation directly from Python code.

---

## 🎯 Problem Statement

Manual reporting is time-consuming, error-prone, and lacks consistency. As data continues to grow in size and complexity, automating the reporting process becomes a critical need for organizations. This project solves the problem of manual report creation by offering a lightweight, customizable Python tool for generating reports programmatically.

---

## 🎯 Objectives

* Automate reading data from a structured file (CSV)
* Analyze and summarize data using Python
* Create a well-formatted PDF report using FPDF
* Support tabular and textual output in the report
* Ensure readability, reusability, and customization

---

## ⚙️ Key Features

* Reads data from any CSV file (e.g., student marks, sales records)
* Computes:

  * Average
  * Minimum and maximum values
  * Total record count
* Generates a styled PDF with:

  * Custom header/footer
  * Summary statistics
  * Tabular data layout
* Lightweight and easy to run
* Fully script-based — no web server required

---

## 📚 Technologies Used

* **Python 3.7+**
* **CSV module** (for data extraction)
* **FPDF** (for PDF generation)
* **Built-in Python functions** (for calculations)

---

## 📂 Folder Structure

```
Automated_Report_Generation/
│
├── generate_report.py       # Main script
├── sample_data.csv          # Sample input data
├── report.pdf               # Output report (auto-generated)
├── README.md                # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/Automated_Report_Generation.git
cd Automated_Report_Generation
```

### 2. Install Required Dependencies:

```bash
pip install fpdf
```

### 3. Add or Modify the Sample Data:

Create a file `sample_data.csv` with the following contents:

```csv
Name,Score
MVSK,88
SAI,75
KUMAR,95
UMA,62
SUBBU,79
```

### 4. Run the Script:

```bash
python generate_report.py
```

The script will generate a `report.pdf` in the current directory.

---

## 🖨️ Output Format

The PDF report includes:

* Title: e.g., "Student Score Report"
* Summary section:

  * Average Score
  * Minimum Score
  * Maximum Score
  * Total Number of Records
* Table section:

  * Each row includes Name and Score

---

## 🧪 Sample Use Cases

* 📊 Student performance reporting
* 📈 Sales reports for businesses
* 📉 Survey summaries and results
* 🧾 Invoice and receipt generation

---

## 🎓 Learning Outcomes

* Understand file handling in Python (CSV reading)
* Learn how to compute basic statistics programmatically
* Get hands-on experience with PDF creation in Python
* Learn formatting principles for readable reports
* Practice structuring Python projects for automation

---
**Screenshot Preview**

![Image](https://github.com/user-attachments/assets/59d2e17c-fc16-4464-b2d6-982170e5fa5b)


## ⚠️ Limitations

* CSV path is currently hardcoded; no GUI or dynamic file selection
* No support for multi-page tables or charts
* Report styling is basic and focused on clarity
* Not yet suitable for production environments with large datasets

---

## 🔮 Future Enhancements

* Add support for Excel (.xlsx) files
* Add graphical charts using matplotlib
* Provide CLI inputs for file name and report title
* Export reports to both PDF and HTML
* Handle missing data and bad formats more robustly
* Enable multi-language support for report content

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Make your changes in a new branch
3. Submit a pull request with a description of the changes

---

## 🙏 Acknowledgments

* **FPDF** — for making PDF generation accessible in Python
* **Python Docs** — for reliable and thorough reference
* **Visual Studio Code** — for an amazing development environment

---

## 👨‍💻 Author

Built by **Masanam Venkata Sai Kumar**
Connect on [LinkedIn](https://www.linkedin.com/in/venkata-sai-kumar-masanam-56458a27b)

Feel free to reach out for suggestions, collaborations, or freelance opportunities.
