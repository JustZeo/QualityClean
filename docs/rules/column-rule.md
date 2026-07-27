# Column Rule

> Standardize column names to create a consistent and predictable dataset.

---

# Overview

The **Column Rule** is the first step in the QualityClean cleaning pipeline.

Its purpose is to normalize column names so they are easier to read, reference, and use in downstream code.

Many real-world datasets contain inconsistent naming conventions such as extra spaces, mixed capitalization, or special characters. This rule applies a consistent naming style before any other cleaning operations are performed.

---

# Why This Rule Exists

Datasets often contain column names like:

```text
Employee Name
Employee-Name
 employee_name
EMPLOYEE NAME
Employee.Name
```

Although these columns may represent the same information, inconsistent naming makes data analysis more difficult.

The Column Rule ensures that column names follow a predictable format throughout the dataset.

---

# What Gets Cleaned?

Depending on the configuration, the Column Rule may:

- Remove leading and trailing whitespace
- Normalize internal whitespace
- Convert column names to lowercase
- Replace spaces with underscores
- Remove unsupported characters
- Ensure consistent naming conventions

---

# Example

## Before

| Employee Name | Age | Department Name |
|---------------|-----|-----------------|
| Alice | 24 | Sales |

## After

| employee_name | age | department_name |
|---------------|-----|-----------------|
| Alice | 24 | Sales |

---

# Example Code

```python
import qualityclean as qc

df = qc.load("employees.csv")

result = qc.clean(df)

print(result.df.columns)
```

Output:

```python
[
    "employee_name",
    "age",
    "department_name",
]
```

---

# Benefits

Standardized column names provide several advantages.

- Easier attribute access
- Consistent code style
- Better compatibility with machine learning workflows
- Improved readability
- Fewer typing mistakes

---

# Execution Order

The Column Rule always runs **first**.

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

Running this rule first ensures that every subsequent cleaning step works with normalized column names.

---

# Configuration

Two keywords, passed to `qc.clean()`, control this rule:

| Keyword | Default | Description |
|---------|---------|--------------|
| `normalize_names` | `True` | Whether to lowercase, strip, and underscore-join column names at all. Set to `False` to leave column names untouched. |
| `remove_empty_columns` | `False` | If `True`, drops any column that is entirely null after loading. |

```python
result = qc.clean(df, normalize_names=False)
result = qc.clean(df, remove_empty_columns=True)
```

---

# Performance

Column normalization is performed once and scales efficiently with the number of columns rather than the number of rows.

For most datasets, the performance impact is negligible.

---

# Notes

- Only column names are modified.
- Cell values are **not** affected.
- The original input DataFrame remains unchanged.
- All later rules operate on the standardized column names.

---

# Best Practices

✅ Use descriptive column names.

✅ Avoid duplicate column names.

✅ Prefer lowercase names with underscores.

✅ Keep naming conventions consistent across datasets.

---

# Related Rules

- Whitespace Rule
- Empty Rule

---

## What's Next?

Now that column names are standardized, the next step is cleaning unnecessary whitespace from the dataset.

➡️ **Next:** [Whitespace Rule](whitespace-rule.md)

⬅️ **Previous:** [export()](../api/export.md)