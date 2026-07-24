# QualityClean Documentation

> Fast, automated data cleaning for Polars DataFrames.

Welcome to the official documentation for **QualityClean**.

QualityClean is a lightweight, Polars-native data cleaning library that automates common preprocessing tasks through a simple, predictable, and transparent API.

Whether you're preparing data for machine learning, analytics, or ETL pipelines, QualityClean helps you clean messy datasets in seconds while providing detailed audit reports for every operation.

---

# Why QualityClean?

Data cleaning is one of the most repetitive tasks in every data workflow.

Instead of writing the same preprocessing code for every project, QualityClean provides a consistent cleaning pipeline that handles common data quality issues automatically.

With a single function call, you can:

- Normalize column names
- Remove unnecessary whitespace
- Convert placeholder values to nulls
- Handle missing values
- Remove duplicate rows
- Infer better datatypes
- Generate detailed audit reports

---

# Features

- 🚀 Built on top of **Polars**
- ⚡ High-performance data cleaning
- 🧹 Automatic cleaning pipeline
- 📊 Human-readable audit reports
- 📂 CSV & Parquet support
- 🔍 Automatic datatype inference
- 📈 Execution statistics
- 🧪 Comprehensive test coverage
- 🐍 Pythonic API

---

# Quick Example

```python
import qualityclean as qc

df = qc.load("employees.csv")

result = qc.clean(df)

qc.audit(result)

qc.export(result, "cleaned.parquet")
```

That's all it takes.

QualityClean handles the cleaning process while keeping every transformation transparent through detailed audit reports.

---

# Documentation

The documentation is organized into several sections.

## 🚀 Getting Started

New to QualityClean?

Start here.

- Getting Started
- Installation
- Quick Start

These guides will take you from installation to cleaning your first dataset in just a few minutes.

---

## 📖 API Reference

Detailed documentation for every public function.

- `load()`
- `clean()`
- `audit()`
- `export()`

Learn about parameters, return values, examples, and best practices.

---

## 🧹 Cleaning Rules

Understand how the built-in cleaning pipeline works.

- Column Rule
- Whitespace Rule
- Empty Rule
- Datatype Rule
- Missing Rule
- Duplicate Rule

Each rule is documented individually with explanations and examples.

---

## 💻 Examples

Real-world workflows demonstrating how to use QualityClean.

Examples include:

- Cleaning CSV datasets
- Cleaning Parquet datasets
- Building custom pipelines

---

## 🤝 Contributing

Interested in contributing?

Read the Contributing Guide to learn how to set up the development environment, run tests, and submit pull requests.

---

# Design Philosophy

QualityClean is built around three simple principles.

## Simple

Most datasets should be cleanable with a single function call.

---

## Fast

Built on top of Polars to deliver excellent performance while maintaining a clean API.

---

## Transparent

Every cleaning operation is recorded in an audit report so you always know what changed.

---

# Project Structure

```
qualityclean/
│
├── src/
├── docs/
├── tests/
├── README.md
├── LICENSE
└── pyproject.toml
```

---

# Need Help?

If you discover a bug, have a feature request, or would like to contribute, please visit the project's GitHub repository.

Contributions are always welcome.

---

# Start Reading

If you're new to QualityClean, continue with the Getting Started guide.

➡️ **Next:** [Getting Started](getting-started.md)