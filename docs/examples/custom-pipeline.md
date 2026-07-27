# Custom Pipeline

> Build your own data cleaning workflow using QualityClean.

---

# Overview

Although QualityClean provides a complete automated cleaning pipeline, you can integrate its functions into your own preprocessing workflow.

This is useful when your project requires additional transformations before or after the built-in cleaning process.

---

# Why Build a Custom Pipeline?

Every dataset is different.

You may want to:

- Validate data before cleaning
- Filter unwanted rows
- Merge multiple datasets
- Perform feature engineering
- Generate custom reports
- Export to different locations

QualityClean fits naturally into these workflows.

---

# Example Workflow

```python
import polars as pl
import qualityclean as qc

# Load data
df = qc.load("employees.csv")

# Custom preprocessing
df = df.filter(pl.col("salary") > 0)

# Clean dataset
result = qc.clean(df)

# Generate audit report
qc.audit(result)

# Access cleaned data
clean_df = result.df

# Custom transformation
clean_df = clean_df.with_columns(
    (pl.col("salary") * 1.10).alias("updated_salary")
)

# Export final dataset — export clean_df directly, not `result`
clean_df.write_csv("employees_clean.csv")
```

!!! warning "Exporting `result` after modifying `clean_df` loses your changes"
    `clean_df.with_columns(...)` returns a **new** DataFrame — it does not mutate `result.df` in place (Polars DataFrames are immutable). If you call `qc.export(result, ...)` after transforming `clean_df`, you'll export the pre-transformation data and silently lose `updated_salary`. Once you've modified `clean_df` yourself, export it directly with Polars (`clean_df.write_csv(...)` / `.write_parquet(...)`) instead of passing `result` back to `qc.export()`.

---

# Workflow Breakdown

```
Load Data
      │
      ▼
Custom Processing
      │
      ▼
QualityClean
      │
      ▼
Audit Report
      │
      ▼
Additional Processing
      │
      ▼
Export
```

This approach allows you to combine your own business logic with QualityClean's automated cleaning.

---

# Example: Filter Before Cleaning

Remove invalid records before running the cleaning pipeline.

```python
import polars as pl

df = qc.load("employees.csv")

df = df.filter(
    pl.col("salary") > 0
)

result = qc.clean(df)
```

---

# Example: Create New Columns

You can continue using Polars after cleaning.

```python
clean_df = result.df

clean_df = clean_df.with_columns(
    (
        pl.col("salary") * 12
    ).alias("annual_salary")
)
```

---

# Example: Export After Custom Processing

If you've made additional changes to `result.df`, export the final DataFrame directly with Polars.

```python
clean_df.write_csv("employees_final.csv")
```

Or, if no further modifications were made after `qc.clean()`, you can use:

```python
qc.export(
    result,
    "employees_clean.csv",
)
```

---

# Best Practices

✅ Perform dataset-specific transformations before cleaning when appropriate.

✅ Use the built-in cleaning pipeline instead of rewriting common cleaning logic.

✅ Review the audit report after every cleaning operation.

✅ Keep raw, cleaned, and processed datasets separate.

---

# Common Workflow

```text
Raw Dataset
      │
      ▼
Custom Validation
      │
      ▼
QualityClean
      │
      ▼
Audit Report
      │
      ▼
Feature Engineering
      │
      ▼
Modeling / Analysis / Export
```

---

# Related Guides

- Working with CSV Files
- Working with Parquet Files
- API Reference
- Cleaning Rules

---

## What's Next?

You've now completed the examples section.

If you'd like to contribute to QualityClean, learn how to set up the project, run tests, and submit changes.

➡️ **Next:** [Contributing](../contributing.md)

⬅️ **Previous:** [Working with Parquet Files](parquet.md)