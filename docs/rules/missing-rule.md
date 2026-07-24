# Missing Rule

> Handle missing values consistently to improve data quality and downstream analysis.

---

# Overview

The **Missing Rule** processes missing values (`null`) in your dataset after placeholder values have been standardized by the Empty Rule.

Missing values are common in real-world datasets and can negatively affect statistical analysis, machine learning models, and business reports.

The Missing Rule ensures missing data is handled consistently according to QualityClean's cleaning strategy.

---

# Why This Rule Exists

Consider the following dataset.

| employee | salary |
|----------|---------|
| Alice | 50000 |
| Bob | null |
| Charlie | 62000 |
| David | null |

Without handling missing values:

- Statistical calculations may be inaccurate.
- Machine learning models may reject the dataset.
- Filtering and aggregations become unreliable.
- Visualizations may contain unexpected gaps.

The Missing Rule identifies and processes these values in a consistent manner.

---

# What Gets Cleaned?

The Missing Rule operates on actual `null` values.

These values may originate from:

- Missing data in the original dataset
- Placeholder values converted by the Empty Rule
- Existing null values

Depending on the cleaning configuration, QualityClean may:

- Preserve missing values
- Fill missing values
- Remove rows containing excessive missing data

---

# Example

## Before

| employee | salary |
|----------|---------|
| Alice | 50000 |
| Bob | null |
| Charlie | 62000 |
| David | null |

---

## After

Example (preserving missing values)

| employee | salary |
|----------|---------|
| Alice | 50000 |
| Bob | null |
| Charlie | 62000 |
| David | null |

The exact behavior depends on the configured cleaning strategy.

---

# Example Code

```python
import qualityclean as qc

df = qc.load("employees.csv")

result = qc.clean(df)

print(result.data)
```

The Missing Rule automatically processes missing values during the cleaning pipeline.

---

# Benefits

Handling missing values correctly provides several advantages.

- More reliable statistical analysis
- Better machine learning compatibility
- Improved data consistency
- Easier downstream processing
- Cleaner visualizations

---

# Execution Order

The Missing Rule runs after datatype normalization.

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

Running after datatype inference ensures missing values are represented consistently across all columns.

---

# Performance

Missing value detection is optimized for Polars DataFrames and scales efficiently with dataset size.

Only columns containing missing values require additional processing.

---

# Notes

- Existing null values are preserved unless configured otherwise.
- Placeholder values are handled by the Empty Rule before reaching this step.
- The original DataFrame is never modified.
- Missing value handling is recorded in the audit report.

---

# Best Practices

✅ Review missing value statistics before training machine learning models.

✅ Understand why values are missing before deciding how to handle them.

✅ Always inspect the audit report to see how many missing values were detected or processed.

✅ Keep the original dataset for reproducibility.

---

# Related Rules

- Empty Rule
- Duplicate Rule

---

## What's Next?

The final step of the cleaning pipeline removes duplicate records to ensure each observation is unique.

➡️ **Next:** [Duplicate Rule](duplicate-rule.md)

⬅️ **Previous:** [Datatype Rule](datatype-rule.md)