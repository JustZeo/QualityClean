# Working with CSV Files

> Learn how to clean CSV datasets using QualityClean.

---

# Overview

CSV is one of the most widely used formats for storing tabular data.

QualityClean provides a simple workflow for loading, cleaning, auditing, and exporting CSV datasets with just a few lines of code.

This guide demonstrates the recommended workflow for working with CSV files.

---

# Complete Workflow

```python
import qualityclean as qc

# Load the dataset
df = qc.load("employees.csv")

# Clean the dataset
result = qc.clean(df)

# Generate an audit report
qc.audit(result)

# Export the cleaned dataset
qc.export(result, "employees_clean.csv")
```

This workflow is sufficient for most CSV cleaning tasks.

---

# Step 1 — Load the Dataset

Load a CSV file.

```python
import qualityclean as qc

df = qc.load("employees.csv")
```

The returned object is a Polars DataFrame.

---

# Step 2 — Clean the Dataset

Clean the dataset using the built-in cleaning pipeline.

```python
result = qc.clean(df)
```

QualityClean automatically performs:

- Column normalization
- Whitespace cleanup
- Empty value detection
- Datatype normalization
- Missing value handling
- Duplicate removal

---

# Step 3 — Inspect the Results

Access the cleaned DataFrame.

```python
clean_df = result.data
```

View the audit report.

```python
qc.audit(result)
```

Example output:

```text
QualityClean Report

Rows Processed       : 50,000
Columns Processed    : 18

Duplicates Removed   : 1,243
Missing Values Fixed : 892

Execution Time       : 0.18 seconds
```

---

# Step 4 — Export the Dataset

Export the cleaned data.

```python
qc.export(
    result,
    "employees_clean.csv",
)
```

The cleaned dataset is written to disk in CSV format.

---

# Recommended Workflow

```
employees.csv
      │
      ▼
qc.load()
      │
      ▼
qc.clean()
      │
      ▼
qc.audit()
      │
      ▼
qc.export()
      │
      ▼
employees_clean.csv
```

---

# Tips

✅ Keep the raw CSV unchanged.

✅ Save cleaned files with a different name.

✅ Review the audit report after every cleaning operation.

✅ Store audit reports alongside cleaned datasets.

---

# Best Practices

- Always validate your input data before analysis.
- Archive raw datasets separately.
- Export cleaned datasets instead of overwriting originals.
- Keep generated audit reports for reproducibility.

---

# Related Guides

- API Reference
- Cleaning Rules
- Working with Parquet Files

---

## What's Next?

Learn how to clean Parquet datasets using the same workflow.

➡️ **Next:** [Working with Parquet Files](parquet.md)

⬅️ **Previous:** [Duplicate Rule](../rules/duplicate-rule.md)