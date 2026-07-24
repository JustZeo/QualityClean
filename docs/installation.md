# Installation

> Install QualityClean and verify that everything is working correctly.

---

# Requirements

Before installing QualityClean, ensure your environment meets the following requirements.

- Python **3.11** or newer
- pip **or** uv
- Internet connection (for package installation)

You can verify your Python version by running:

```bash
python --version
```

---

# Install Using pip

Install the latest stable release from PyPI.

```bash
pip install qualityclean
```

After installation, verify that the package was installed successfully.

```python
import qualityclean as qc

print(qc.__version__)
```

---

# Install Using uv

If you're using **uv**, install QualityClean with:

```bash
uv add qualityclean
```

---

# Verify Your Installation

Create a new Python file.

```python
import qualityclean as qc

print(qc.__version__)
```

If the package is installed correctly, Python will print the installed version without any errors.

---

# Your First Test

Create a small DataFrame.

```python
import polars as pl
import qualityclean as qc

df = pl.DataFrame(
    {
        " Name ": [" Alice ", "Bob"],
        "Age": [23, None],
    }
)

result = qc.clean(df)

qc.audit(result)

print(result.data)
```

If everything works, your installation is complete.

---

# Upgrading QualityClean

Upgrade to the latest version.

Using pip:

```bash
pip install --upgrade qualityclean
```

Using uv:

```bash
uv add --upgrade qualityclean
```

---

# Uninstalling

Using pip:

```bash
pip uninstall qualityclean
```

Using uv:

```bash
uv remove qualityclean
```

---

# Troubleshooting

## ModuleNotFoundError

If you see:

```text
ModuleNotFoundError: No module named 'qualityclean'
```

Ensure the package is installed in the same Python environment that you're currently using.

You can verify your active Python interpreter with:

```bash
python --version
```

and reinstall the package if necessary.

---

## Python Version Not Supported

QualityClean requires **Python 3.11 or newer**.

Check your version:

```bash
python --version
```

If you're using an older version of Python, upgrade before installing QualityClean.

---

## Virtual Environments

Using a virtual environment is strongly recommended for all Python projects.

Example using uv:

```bash
uv venv

# Activate the virtual environment

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

Then install QualityClean.

---

# Best Practices

- Use virtual environments for every project.
- Keep QualityClean updated.
- Read the Quick Start guide before using the library in production projects.
- Use `uv` for faster dependency management if it fits your workflow.

---

# Need Help?

If installation fails, please open an issue on the project's GitHub repository and include:

- Your operating system
- Python version
- Installation command
- Full error message

This information helps reproduce and resolve issues more quickly.

---

## What's Next?

QualityClean is now installed and ready to use.

Continue with the Quick Start guide to clean your first dataset.

➡️ **Next:** [Quick Start](quickstart.md)

⬅️ **Previous:** [Getting Started](getting-started.md)