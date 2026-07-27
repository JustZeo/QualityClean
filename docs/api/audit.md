# `audit()`

> Generate a detailed report of the cleaning process.

---

# Overview

The `audit()` function displays or exports a comprehensive report describing every operation performed during the cleaning process.

Instead of guessing what changed, QualityClean provides complete transparency by recording cleaning statistics, execution metadata, and rule summaries.

The audit report is generated from the `CleanResult` object returned by `clean()`.

---

# Function Signature

```python
qualityclean.audit(
    result: CleanResult,
    format: str = "print",
    path: str | pathlib.Path | None = None,
) -> None
```

---

# Parameters

## `result`

The `CleanResult` object returned by `clean()`.

```python
result = qc.clean(df)

qc.audit(result)
```

---

## `format`

Specifies how the report should be generated.

Supported values:

| Format | Description |
|----------|-------------|
| `"print"` | Display the report in the terminal |
| `"html"` | Export as an HTML file |
| `"markdown"` | Export as a Markdown file |
| `"json"` | Export as a JSON file |

Default:

```python
format="print"
```

---

## `path`

The destination file path when exporting a report.

Required for:

- HTML
- Markdown
- JSON

Not required for terminal output.

Example:

```python
qc.audit(
    result,
    format="html",
    path="report.html",
)
```

---

# Returns

Returns `None`.

The function either prints the report or writes it to disk.

---

# Display a Report

```python
qc.audit(result)
```

Example output:

```text
QualityClean Report
===================

Rows Processed        : 50,000
Columns Processed     : 18

Duplicate Rows Removed: 1,243
Missing Values Fixed  : 892
Whitespace Trimmed    : 3,144

Execution Time        : 0.18 s
```

---

# Export as HTML

```python
qc.audit(
    result,
    format="html",
    path="report.html",
)
```

---

# Export as Markdown

```python
qc.audit(
    result,
    format="markdown",
    path="report.md",
)
```

!!! warning "Known bug: Datatype Changes table"
    In the current version, the "Datatype Changes" table in the Markdown export renders the literal words `before` and `after` in every row instead of the actual old/new datatypes, due to how that table's rows are unpacked internally. The `print` and `html` formats are not affected. Until this is fixed, prefer `format="print"` or `format="json"` if you need accurate datatype-change details.

---

# Export as JSON

```python
qc.audit(
    result,
    format="json",
    path="report.json",
)
```

---

# What's Included?

Depending on the cleaning process, the report may include:

- Dataset information
- Number of rows processed
- Number of columns processed
- Cleaning rules executed
- Missing values handled
- Duplicate rows removed
- Whitespace corrections
- Datatype conversions
- Processing time
- Library version

---

# When Should You Use `audit()`?

It is recommended to generate an audit report after every cleaning operation.

Example workflow:

```python
df = qc.load("employees.csv")

result = qc.clean(df)

qc.audit(result)

qc.export(result, "cleaned.parquet")
```

---

# Errors

## Invalid Result Object

```python
qc.audit(df)
```

Raises:

```text
TypeError
```

because `audit()` expects a `CleanResult`.

---

## Missing Export Path

```python
qc.audit(
    result,
    format="html",
)
```

Raises:

```text
ValueError
```

because exporting requires a destination path.

---

## Unsupported Format

```python
qc.audit(
    result,
    format="xml",
)
```

Raises:

```text
ValueError
```

Supported formats are:

- print
- html
- markdown
- json

---

# Best Practices

✅ Always review the audit report after cleaning.

✅ Save HTML or Markdown reports for documentation.

✅ Use JSON reports for programmatic analysis.

✅ Archive reports alongside cleaned datasets for reproducibility.

---

# Related Functions

- `clean()`
- `export()`

---

## What's Next?

Now that you've reviewed your cleaning report, learn how to save the cleaned dataset.

➡️ **Next:** [export()](export.md)

⬅️ **Previous:** [clean()](clean.md)