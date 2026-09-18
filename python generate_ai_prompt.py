import json
import os

# Read analysis summary
with open("reports/analysis_summary.json", "r") as file:
    summary = json.load(file)

# Create AI prompt
prompt = f"""
You are an HR Data Analyst.

Analyze the following employee attrition analysis:

{json.dumps(summary, indent=4)}

Generate a professional HR Attrition Analysis Report with:

1. Overall attrition summary
2. Key findings
3. Important patterns by Job Role
4. Impact of Overtime
5. Income-related attrition patterns
6. Job Satisfaction findings
7. Work-Life Balance findings
8. Possible areas HR should investigate
9. 5 concise business recommendations

Important:
- Use only the provided data.
- Do not claim that one factor causes attrition.
- Clearly mention that these are observed patterns, not causal conclusions.
- Keep the report professional and suitable for management.
"""

# Create reports folder if needed
os.makedirs("reports", exist_ok=True)

# Save prompt
with open("reports/ai_prompt.txt", "w", encoding="utf-8") as file:
    file.write(prompt)

print("AI prompt created successfully!")
print("Saved at: reports/ai_prompt.txt")