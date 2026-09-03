# Changelog

All notable changes to the Calories Prediction project are documented in this file.

The format is based on the principles of Semantic Versioning.

---

# [Unreleased]

## Added

* Machine Learning preprocessing workflow.
* Model training workflow.
* Model evaluation workflow.
* Prediction workflow.
* Additional Machine Learning tests.
* Additional reports and metrics.

## Planned

* Hyperparameter tuning.
* Cross-validation.
* Advanced feature engineering.
* Additional regression models.
* Model comparison reports.
* Prediction API.
* Web application.
* Mobile application.
* Cloud deployment.

---

# [0.1.0] - 2026-09-03

## Project Initialization

### Added

* Created the `calories-prediction` project.
* Created the main project directory structure.
* Added raw and processed data directories.
* Added source code directory.
* Added notebooks directory.
* Added reports directory.
* Added models directory.
* Added tests directory.

---

## Data Loading

### Added

* Added `src/data_loader.py`.
* Added raw dataset loading.
* Added processed dataset loading.
* Added dataset information utilities.
* Added dataset validation.

Initial dataset validation:

```text
Rows:              200
Columns:           10
Total Values:      2,000
Missing Values:    0
Duplicate Rows:    0
```

---

## Data Analysis

### Added

* Added `src/data_analysis.py`.
* Added basic dataset information.
* Added missing value analysis.
* Added duplicate analysis.
* Added numerical column detection.
* Added categorical column detection.
* Added descriptive statistics.
* Added unique value analysis.
* Added categorical summaries.
* Added correlation analysis.
* Added target analysis.
* Added IQR-based outlier detection.

---

## Data Cleaning

### Added

* Added `src/data_cleaning.py`.
* Added duplicate removal.
* Added missing value handling.
* Added column name standardization.
* Added Gender value cleaning.
* Added numerical type conversion.
* Added invalid value removal.
* Added impossible value filtering.
* Added cleaning report generation.
* Added processed dataset export.

The cleaning pipeline currently preserves all 200 observations because the initial dataset contains no missing values or duplicate rows and no rows were removed during validation.

---

## Data Visualization

### Added

* Added `src/visualization.py`.
* Added histogram generation.
* Added boxplot generation.
* Added scatter plots.
* Added regression plots.
* Added correlation heatmap.
* Added bar charts.
* Added line plots.
* Added pair plots.
* Added count plots.
* Added violin plots.
* Added KDE plots.
* Added target correlation visualization.
* Added calories-based visualizations.
* Added gender-based visualizations.

Generated figures are stored in:

```text
reports/figures/
```

---

## Notebooks

### Added

```text
01_1_data_exploration.ipynb
01_2_data_exploration.ipynb
01_3_data_visualization.ipynb
```

The notebooks cover:

* Dataset exploration.
* Data quality checks.
* Descriptive statistics.
* Target analysis.
* Correlation analysis.
* Outlier analysis.
* Data visualization.

---

## Testing

### Added

```text
test_imports.py
test_data_loader.py
test_data_analysis.py
test_data_cleaning.py
test_visualization.py
```

The tests verify:

* Library imports.
* Dataset loading.
* Dataset structure.
* Data analysis functions.
* Data cleaning functions.
* Visualization generation.

---

## Documentation

### Added

```text
README.md
PROJECT_DOCUMENTATION.md
CHANGELOG.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md
LICENSE
```

Additional documentation:

```text
docs/
├── DATA_DICTIONARY.md
└── MODEL_CARD.md
```

---

# Dataset Validation

Initial validation produced the following results:

```text
Dataset:
├── Rows              : 200
├── Columns           : 10
├── Total Values      : 2,000
├── Missing Values    : 0
└── Duplicate Rows    : 0
```

No IQR-based numerical outliers were detected during the initial dataset analysis.

---

# Future Releases

Future versions may include:

```text
0.2.0
```

Potential additions:

* Complete preprocessing pipeline.
* Multiple Machine Learning models.
* Model evaluation.
* Model comparison.
* Best model selection.
* Saved model artifacts.

Future versions may also include:

```text
0.3.0
```

Potential additions:

* Prediction pipeline.
* Prediction test cases.
* REST API.
* Application integration.

---

# Notes

The changelog will be updated whenever a significant feature, fix, refactor, documentation change, or Machine Learning experiment is added to the project.
