# `export()`

> Save a cleaned dataset to disk in a supported file format.

---

# Overview

The `export()` function writes the cleaned dataset contained in a `CleanResult` object to a file.

Instead of manually accessing the cleaned DataFrame and calling Polars export functions, QualityClean provides a simple interface for saving cleaned data.

Currently, QualityClean supports exporting datasets as:

- CSV
- Parquet

---

# Function Signature

```python
qualityclean.export(
    result: CleanResult,
    path: str | pathlib.Path,
) -> None
```

---

# Parameters

## `result`

The `CleanResult` object returned by `clean()`.

```python
result = qc.clean(df)
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

## Invalid Result Object

```python
qc.export(df, "clean.csv")
```

Raises:

```text
TypeError
```

because `export()` expects a `CleanResult`.

---

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

because a valid destination path must be provided.

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