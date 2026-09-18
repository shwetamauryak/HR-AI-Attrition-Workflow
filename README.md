# HR AI Attrition Workflow

An end-to-end HR Employee Attrition Analysis project using **Python, Pandas, and n8n automation** to analyze employee attrition patterns and generate an automated HR report.

## 📌 Project Overview

Employee attrition is an important HR challenge. This project analyzes employee data to identify patterns related to:

* Overall employee attrition
* Overtime
* Income bands
* Job roles
* Job satisfaction
* Work-life balance

The analysis is performed using Python and Pandas, and an n8n workflow is used to automate the report-generation process.

## 🛠️ Tools & Technologies

* **Python**
* **Pandas**
* **Jupyter / VS Code**
* **n8n**
* **GitHub**
* **CSV Dataset**

## 📊 Key KPIs

| KPI                    |    Value |
| ---------------------- | -------: |
| Total Employees        |    1,470 |
| Attrition Count        |      237 |
| Attrition Rate         |   16.12% |
| Average Age            |    36.92 |
| Average Monthly Income | 6,502.93 |

## 🔎 Key Findings

* Employees working overtime had an attrition rate of **30.53%**, compared with **10.44%** for employees not working overtime.
* Employees in the **0–3K income band** had an attrition rate of **28.61%**.
* **Sales Representatives** had an attrition rate of **39.76%**.
* Employees with the lowest job satisfaction level had an attrition rate of **22.84%**.
* Employees with the lowest work-life balance level had an attrition rate of **31.25%**.

## ⚙️ Workflow

```text
Employee CSV Data
       ↓
Python + Pandas
       ↓
Data Analysis
       ↓
KPI Generation
       ↓
HR Report Generation
       ↓
n8n Automation
       ↓
Report File
```

## 📁 Project Structure

```text
HR-AI-Attrition-Workflow/
│
├── data.csv
├── analysis_summary.py
├── test_ai.py
├── generate_ai_prompt.py
├── hr_attrition_n8n_workflow.json
│
└── reports/
    ├── analysis_summary.json
    ├── ai_prompt.txt
    ├── generate_report.py
    └── hr_attrition_report.txt
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project folder

```bash
cd HR-AI-Attrition-Workflow
```

### 3. Install Pandas

```bash
pip install pandas
```

### 4. Run the analysis

```bash
python analysis_summary.py
```

This generates the analysis summary used by the reporting workflow.

### 5. Generate the HR report

```bash
python reports/generate_report.py
```

The report will be generated inside the `reports` folder.

## 🤖 n8n Automation

The project includes an exported n8n workflow:

```text
Manual Trigger
      ↓
HR Analysis Data
      ↓
Generate HR Report
      ↓
Convert Report to File
```

The workflow can be imported into n8n and used as the automation layer for the HR reporting process.

## 💡 Business Use Case

This project demonstrates how HR teams can use data analysis and workflow automation to:

* Monitor employee attrition
* Identify areas requiring HR investigation
* Generate repeatable reports
* Reduce manual reporting work
* Support data-driven HR decisions

## ⚠️ Note

The findings in this project represent **associations in the dataset and do not prove causation**. Further investigation would be required before making HR decisions.

## 👨‍💻 Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis
* Pandas
* KPI Analysis
* Business Insights
* Report Automation
* n8n Workflow Automation
* Git & GitHub
* Python Scripting
