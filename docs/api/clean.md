# `clean()`

> Automatically clean a dataset using QualityClean's built-in rule-based pipeline.

---

# Overview

The `clean()` function is the core of QualityClean.

It applies a sequence of predefined cleaning rules to a dataset and returns both the cleaned data and a detailed report describing every operation that was performed.

Instead of modifying the original DataFrame, `clean()` returns a `CleanResult` object containing the cleaned data and metadata about the cleaning process.

---

# Function Signature

```python
qualityclean.clean(
    data: pl.DataFrame,
) -> CleanResult
```

---

# Parameters

## `data`

The Polars DataFrame to clean.

```python
result = qc.clean(df)
```

---

# Returns

Returns a `CleanResult` object.

The object contains two primary attributes.

| Attribute | Description |
|-----------|-------------|
| `data` | Cleaned Polars DataFrame |
| `report` | Dictionary containing cleaning statistics and metadata |

---

# Cleaning Pipeline

The following rules are executed in order.

1. Column Rule
2. Whitespace Rule
3. Empty Rule
4. Datatype Rule
5. Missing Rule
6. Duplicate Rule

Each rule focuses on one specific task, making the pipeline predictable and easy to understand.

---

# Example

```python
import qualityclean as qc

df = qc.load("employees.csv")

result = qc.clean(df)
```

Access the cleaned DataFrame.

```python
clean_df = result.data
```

Access the report.

```python
report = result.report
```

---

# Understanding `CleanResult`

Example:

```python
result = qc.clean(df)

print(result.data)
print(result.report)
```

Typical structure:

```python
CleanResult(
    data=<Polars DataFrame>,
    report={
        ...
    }
)
```

---

# Example Workflow

```python
import qualityclean as qc

df = qc.load("employees.csv")

result = qc.clean(df)

qc.audit(result)

qc.export(result, "cleaned.parquet")
```

---

# What Gets Cleaned?

QualityClean automatically handles common data quality issues.

Examples include:

- Inconsistent column names
- Leading and trailing whitespace
- Placeholder values
- Missing values
- Duplicate rows
- Datatype normalization

---

# What Does NOT Change?

QualityClean never modifies:

- File names
- Folder structure
- Row order (unless duplicate removal requires it)
- User-created columns
- Original DataFrame object

The input DataFrame remains unchanged.

---

# Performance

QualityClean is built on top of Polars and is designed for efficient processing of both small and large datasets.

Performance depends on:

- Dataset size
- Number of columns
- Datatypes
- Hardware

---

# Common Usage Pattern

```python
df = qc.load("employees.csv")

result = qc.clean(df)

qc.audit(result)

clean_df = result.data

qc.export(result, "cleaned.csv")
```

---

# Errors

## Invalid Input

```python
qc.clean("employees.csv")
```

Raises:

```
TypeError
```

because the input must be a Polars DataFrame.

---

## Empty DataFrame

Cleaning an empty DataFrame returns an empty `CleanResult`.

No exception is raised.

---

# Best Practices

✅ Always inspect the audit report.

✅ Keep a copy of the original dataset.

✅ Export cleaned data instead of overwriting raw files.

✅ Use `load()` before calling `clean()`.

---

# Related Functions

- `load()`
- `audit()`
- `export()`

---

## What's Next?

Now that your dataset has been cleaned, learn how to generate detailed reports.

➡️ **Next:** [audit()](audit.md)

⬅️ **Previous:** [load()](load.md)