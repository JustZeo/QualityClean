# `export()`

> Save a cleaned dataset to disk in a supported file format.

---

# Overview

The `export()` function writes a cleaned dataset to a file. It accepts **either** a `CleanResult` (returned by `clean()`) **or** a plain `pl.DataFrame` directly — if you pass a `CleanResult`, its `.df` is unwrapped automatically.

Instead of manually accessing the cleaned DataFrame and calling Polars export functions, QualityClean provides a simple interface for saving cleaned data.

Currently, QualityClean supports exporting datasets as:

- CSV
- Parquet

---

# Function Signature

```python
qualityclean.export(
    data: pl.DataFrame | CleanResult,
    path: str | pathlib.Path,
) -> None
```

---

# Parameters

## `data`

Either the `CleanResult` object returned by `clean()`, or a `pl.DataFrame` directly (e.g. `result.df`, or any other DataFrame you've built yourself).

```python
result = qc.clean(df)

qc.export(result, "cleaned.parquet")       # CleanResult — unwrapped automatically
qc.export(result.df, "cleaned.parquet")    # plain DataFrame — also fine
```

---

## `path`

Destination path for the exported dataset.

The file extension determines the export format.

Examples:

```python
"employees.csv"
```

```python
"employees.parquet"
```

---

# Returns

Returns `None`.

The cleaned dataset is written to the specified file.

---

# Supported Formats

| Format | Supported |
|----------|-----------|
| CSV | ✅ |
| Parquet | ✅ |
| Excel | ❌ |
| JSON | ❌ |

---

# Export as CSV

```python
qc.export(
    result,
    "cleaned.csv",
)
```

Equivalently, with a plain DataFrame:

```python
qc.export(
    result.df,
    "cleaned.csv",
)
```

---

# Export as Parquet

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

qc.export(
    result,
    "cleaned.parquet",
)
```

---

# How Export Format Is Determined

QualityClean automatically detects the export format from the file extension.

Example:

```python
qc.export(result, "data.csv")
```

→ CSV

```python
qc.export(result, "data.parquet")
```

→ Parquet

No additional parameters are required.

---

# Errors

## Unsupported Extension

```python
qc.export(
    result,
    "clean.xlsx",
)
```

Raises:

```text
ValueError
```

because Excel export is not currently supported.

---

## Invalid Output Path

```python
qc.export(
    result,
    "",
)
```

Raises:

```text
ValueError
```

An empty path has no recognizable file extension, which `export()` treats the same as any unsupported extension.

---

# Best Practices

✅ Keep the original dataset unchanged.

✅ Save cleaned datasets with descriptive file names.

✅ Use Parquet for larger datasets when performance and storage efficiency are important.

✅ Save the audit report alongside the exported dataset for reproducibility.

---

# Typical Workflow

```python
import qualityclean as qc

df = qc.load("employees.csv")

result = qc.clean(df)

qc.audit(result)

qc.export(
    result,
    "cleaned.parquet",
)
```

This is the recommended workflow for most projects.

---

# Related Functions

- `load()`
- `clean()`
- `audit()`

---

## What's Next?

You've completed the core QualityClean workflow.

Next, explore the built-in cleaning rules to understand exactly how your data is processed.

➡️ **Next:** [Column Rule](../rules/column-rule.md)

⬅️ **Previous:** [audit()](audit.md)