# Contributing

> Thank you for your interest in contributing to QualityClean!

---

# Welcome

QualityClean is an open-source project built to make data cleaning fast, transparent, and easy for everyone.

Whether you've found a bug, have an idea for a new feature, or want to improve the documentation, your contributions are always appreciated.

There are many ways to contribute, including:

- Reporting bugs
- Suggesting new features
- Improving documentation
- Fixing bugs
- Writing tests
- Improving performance
- Refactoring code

Every contribution, no matter how small, helps improve the project.

---

# Before You Start

Before contributing, please:

- Search existing GitHub Issues.
- Check open Pull Requests.
- Read the project documentation.
- Ensure your idea hasn't already been discussed.

---

# Setting Up the Development Environment

## 1. Clone the Repository

```bash
git clone https://github.com/JustZeo/qualityclean.git

cd qualityclean
```

---

## 2. Create a Virtual Environment

Using uv:

```bash
uv venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
uv sync
```

This installs all project dependencies, including development tools.

---

# Running Tests

Run the complete test suite.

```bash
pytest
```

Run with coverage.

```bash
pytest --cov=qualityclean
```

All tests should pass before submitting a Pull Request.

---

# Project Structure

```text
qualityclean/
│
├── docs/
├── src/
│   └── qualityclean/
├── tests/
├── LICENSE
├── README.md
└── pyproject.toml
```

---

# Coding Guidelines

Please follow these guidelines when contributing.

- Write clear and readable code.
- Keep functions focused on one responsibility.
- Add tests for new functionality.
- Update documentation when necessary.
- Use descriptive variable names.
- Keep pull requests focused on a single feature or fix.

---

# Reporting Bugs

When reporting a bug, please include:

- Operating system
- Python version
- QualityClean version
- Steps to reproduce
- Expected behavior
- Actual behavior
- Full error message (if applicable)

Providing this information helps reproduce and resolve issues more quickly.

---

# Suggesting Features

Feature requests are welcome.

When opening a feature request, try to explain:

- The problem you're trying to solve.
- Your proposed solution.
- Why the feature would benefit other users.
- Any alternatives you've considered.

---

# Pull Request Checklist

Before opening a Pull Request, ensure that:

- Your code builds successfully.
- All tests pass.
- New functionality includes tests.
- Documentation has been updated.
- Code follows the project's style.
- Commits have meaningful messages.

---

# Documentation Contributions

Documentation improvements are always welcome.

Examples include:

- Fixing typos
- Improving explanations
- Adding examples
- Clarifying API behavior
- Expanding tutorials

Good documentation is just as valuable as good code.

---

# Code of Conduct

Please be respectful and constructive when interacting with the community.

We aim to create a welcoming environment for contributors of all experience levels.

---

# License

By contributing to QualityClean, you agree that your contributions will be licensed under the project's MIT License.

---

# Thank You

Thank you for helping improve QualityClean.

Every bug report, documentation improvement, and pull request helps make the project better for everyone.

We appreciate your time and effort.

---

## What's Next?

You've reached the end of the documentation.

If you're new to QualityClean, return to the documentation home to explore other guides.

➡️ **Documentation Home:** [Home](index.md)

⬅️ **Previous:** [Custom Pipeline](examples/custom-pipeline.md)