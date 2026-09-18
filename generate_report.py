import json
import os

# Read analysis summary
with open("reports/analysis_summary.json", "r") as file:
    data = json.load(file)

# Create report
report = f"""
HR ATTRITION ANALYSIS REPORT
=============================

1. OVERALL SUMMARY
------------------
Total Employees: {data["Total Employees"]}
Attrition Count: {data["Attrition Count"]}
Attrition Rate: {data["Attrition Rate"]}%
Average Age: {data["Average Age"]}
Average Monthly Income: {data["Average Monthly Income"]}


2. KEY FINDINGS
---------------
OverTime:
- No: {data["OverTime Attrition"]["No"]}% attrition
- Yes: {data["OverTime Attrition"]["Yes"]}% attrition

Income Band:
- 0-3K: {data["Income Band Attrition"]["0-3K"]}%
- 3K-6K: {data["Income Band Attrition"]["3K-6K"]}%
- 6K-10K: {data["Income Band Attrition"]["6K-10K"]}%
- 10K-15K: {data["Income Band Attrition"]["10K-15K"]}%
- 15K+: {data["Income Band Attrition"]["15K+"]}%


3. JOB ROLE PATTERNS
--------------------
"""

for role, rate in data["JobRole Attrition"].items():
    report += f"- {role}: {rate}%\n"

report += f"""

4. JOB SATISFACTION
-------------------
"""

for level, rate in data["Job Satisfaction Attrition"].items():
    report += f"- Satisfaction Level {level}: {rate}%\n"

report += f"""

5. WORK-LIFE BALANCE
--------------------
"""

for level, rate in data["Work Life Balance Attrition"].items():
    report += f"- Level {level}: {rate}%\n"

report += """

6. HR AREAS TO INVESTIGATE
--------------------------
- Overtime and workload patterns
- Attrition among lower-income employees
- High-attrition job roles
- Employee job satisfaction
- Work-life balance


7. BUSINESS RECOMMENDATIONS
---------------------------
1. Investigate workload and overtime patterns.
2. Review retention strategies for high-attrition job roles.
3. Examine compensation patterns among lower-income employees.
4. Monitor employee satisfaction levels.
5. Review work-life balance initiatives.

IMPORTANT:
These findings represent observed patterns in the dataset.
They do not establish causal relationships.
"""

# Create reports folder
os.makedirs("reports", exist_ok=True)

# Save report
with open("reports/hr_attrition_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("HR Attrition Report generated successfully!")
print("Saved at: reports/hr_attrition_report.txt")