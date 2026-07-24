# Working with Parquet Files

> Learn how to clean and export Parquet datasets using QualityClean.

---

# Overview

Parquet is a columnar storage format designed for high-performance analytics and efficient storage.

Compared to CSV, Parquet offers:

- Faster reading and writing
- Better compression
- Lower disk usage
- Improved analytical performance

QualityClean fully supports loading and exporting Parquet datasets.

---

# Complete Workflow

```python
import qualityclean as qc

# Load the dataset
df = qc.load("employees.parquet")

# Clean the dataset
result = qc.clean(df)

# Generate an audit report
qc.audit(result)

# Export the cleaned dataset
qc.export(result, "employees_clean.parquet")
```

This workflow is recommended for most Parquet datasets.

---

# Step 1 — Load the Dataset

Load a Parquet file.

```python
import qualityclean as qc

df = qc.load("employees.parquet")
```

The returned object is a Polars DataFrame.

---

# Step 2 — Clean the Dataset

Run the default cleaning pipeline.

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

# Step 3 — Review the Audit Report

Inspect the cleaning summary.

```python
qc.audit(result)
```

Example:

```text
QualityClean Report

Rows Processed        : 250,000
Columns Processed     : 32

Duplicate Rows Removed: 2,145
Missing Values Fixed  : 1,089

Execution Time        : 0.74 seconds
```

---

# Step 4 — Export the Dataset

Save the cleaned dataset.

```python
qc.export(
    result,
    "employees_clean.parquet",
)
```

The exported file remains in Parquet format.

---

# Why Use Parquet?

Parquet is often a better choice than CSV for production workflows.

| Feature | CSV | Parquet |
|----------|-----|----------|
| Human-readable | ✅ | ❌ |
| Compression | ❌ | ✅ |
| Storage Efficiency | Low | High |
| Read Performance | Good | Excellent |
| Write Performance | Good | Excellent |
| Analytics | Good | Excellent |

---

# Recommended Workflow

```
employees.parquet
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
employees_clean.parquet
```

---

# Tips

✅ Use Parquet for large datasets.

✅ Preserve the original Parquet file.

✅ Generate an audit report after every cleaning operation.

✅ Use Parquet when building analytics or machine learning pipelines.

---

# Best Practices

- Store raw and cleaned datasets separately.
- Archive audit reports for reproducibility.
- Prefer Parquet for datasets with many rows or columns.
- Keep file names descriptive.

---

# Related Guides

- Working with CSV Files
- API Reference
- Cleaning Rules

---

## What's Next?

Learn how to build custom cleaning workflows with QualityClean.

➡️ **Next:** [Custom Pipeline](custom-pipeline.md)

⬅️ **Previous:** [Working with CSV Files](csv.md)