# Whitespace Rule

> Remove unnecessary whitespace from string values while preserving the actual data.

---

# Overview

The **Whitespace Rule** removes unwanted leading and trailing whitespace from string values in your dataset.

Whitespace issues are common in real-world data due to manual entry, imports from spreadsheets, or inconsistent formatting. While often invisible, these extra spaces can cause duplicate values, incorrect filtering, failed joins, and inaccurate analysis.

The Whitespace Rule ensures that textual data is clean and consistently formatted.

---

# Why This Rule Exists

Consider the following values:

```text
Alice
 Alice
Alice
Alice
```

Although they appear similar, they are actually different strings.

Without trimming whitespace:

- Filtering may fail
- Grouping may create duplicate categories
- Joins may not match correctly
- Duplicate detection becomes inaccurate

Removing unnecessary whitespace improves data consistency.

---

# What Gets Cleaned?

The Whitespace Rule:

- Removes leading whitespace
- Removes trailing whitespace
- Preserves internal spacing
- Applies only to string columns

For example:

```text
"  Alice  "
```

becomes

```text
"Alice"
```

---

# Example

## Before

| name | city |
|------|------|
| `" Alice "` | `" Delhi "` |
| `"Bob"` | `" Mumbai"` |
| `" Charlie"` | `"Pune "` |

---

## After

| name | city |
|------|------|
| `"Alice"` | `"Delhi"` |
| `"Bob"` | `"Mumbai"` |
| `"Charlie"` | `"Pune"` |

---

# Example Code

```python
import qualityclean as qc

df = qc.load("employees.csv")

result = qc.clean(df)

print(result.data)
```

All unnecessary leading and trailing whitespace is automatically removed.

---

# What Does NOT Change?

The Whitespace Rule does **not** modify:

- Numeric columns
- Boolean columns
- Date columns
- Internal spaces within strings

Example:

```text
"New York"
```

remains

```text
"New York"
```

Only the outer whitespace is removed.

---

# Benefits

Cleaning whitespace helps:

- Improve duplicate detection
- Produce consistent filtering results
- Improve joins and merges
- Standardize user-entered data
- Reduce formatting inconsistencies

---

# Execution Order

The Whitespace Rule runs immediately after the Column Rule.

```
Column Rule
      ↓
Whitespace Rule
      ↓
Empty Rule
      ↓
Datatype Rule
      ↓
Missing Rule
      ↓
Duplicate Rule
```

Running this rule early ensures later cleaning steps operate on normalized string values.

---

# Performance

Whitespace trimming is performed only on string columns.

Non-string columns are skipped, reducing unnecessary processing.

---

# Notes

- Only string values are modified.
- Internal spaces are preserved.
- Column names are handled separately by the Column Rule.
- The original DataFrame remains unchanged.

---

# Best Practices

✅ Clean whitespace before checking for duplicates.

✅ Trim text before handling missing values.

✅ Keep user-entered text consistent.

✅ Always review the audit report to see how many values were trimmed.

---

# Related Rules

- Column Rule
- Empty Rule

---

## What's Next?

With unnecessary whitespace removed, the next step is identifying empty or placeholder values.

➡️ **Next:** [Empty Rule](empty-rule.md)

⬅️ **Previous:** [Column Rule](column-rule.md)