<div align="center">

# ✨ QualityClean

### Fast, automated data cleaning for Polars DataFrames.

Clean messy datasets with a single function call while generating detailed audit reports.

<!-- Badges (replace when available) -->

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Polars](https://img.shields.io/badge/Powered%20by-Polars-orange)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

## Why QualityClean?

Cleaning datasets is one of the most repetitive steps in every data science and machine learning workflow.

QualityClean automates common preprocessing tasks so you can focus on analysis instead of writing the same cleaning code over and over.

With a single function call, QualityClean can:

- Normalize column names
- Trim unnecessary whitespace
- Replace placeholder values with nulls
- Handle missing values (drop or fill)
- Remove duplicate rows
- Infer and convert datatypes
- Generate detailed cleaning reports (console, HTML, Markdown, JSON)

---

# Installation

```bash
pip install qualityclean
```

or

```bash
uv add qualityclean
```

---

# Quick Start

```python
import qualityclean as qc

df = qc.load("employees.csv")

result = qc.clean(df)

clean_df = result.df

qc.audit(result)

qc.export(result, "cleaned.parquet")
```

---

# Example

### Before

| Name | Age | City |
|------|----:|------|
| `" Alice "` | 23 | Delhi |
| `"Bob"` | NULL | Mumbai |
| `"Alice"` | 23 | Delhi |

### After — `qc.clean(df, fill=True)`

| name | age | city |
|------|----:|------|
| alice | 23 | delhi |
| bob | 23 | mumbai |

✔ Column names normalized

✔ Whitespace removed

✔ Missing age filled with the column median

✔ Duplicate row removed

> By **default** (`fill=False`), any row containing a null is dropped instead of filled — Bob's row would be removed rather than repaired. Pass `fill=True` to fill instead of drop. See [Configuration](#configuration) below.

---

# Configuration

`clean()` accepts keyword arguments that tune the six built-in rules:

```python
result = qc.clean(
    df,
    normalize_names=True,        # Column Rule: standardize column names
    remove_empty_columns=False,  # Column Rule: drop all-null columns
    missing_placeholders=None,   # Empty Rule: custom placeholder strings to treat as null
    confidence=0.80,             # Datatype Rule: min. cast success rate to convert a column
    fill=False,                  # Missing Rule: fill nulls instead of dropping their rows
)
```

Full details for each option live in the corresponding rule's page under `/docs/rules`.

---

# Features

- Fast Polars-based processing
- Automatic, configurable cleaning pipeline
- Human-readable audit reports (console, HTML, Markdown, JSON)
- CSV and Parquet support (load and export)
- Detailed execution statistics
- Rule-level timing information
- Pythonic API
- Lightweight with minimal dependencies

---

# Example Audit Report

```
QualityClean Report v0.1.0

Dataset Summary
  Original Rows: 50000    Final Rows: 48757
  Original Columns: 18    Final Columns: 18

Cleaning Summary
  Whitespace Fixed: 3144
  Placeholders Converted: 421
  Missing Values Dropped: 1243
  Duplicates Removed: 892

Execution Time: 0.18 s
```

`qc.audit(result)` prints a fuller version of this to the console by default — see `qc.audit(result, format="html", path="report.html")` for HTML/Markdown/JSON export.

---

# API

```python
qc.load(source)                       # -> pl.DataFrame
qc.clean(df, **kwargs)                # -> CleanResult(df, report)
qc.audit(result, format="print", path=None)
qc.export(result_or_df, path)
```

Complete API documentation is available in the `/docs` directory.

---

# Project Structure

```
qualityclean/
│
├── src/
├── docs/
├── README.md
└── pyproject.toml
```

---

# Roadmap

- [x] Core cleaning engine
- [x] Built-in cleaning rules
- [x] Audit reporting (print / HTML / Markdown / JSON)
- [x] CSV & Parquet support
- [x] Test suite
- [x] Custom rule plugins
- [ ] Performance benchmarks
- [x] Documentation website
- [x] PyPI release

---

# Contributing

Contributions, bug reports, and feature requests are welcome.

Please open an issue or submit a pull request. See `docs/contributing.md` for setup details.

---

# License

Released under the MIT License.

---

<div align="center">

**Built with ❤️ using Polars**

</div>
