# Datatype Rule

> Infer and normalize column data types to improve consistency, performance, and analysis.

---

# Overview

The **Datatype Rule** analyzes each column and ensures that values are stored using the most appropriate Polars data type.

Datasets imported from CSV files often contain numeric values, dates, or booleans stored as plain text. This prevents numerical calculations, filtering, sorting, and aggregations from working correctly.

The Datatype Rule converts compatible columns into their appropriate types while preserving the original meaning of the data.

---

# Why This Rule Exists

Consider the following dataset.

| age | salary | active |
|-----|---------|---------|
| "24" | "50000" | "True" |
| "31" | "62000" | "False" |

Although these values represent numbers and booleans, they are stored as strings.

As a result:

- Mathematical operations fail
- Sorting is incorrect
- Aggregations become unreliable
- Machine learning pipelines require additional preprocessing

The Datatype Rule automatically converts these columns into more suitable data types.

---

# What Gets Cleaned?

Depending on the data, the Datatype Rule may convert string columns to:

- Integer (`Int64`)
- Float (`Float64`)
- Date
- Datetime

Only columns that can be safely converted are changed — a column is left as `String` if it doesn't confidently match any of the above.

!!! note "Boolean is not inferred"
    Values like `"True"` / `"False"` are **not** converted to a `Boolean` dtype by this rule — `Boolean` isn't one of the supported cast targets. Such columns remain strings unless you cast them yourself after `clean()`.

---

# Example

## Before

| age | salary | active |
|-----|---------|---------|
| "24" | "50000" | "True" |
| "31" | "62000" | "False" |

Data Types

```text
age       -> String
salary    -> String
active    -> String
```

---

## After

| age | salary | active |
|-----|---------|---------|
| 24 | 50000 | "True" |
| 31 | 62000 | "False" |

Data Types

```text
age       -> Int64
salary    -> Int64
active    -> String   # unchanged — Boolean isn't a supported cast target
```

---

# Example Code

```python
import qualityclean as qc

df = qc.load("employees.csv")

result = qc.clean(df)

print(result.df.dtypes)
```

The output will show the inferred Polars data types for each column.

---

# Benefits

Using appropriate data types provides several advantages.

- Faster computations
- Reduced memory usage
- Correct mathematical operations
- Better sorting and filtering
- Improved compatibility with analytics and machine learning libraries

---

# Execution Order

The Datatype Rule runs after placeholder values have been standardized.

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

Running after the Empty Rule ensures placeholder values have already been converted to `null`, making type inference more accurate.

---

# Performance

Datatype inference is performed once per column.

QualityClean analyzes column values and applies conversions only when they can be performed safely.

---

# Configuration

The conversion threshold is controlled by the `confidence` keyword passed to `qc.clean()` — the fraction of non-null values in a column that must successfully cast to a candidate type before the column is converted.

```python
result = qc.clean(df, confidence=0.9)  # stricter — fewer columns get converted
result = qc.clean(df, confidence=0.5)  # looser — more columns get converted
```

Default: `confidence=0.80` (80% of values must cast successfully).

---

# Notes

- Original values are preserved whenever possible.
- Columns that cannot be safely converted remain unchanged.
- Existing Polars data types are respected.
- The original DataFrame is never modified.

---

# Best Practices

✅ Store numbers as numeric types.

✅ Store dates using proper date or datetime types.

✅ Avoid mixing multiple data types within the same column.

✅ Review the audit report to see which columns were converted.

---

# Related Rules

- Empty Rule
- Missing Rule

---

## What's Next?

With datatypes normalized, the next step is handling missing values consistently across the dataset.

➡️ **Next:** [Missing Rule](missing-rule.md)

⬅️ **Previous:** [Empty Rule](empty-rule.md)