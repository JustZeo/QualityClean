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
- Handle missing values
- Remove duplicate rows
- Infer and convert datatypes
- Generate detailed cleaning reports

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

clean_df = result.data

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

### After

| name | age | city |
|------|----:|------|
| Alice | 23 | Delhi |
| Bob | 23 | Mumbai |

✔ Column names normalized

✔ Whitespace removed

✔ Missing values handled

✔ Duplicate rows removed

---

# Features

- Fast Polars-based processing
- Automatic cleaning pipeline
- Human-readable audit reports
- CSV and Parquet support
- Detailed execution statistics
- Rule-level timing information
- Pythonic API
- Lightweight with minimal dependencies

---

# Example Audit Report

```
QualityClean Report

Rows processed      : 50,000
Duplicates removed  : 1,243
Missing values fixed: 892
Whitespace trimmed  : 3,144
Execution time      : 0.18 s
```

---

# API

```python
qc.load(...)
qc.clean(...)
qc.audit(...)
qc.export(...)
```

Complete API documentation is available in the `/docs` directory.

---

# Project Structure

```
qualityclean/
│
├── src/
├── tests/
├── docs/
├── README.md
└── pyproject.toml
```

---

# Roadmap

- [x] Core cleaning engine
- [x] Built-in cleaning rules
- [x] Audit reporting
- [x] CSV & Parquet support
- [x] Comprehensive test suite
- [ ] Custom rule plugins
- [ ] Performance benchmarks
- [ ] Documentation website
- [ ] PyPI release

---

# Contributing

Contributions, bug reports, and feature requests are welcome.

Please open an issue or submit a pull request.

---

# License

Released under the MIT License.

---

<div align="center">

**Built with ❤️ using Polars**

</div>