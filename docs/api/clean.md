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
    df: pl.DataFrame,
    **kwargs,
) -> CleanResult
```

---

# Parameters

## `df`

The Polars DataFrame to clean.

```python
result = qc.clean(df)
```

## `**kwargs`

Every keyword argument is forwarded straight through to the six built-in rules, so you can tune the pipeline without touching individual rules directly.

| Keyword | Default | Used by | Description |
|---------|---------|---------|--------------|
| `normalize_names` | `True` | Column Rule | Lowercase, strip, and underscore-join column names. |
| `remove_empty_columns` | `False` | Column Rule | Drop columns that are entirely null. |
| `missing_placeholders` | built-in list (`"N/A"`, `"null"`, `"unknown"`, etc.) | Empty Rule | Custom list of string values to treat as missing and convert to null. |
| `confidence` | `0.80` | Datatype Rule | Minimum fraction of values that must successfully cast for a column's datatype to be converted. |
| `fill` | `False` | Missing Rule | If `False` (default), rows containing any null are dropped. If `True`, nulls are filled instead (median for numeric columns, mode for string/boolean columns, forward-fill for dates) — see the [Missing Rule](../rules/missing-rule.md). |

```python
result = qc.clean(
    df,
    fill=True,
    confidence=0.9,
    remove_empty_columns=True,
)
```

---

# Returns

Returns a `CleanResult` object.

The object contains two primary attributes.

| Attribute | Description |
|-----------|-------------|
| `df` | Cleaned Polars DataFrame |
| `report` | `Report` dataclass containing cleaning statistics and metadata |

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
clean_df = result.df
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

print(result.df)
print(result.report)
```

Typical structure:

```python
CleanResult(
    df=<Polars DataFrame>,
    report=Report(
        version="...",
        original_rows=...,
        final_rows=...,
        whitespace_fixed=...,
        duplicates_removed=...,
        ...
    ),
)
```

`report` is a `Report` dataclass instance, not a dictionary — access fields directly (`result.report.duplicates_removed`), or pass it to `qc.audit()` for a formatted view.

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

clean_df = result.df

qc.export(result, "cleaned.csv")
```

---

# Errors

## Invalid Input

```python
qc.clean("employees.csv")
```

`clean()` does not validate its input up front — passing anything other than a `pl.DataFrame` fails inside the first rule that touches it (typically `AttributeError: 'str' object has no attribute 'columns'` from the Column Rule). Call `qc.load()` first to get a proper DataFrame rather than relying on a clean error message here.

---

## Empty DataFrame

Cleaning an empty DataFrame (0 rows) runs without raising an exception and returns a `CleanResult` with `original_rows` / `final_rows` set to `0`.

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