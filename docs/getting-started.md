# Getting Started

> Learn what QualityClean is, what problems it solves, and how to clean your first dataset.

---

# Overview

Welcome to **QualityClean**.

QualityClean is a lightweight, Polars-native data cleaning library that automates common preprocessing tasks through a simple and consistent API.

Instead of manually writing repetitive data cleaning code, QualityClean provides an intelligent cleaning pipeline that prepares your data while generating detailed audit reports.

Whether you're building machine learning models, performing exploratory data analysis, or creating ETL pipelines, QualityClean helps you spend less time cleaning and more time analyzing.

---

# Why QualityClean?

Real-world datasets are rarely perfect.

They often contain:

- Inconsistent column names
- Leading and trailing whitespace
- Placeholder values like `"N/A"` or `"Unknown"`
- Missing values
- Duplicate rows
- Incorrect datatypes

Cleaning these issues manually can become repetitive and error-prone.

QualityClean automates these common tasks through a predictable, rule-based cleaning pipeline.

---

# Who Is It For?

QualityClean is designed for:

- Data Scientists
- Machine Learning Engineers
- Data Analysts
- Python Developers
- ETL Engineers
- Students learning data preprocessing

If you work with tabular data, QualityClean can simplify your preprocessing workflow.

---

# Built-in Cleaning Pipeline

By default, QualityClean applies the following cleaning rules in order:

1. Column Rule
2. Whitespace Rule
3. Empty Rule
4. Datatype Rule
5. Missing Rule
6. Duplicate Rule

Each rule performs one specific task, making the cleaning process easy to understand and predictable.

---

# Your First Cleaning Job

```python
import qualityclean as qc

df = qc.load("employees.csv")

result = qc.clean(df)

qc.audit(result)

clean_df = result.data
```

In just a few lines of code, QualityClean:

- Loads your dataset
- Cleans it using the default pipeline
- Generates a detailed audit report
- Returns the cleaned DataFrame

---

# Understanding the Result

`qc.clean()` returns a `CleanResult` object.

```python
result = qc.clean(df)
```

The object contains two important attributes.

## Cleaned Data

```python
clean_df = result.data
```

Returns the cleaned Polars DataFrame.

---

## Cleaning Report

```python
report = result.report
```

Returns a dictionary containing:

- Cleaning statistics
- Rule execution timings
- Processing metadata
- Environment information
- Summary of performed operations

---

# Viewing the Audit Report

Print a human-readable report directly in the terminal.

```python
qc.audit(result)
```

You can also export the report.

```python
qc.audit(
    result,
    report_format="html",
    path="report.html",
)
```

Supported formats:

- Print
- HTML
- Markdown
- JSON

---

# Exporting Clean Data

Export the cleaned dataset using the built-in exporter.

```python
qc.export(
    result,
    "cleaned.parquet",
)
```

Supported formats:

- CSV
- Parquet

---

# Design Philosophy

QualityClean is built around three core principles.

## Simple

Most datasets should be cleanable with a single function call.

## Fast

Leverage the performance of Polars without adding unnecessary complexity.

## Transparent

Every cleaning operation is recorded in an audit report so you always know exactly what changed.

---

# Related Guides

After completing this guide, continue with:

- Installation
- Quick Start
- API Reference
- Cleaning Rules
- Examples

---

# Need Help?

If you encounter a bug, have a feature request, or would like to contribute, please visit the project's GitHub repository and open an issue.

Contributions are always welcome.

---

## What's Next?

Now that you understand what QualityClean is and how it works, the next step is installing it in your environment.

➡️ **Next:** [Installation](installation.md)

⬅️ **Previous:** [Documentation Home](index.md)