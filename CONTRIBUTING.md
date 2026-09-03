# Contributing to Calories Prediction

Thank you for your interest in contributing to the Calories Prediction project.

This document explains how to set up the project, make changes, run tests, and submit contributions.

---

# 1. Getting Started

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd calories-prediction
```

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# 2. Project Structure

The main project structure is:

```text
calories-prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│
├── reports/
│
├── src/
│
├── tests/
│
├── README.md
├── PROJECT_DOCUMENTATION.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── LICENSE
```

---

# 3. Development Workflow

The recommended Git workflow is:

```text
main
  │
  └── develop
        │
        └── feature/your-feature
```

Create a feature branch from `develop`:

```bash
git checkout develop
git pull origin develop
git checkout -b feature/your-feature
```

After completing the work:

```bash
git add .
git commit -m "feat: describe your change"
git push origin feature/your-feature
```

Then create a Pull Request targeting the `develop` branch.

---

# 4. Branch Naming

Use descriptive branch names.

Examples:

```text
feature/add-preprocessing
feature/train-model
feature/add-visualizations
fix/data-cleaning
fix/model-loading
refactor/analysis-module
docs/update-readme
test/add-model-tests
```

Avoid unclear names such as:

```text
test
new
update
branch1
mybranch
```

---

# 5. Code Style

Code should be:

* Readable.
* Modular.
* Reusable.
* Maintainable.
* Easy to test.

Use descriptive names.

Good example:

```python
def calculate_target_correlation(df):
    ...
```

Avoid unclear names:

```python
def calc(x):
    ...
```

Reusable functions should include docstrings.

Example:

```python
def load_dataset(file_path):
    """
    Load a dataset from a CSV file.
    """

    return pd.read_csv(file_path)
```

---

# 6. Data Guidelines

Do not modify the original raw dataset directly.

Raw data belongs in:

```text
data/raw/
```

Processed data belongs in:

```text
data/processed/
```

The original dataset should remain unchanged so that the cleaning and preprocessing workflow can be reproduced.

---

# 7. Notebook Guidelines

When creating or modifying notebooks:

* Use clear section headings.
* Explain the purpose of each analysis.
* Use the real project dataset.
* Do not invent results.
* Keep code reproducible.
* Include useful interpretations.
* Avoid unnecessary duplicated code.
* Ensure the notebook can run from top to bottom.

The main notebooks include:

```text
01_1_data_exploration.ipynb
01_2_data_exploration.ipynb
01_3_data_visualization.ipynb
02_data_analysis.ipynb
03_machine_learning.ipynb
```

---

# 8. Visualization Guidelines

Generated visualizations should be stored in:

```text
reports/figures/
```

Use descriptive filenames.

Examples:

```text
calories_burned_distribution.png
correlation_heatmap.png
target_correlations.png
calories_by_gender.png
```

Visualizations should:

* Use actual project data.
* Have meaningful titles.
* Have labeled axes.
* Be readable.
* Be saved at an appropriate resolution.
* Include interpretations when used in notebooks or reports.

---

# 9. Testing

Every important change should be tested.

Run the existing tests:

```powershell
python tests\test_imports.py
python tests\test_data_loader.py
python tests\test_data_analysis.py
python tests\test_data_cleaning.py
python tests\test_visualization.py
```

If new functionality is added, add appropriate tests.

For example:

```text
tests/
├── test_imports.py
├── test_data_loader.py
├── test_data_analysis.py
├── test_data_cleaning.py
├── test_visualization.py
├── test_preprocessing.py
├── test_train_model.py
├── test_evaluate_model.py
└── test_prediction.py
```

---

# 10. Commit Messages

Use clear and descriptive commit messages.

Recommended format:

```text
type: description
```

Examples:

```text
feat: add preprocessing pipeline
```

```text
fix: correct missing value handling
```

```text
test: add data cleaning tests
```

```text
docs: update project documentation
```

```text
refactor: improve visualization utilities
```

Common types:

```text
feat
fix
test
docs
refactor
chore
```

---

# 11. Pull Requests

A Pull Request should contain:

* A clear title.
* A short description.
* The reason for the change.
* Relevant test results.
* Screenshots when visualization changes are involved.
* Any known limitations.

Before opening a Pull Request:

```text
[ ] Code is complete.
[ ] Tests pass.
[ ] Notebook runs correctly.
[ ] No unnecessary files were added.
[ ] No secrets were committed.
[ ] Documentation was updated when necessary.
[ ] Changes were reviewed locally.
```

---

# 12. Issues

When reporting an issue, provide:

* A clear title.
* A description of the problem.
* Steps to reproduce the problem.
* Expected behavior.
* Actual behavior.
* Error messages.
* Relevant environment information.

Example:

```text
Environment:
- Windows
- Python 3.x
- Project version: ...

Problem:
...

Steps to reproduce:
1. ...
2. ...
3. ...

Expected:
...

Actual:
...
```

---

# 13. Feature Requests

Feature requests should explain:

* What the feature does.
* Why it is useful.
* How it improves the project.
* Possible implementation ideas.
* Any potential limitations.

---

# 14. Documentation

Documentation improvements are welcome.

When modifying documentation:

* Keep information accurate.
* Use clear English.
* Keep formatting consistent.
* Update related documentation when necessary.
* Do not document functionality that does not exist yet as if it were already implemented.

---

# 15. Security

Never commit:

```text
Passwords
API keys
Access tokens
Private keys
Database credentials
JWT secrets
.env files
Private datasets
```

Security-related issues should be reported privately according to:

```text
SECURITY.md
```

---

# 16. Final Checklist

Before submitting a contribution:

```text
[ ] Feature or fix is complete.
[ ] Code is readable.
[ ] Functions are properly documented.
[ ] Tests were added or updated.
[ ] Existing tests pass.
[ ] Notebooks run correctly.
[ ] Visualizations are correct.
[ ] No secrets were committed.
[ ] Generated files are stored correctly.
[ ] Documentation is updated.
[ ] Commit message is descriptive.
[ ] Pull Request targets the correct branch.
```

---

# 17. Thank You

Thank you for contributing to Calories Prediction.

Every contribution, whether it is code, documentation, testing, analysis, or suggestions, helps improve the project.
