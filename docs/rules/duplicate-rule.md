# Duplicate Rule

> Identify and remove duplicate records to ensure every row in the dataset is unique.

---

# Overview

The **Duplicate Rule** is the final step in the QualityClean cleaning pipeline.

Its purpose is to identify and remove duplicate rows that may have been introduced through data entry errors, repeated imports, or merged datasets.

Duplicate records can distort statistics, inflate counts, and negatively impact machine learning models. Removing them ensures that each observation is represented only once.

---

# Why This Rule Exists

Duplicate records are common in real-world datasets.

For example:

| employee_id | name | department |
|-------------|------|------------|
| 101 | Alice | Sales |
| 102 | Bob | HR |
| 101 | Alice | Sales |

The third row is an exact duplicate of the first.

If duplicates remain:

- Counts become inaccurate.
- Aggregations produce incorrect results.
- Reports overestimate values.
- Machine learning models may become biased.

The Duplicate Rule removes these unnecessary records.

---

# What Gets Cleaned?

The Duplicate Rule identifies rows where every column contains identical values.

Duplicate rows are removed while preserving the first occurrence.

---

# Example

## Before

| employee_id | name | department |
|-------------|------|------------|
| 101 | Alice | Sales |
| 102 | Bob | HR |
| 101 | Alice | Sales |
| 103 | Charlie | IT |

---

## After

| employee_id | name | department |
|-------------|------|------------|
| 101 | Alice | Sales |
| 102 | Bob | HR |
| 103 | Charlie | IT |

---

# Example Code

```python
import qualityclean as qc

df = qc.load("employees.csv")

result = qc.clean(df)

print(result.df)
```

Duplicate rows are automatically removed during the cleaning process.

---

# Benefits

Removing duplicate records provides several advantages.

- Accurate row counts
- More reliable statistical analysis
- Improved machine learning performance
- Cleaner reports
- Reduced storage requirements

---

# Execution Order

The Duplicate Rule always runs last.

```
Column Rule
      ↓
Whitespace Rule
      ↓
Empty Rule
      ↓
Datatype Rule
      ↓
Missing Rule
      ↓
Duplicate Rule
```

Running this rule after all previous cleaning steps ensures duplicate detection is based on standardized and normalized data.

---

# Performance

Duplicate detection is performed using Polars' optimized DataFrame operations, making it efficient even for large datasets.

Performance depends primarily on:

- Number of rows
- Number of columns
- Available system memory

---

# Notes

- Only exact duplicate rows are removed.
- The first occurrence of each duplicate is preserved.
- Unique rows are never modified.
- The original input DataFrame remains unchanged.
- The number of removed duplicates is included in the audit report.

---

# Best Practices

✅ Review duplicate statistics in the audit report.

✅ Investigate why duplicates exist before removing them.

✅ Keep a backup of the original dataset.

✅ Verify that duplicate removal aligns with your project's requirements.

---

# Related Rules

- Missing Rule
- Column Rule

---

# Complete Cleaning Pipeline

QualityClean applies its built-in rules in the following order:

1. Column Rule
2. Whitespace Rule
3. Empty Rule
4. Datatype Rule
5. Missing Rule
6. Duplicate Rule

This sequence ensures that each rule builds upon the previous one, producing clean and consistent datasets.

---

## What's Next?

You've now learned how every built-in cleaning rule works.

Continue to the Examples section to see complete workflows for real-world datasets.

➡️ **Next:** [Examples](../examples/csv.md)

⬅️ **Previous:** [Missing Rule](missing-rule.md)