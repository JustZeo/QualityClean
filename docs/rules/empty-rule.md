# Empty Rule

> Detect and standardize empty or placeholder values before handling missing data.

---

# Overview

The **Empty Rule** identifies values that represent missing information but are stored as text rather than actual null values.

Real-world datasets often use placeholders such as empty strings or `"N/A"` instead of proper missing values. These placeholders can interfere with filtering, aggregation, datatype inference, and machine learning workflows.

The Empty Rule converts these values into a consistent representation so they can be processed correctly in later cleaning steps.

---

# Why This Rule Exists

Consider the following dataset.

| name | department |
|------|------------|
| Alice | Sales |
| Bob | N/A |
| Charlie | Unknown |
| David | |

Although `"N/A"`, `"Unknown"`, and the empty string all indicate missing information, they are treated as ordinary text unless they are standardized.

This leads to:

- Incorrect statistics
- Failed missing value detection
- Inconsistent filtering
- Poor model performance

The Empty Rule solves this by replacing placeholder values with proper null values.

---

# What Gets Cleaned?

Depending on the configuration, the Empty Rule may detect values such as:

- Empty strings (`""`)
- Strings containing only whitespace
- `"N/A"`
- `"NA"`
- `"NULL"`
- `"None"`
- `"Unknown"`
- Other configured placeholder values

These values are replaced with `null`.

---

# Example

## Before

| name | department |
|------|------------|
| Alice | Sales |
| Bob | N/A |
| Charlie | Unknown |
| David | |

---

## After

| name | department |
|------|------------|
| Alice | Sales |
| Bob | null |
| Charlie | null |
| David | null |

---

# Example Code

```python
import qualityclean as qc

df = qc.load("employees.csv")

result = qc.clean(df)

print(result.df)
```

All recognized placeholder values are converted to null.

---

# Benefits

Standardizing missing values provides several advantages.

- Accurate missing value counts
- Better datatype inference
- More reliable statistical analysis
- Improved machine learning preprocessing
- Consistent downstream transformations

---

# Execution Order

The Empty Rule runs after whitespace has been removed.

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

Running after the Whitespace Rule ensures values like `"   "` become empty strings before being detected.

---

# Performance

The Empty Rule scans only applicable columns and performs lightweight value comparisons.

Its performance scales efficiently with dataset size.

---

# Notes

- Placeholder values are converted to `null`.
- Existing null values remain unchanged.
- Comparison is performed after whitespace trimming.
- The original DataFrame is never modified.

---

# Best Practices

✅ Standardize placeholder values before handling missing data.

✅ Keep placeholder values consistent across datasets.

✅ Review the audit report to see how many values were converted.

✅ Avoid mixing multiple placeholder conventions in the same dataset.

---

# Related Rules

- Whitespace Rule
- Missing Rule

---

## What's Next?

Now that placeholder values have been standardized, the next step is ensuring each column has the most appropriate datatype.

➡️ **Next:** [Datatype Rule](datatype-rule.md)

⬅️ **Previous:** [Whitespace Rule](whitespace-rule.md)