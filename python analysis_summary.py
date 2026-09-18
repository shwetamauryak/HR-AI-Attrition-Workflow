import pandas as pd
import json
import os

# Load data
df = pd.read_csv("data.csv")

# Basic KPIs
total_employees = len(df)
attrition_count = (df["Attrition"] == "Yes").sum()
attrition_rate = (attrition_count / total_employees) * 100

# Overtime analysis
overtime_attrition = df.groupby("OverTime")["Attrition"].apply(
    lambda x: round((x == "Yes").mean() * 100, 2)
).to_dict()

# Income band analysis
df["IncomeBand"] = pd.cut(
    df["MonthlyIncome"],
    bins=[0, 3000, 6000, 10000, 15000, float("inf")],
    labels=["0-3K", "3K-6K", "6K-10K", "10K-15K", "15K+"]
)

income_attrition = df.groupby(
    "IncomeBand", observed=False
)["Attrition"].apply(
    lambda x: round((x == "Yes").mean() * 100, 2)
).to_dict()

# Job role analysis
jobrole_attrition = df.groupby("JobRole")["Attrition"].apply(
    lambda x: round((x == "Yes").mean() * 100, 2)
).sort_values(ascending=False).to_dict()

# Job satisfaction
satisfaction_attrition = df.groupby("JobSatisfaction")["Attrition"].apply(
    lambda x: round((x == "Yes").mean() * 100, 2)
).to_dict()

# Work-life balance
worklife_attrition = df.groupby("WorkLifeBalance")["Attrition"].apply(
    lambda x: round((x == "Yes").mean() * 100, 2)
).to_dict()

# Final summary
summary = {
    "Total Employees": total_employees,
    "Attrition Count": int(attrition_count),
    "Attrition Rate": round(attrition_rate, 2),
    "Average Age": round(df["Age"].mean(), 2),
    "Average Monthly Income": round(df["MonthlyIncome"].mean(), 2),
    "OverTime Attrition": overtime_attrition,
    "Income Band Attrition": income_attrition,
    "JobRole Attrition": jobrole_attrition,
    "Job Satisfaction Attrition": satisfaction_attrition,
    "Work Life Balance Attrition": worklife_attrition
}

# Create reports folder
os.makedirs("reports", exist_ok=True)

# Save JSON summary
with open("reports/analysis_summary.json", "w") as file:
    json.dump(summary, file, indent=4)

print("Analysis summary created successfully!")
print("Saved at: reports/analysis_summary.json")