# Quick Start

> Clean your first dataset in less than two minutes.

---

# Overview

This guide walks through a complete QualityClean workflow.

By the end of this guide, you will know how to:

- Load a dataset
- Clean it
- View the audit report
- Export the cleaned data

No prior knowledge of QualityClean is required.

---

# Step 1 — Import QualityClean

```python
import qualityclean as qc
```

That's it.

Everything in QualityClean is available through the main package.

---

# Step 2 — Load Your Dataset

Load a CSV file.

```python
df = qc.load("employees.csv")
```

QualityClean currently supports:

- CSV
- Parquet

---

# Step 3 — Clean the Dataset

Clean the dataset using the default cleaning pipeline.

```python
result = qc.clean(df)
```

During cleaning, QualityClean automatically performs:

- Column normalization
- Whitespace cleanup
- Placeholder detection
- Datatype inference
- Missing value handling
- Duplicate removal

---

# Step 4 — Access the Clean Data

The cleaned DataFrame is available through:

```python
clean_df = result.data
```

You can continue working with it exactly like a normal Polars DataFrame.

```python
print(clean_df)
```

---

# Step 5 — View the Audit Report

Print a detailed audit report.

```python
qc.audit(result)
```

Example:

```text
QualityClean Report

Rows Processed       : 50000
Duplicates Removed   : 1243
Missing Values Fixed : 892
Whitespace Trimmed   : 3144

Execution Time       : 0.18 s
```

---

# Step 6 — Export the Clean Data

Export your cleaned dataset.

CSV

```python
qc.export(
    result,
    "cleaned.csv",
)
```

Parquet

```python
qc.export(
    result,
    "cleaned.parquet",
)
```

---

# Complete Example

```python
import qualityclean as qc

df = qc.load("employees.csv")

result = qc.clean(df)

qc.audit(result)

qc.export(result, "cleaned.parquet")

clean_df = result.data
```

This workflow is sufficient for most data cleaning tasks.

---

# Default Cleaning Pipeline

By default, QualityClean applies the following rules.

1. Column Rule
2. Whitespace Rule
3. Empty Rule
4. Datatype Rule
5. Missing Rule
6. Duplicate Rule

Each rule performs one dedicated task to keep the pipeline predictable.

---

# Common Workflow

```
Load
   │
   ▼
Clean
   │
   ▼
Audit
   │
   ▼
Export
```

This is the recommended workflow for most projects.

---

# Tips

- Keep the original dataset unchanged.
- Always review the audit report.
- Export cleaned datasets instead of overwriting raw data.
- Store raw and cleaned datasets separately.

---

# What's Next?

Now that you've completed your first cleaning workflow, explore the API Reference to learn about each function in detail.

➡️ **Next:** [API Reference - load()](api/load.md)

⬅️ **Previous:** [Installation](installation.md)