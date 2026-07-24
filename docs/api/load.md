# `load()`

> Load a dataset into a Polars DataFrame.

---

# Overview

The `load()` function reads a dataset from disk and returns a Polars DataFrame.

It provides a simple interface for loading supported file formats without requiring users to interact directly with Polars' file readers.

QualityClean currently supports:

- CSV
- Parquet

---

# Function Signature

```python
qualityclean.load(
    source: str | pathlib.Path | pl.DataFrame,
) -> pl.DataFrame
```

---

# Parameters

## `source`

The dataset to load.

Accepted types:

- `str`
- `pathlib.Path`
- `polars.DataFrame`

If a Polars DataFrame is provided, it is returned unchanged.

---

# Returns

Returns a `polars.DataFrame`.

```python
df = qc.load("employees.csv")
```

---

# Supported Formats

| Format | Supported |
|----------|-----------|
| CSV | ✅ |
| Parquet | ✅ |
| Excel | ❌ |
| JSON | ❌ |

---

# Examples

## Load a CSV File

```python
import qualityclean as qc

df = qc.load("employees.csv")
```

---

## Load a Parquet File

```python
import qualityclean as qc

df = qc.load("employees.parquet")
```

---

## Pass an Existing DataFrame

```python
import polars as pl
import qualityclean as qc

df = pl.DataFrame(
    {
        "name": ["Alice", "Bob"],
        "age": [22, 24],
    }
)

loaded = qc.load(df)
```

---

# Errors

The following situations raise exceptions.

## File Not Found

```python
qc.load("missing.csv")
```

Raises:

```
FileNotFoundError
```

---

## Unsupported File Format

```python
qc.load("employees.xlsx")
```

Raises:

```
ValueError
```

---

## Directory Instead of File

```python
qc.load("datasets/")
```

Raises:

```
IsADirectoryError
```

---

# Notes

- Loading a Polars DataFrame does **not** create a copy.
- CSV and Parquet files are loaded using Polars.
- Unsupported file extensions raise an exception.
- The returned DataFrame is ready for `qc.clean()`.

---

# Best Practices

✅ Store datasets in CSV or Parquet format.

✅ Validate file paths before loading large datasets.

✅ Use Parquet whenever possible for improved performance.

---

# Related Functions

- `clean()`
- `export()`

---

## What's Next?

Now that you know how to load data, learn how QualityClean cleans it.

➡️ **Next:** [clean()](clean.md)

⬅️ **Previous:** [Quick Start](../quickstart.md)