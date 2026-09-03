# 🔥 Calories Prediction — Project Documentation

## 1. Project Overview

**Calories Prediction** is a Machine Learning regression project designed to predict the number of calories burned during running activities.

The project follows a complete Machine Learning workflow:

```text
Raw Data
    ↓
Data Loading
    ↓
Data Cleaning
    ↓
Exploratory Data Analysis
    ↓
Data Visualization
    ↓
Data Preprocessing
    ↓
Model Training
    ↓
Model Evaluation
    ↓
Model Selection
    ↓
Prediction
```

The project is developed using Python and popular Data Science and Machine Learning libraries.

---

# 2. Problem Statement

Predicting calories burned during physical activity can be treated as a regression problem when the target is a continuous numerical value.

This project uses personal and running-related information to estimate:

```text
Calories Burned
```

The available input features include:

* Gender
* Age
* Height
* Weight
* BMI
* Running Time
* Running Speed
* Distance
* Average Heart Rate

---

# 3. Project Objectives

The main objectives are:

1. Load and understand the dataset.
2. Verify data quality.
3. Clean the dataset.
4. Perform exploratory data analysis.
5. Create meaningful visualizations.
6. Analyze feature relationships.
7. Analyze correlations.
8. Prepare data for Machine Learning.
9. Train multiple regression models.
10. Evaluate model performance.
11. Select the best model.
12. Save the trained model.
13. Build a reusable prediction workflow.

---

# 4. Dataset

The dataset contains:

```text
Rows:              200
Columns:           10
Total Values:      2,000
Missing Values:    0
Duplicate Rows:    0
```

## Dataset Features

| Feature             | Type        | Description           |
| ------------------- | ----------- | --------------------- |
| Gender              | Categorical | Gender category       |
| Age                 | Numerical   | Age of the person     |
| Height(cm)          | Numerical   | Height in centimeters |
| Weight(kg)          | Numerical   | Weight in kilograms   |
| BMI                 | Numerical   | Body Mass Index       |
| Running Time(min)   | Numerical   | Running duration      |
| Running Speed(km/h) | Numerical   | Running speed         |
| Distance(km)        | Numerical   | Running distance      |
| Average Heart Rate  | Numerical   | Average heart rate    |
| Calories Burned     | Numerical   | Target variable       |

---

# 5. Target Variable

The target variable is:

```text
Calories Burned
```

The project is a regression problem because the target represents a continuous numerical value.

---

# 6. Project Directory

```text
calories-prediction/
│
├── data/
│   ├── raw/
│   │   └── dataset.csv
│   │
│   └── processed/
│       └── dataset_clean.csv
│
├── models/
│   ├── best_model.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   ├── 01_1_data_exploration.ipynb
│   ├── 01_2_data_exploration.ipynb
│   ├── 01_3_data_visualization.ipynb
│   ├── 02_data_analysis.ipynb
│   └── 03_machine_learning.ipynb
│
├── reports/
│   ├── figures/
│   ├── models/
│   ├── metrics/
│   ├── matrices/
│   ├── tables/
│   ├── test_cases/
│   └── notebooks/
│
├── scripts/
│
├── src/
│   ├── __init__.py
│   ├── imports.py
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── data_analysis.py
│   ├── visualization.py
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── prediction.py
│
├── tests/
│   ├── test_imports.py
│   ├── test_data_loader.py
│   ├── test_data_analysis.py
│   ├── test_data_cleaning.py
│   └── test_visualization.py
│
├── .gitignore
├── README.md
├── PROJECT_DOCUMENTATION.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── LICENSE
```

---

# 7. Data Loading

The data loading functionality is implemented in:

```text
src/data_loader.py
```

The module provides functions for:

* Loading the raw dataset.
* Loading the processed dataset.
* Returning basic dataset information.

The original dataset is located at:

```text
data/raw/dataset.csv
```

The processed dataset is located at:

```text
data/processed/dataset_clean.csv
```

---

# 8. Data Cleaning

The data cleaning functionality is implemented in:

```text
src/data_cleaning.py
```

The cleaning pipeline performs:

* Column name standardization.
* Numerical type conversion.
* Gender value cleaning.
* Missing value handling.
* Duplicate removal.
* Invalid value removal.
* Impossible value removal.
* Index resetting.

The cleaned dataset is saved as:

```text
data/processed/dataset_clean.csv
```

---

# 9. Exploratory Data Analysis

Exploratory Data Analysis is performed to understand the structure and characteristics of the dataset.

The analysis includes:

* Dataset dimensions.
* Data types.
* Missing values.
* Duplicate rows.
* Numerical columns.
* Categorical columns.
* Unique values.
* Descriptive statistics.
* Target statistics.
* Correlation analysis.
* Outlier analysis.

The notebooks are:

```text
notebooks/01_1_data_exploration.ipynb
notebooks/01_2_data_exploration.ipynb
```

---

# 10. Data Visualization

The visualization module is:

```text
src/visualization.py
```

The visualization notebook is:

```text
notebooks/01_3_data_visualization.ipynb
```

The project generates:

* Histograms.
* Boxplots.
* Scatter plots.
* Regression plots.
* Correlation heatmaps.
* Bar charts.
* Line plots.
* Pair plots.
* Count plots.
* Violin plots.
* KDE plots.

All generated figures are stored in:

```text
reports/figures/
```

Each visualization should be:

1. Generated from the real dataset.
2. Saved as a PNG file.
3. Displayed inside the notebook.
4. Interpreted based on the actual data.

---

# 11. Data Preprocessing

The preprocessing stage prepares the cleaned dataset for Machine Learning.

The preprocessing workflow includes:

```text
Processed Dataset
      ↓
Feature Selection
      ↓
Target Selection
      ↓
Categorical Encoding
      ↓
Numerical Scaling
      ↓
Train/Test Split
      ↓
Preprocessing Pipeline
```

The preprocessing implementation is:

```text
src/preprocessing.py
```

The fitted preprocessing pipeline is saved as:

```text
models/preprocessor.pkl
```

---

# 12. Machine Learning Models

The project evaluates several regression algorithms.

## Linear Regression

Linear Regression provides a simple baseline model.

## Decision Tree Regressor

Decision Tree Regression can model non-linear relationships.

## Random Forest Regressor

Random Forest combines multiple decision trees to improve prediction performance.

## Gradient Boosting Regressor

Gradient Boosting builds models sequentially to improve prediction accuracy.

---

# 13. Model Evaluation

The models are evaluated using:

### MAE

```text
Mean Absolute Error
```

Lower values indicate smaller average prediction errors.

### MSE

```text
Mean Squared Error
```

Lower values indicate smaller squared prediction errors.

### RMSE

```text
Root Mean Squared Error
```

Lower values indicate better prediction performance.

### R² Score

```text
R² Score
```

Higher values generally indicate better explanatory performance.

---

# 14. Model Selection

The models will be compared using the actual evaluation results.

The best model should be selected based on measurable performance rather than assumptions.

The selected model is stored as:

```text
models/best_model.pkl
```

Model results can be stored under:

```text
reports/models/
reports/metrics/
```

---

# 15. Prediction Pipeline

The prediction process follows:

```text
User Input
    ↓
Preprocessor
    ↓
Transformed Features
    ↓
Trained Model
    ↓
Predicted Calories
```

The prediction implementation is:

```text
src/prediction.py
```

---

# 16. Testing

The project contains automated tests for important components.

```text
tests/
├── test_imports.py
├── test_data_loader.py
├── test_data_analysis.py
├── test_data_cleaning.py
└── test_visualization.py
```

The tests verify:

* Library imports.
* Dataset loading.
* Dataset analysis.
* Data cleaning.
* Visualization generation.

---

# 17. Reports

Generated project artifacts are organized under:

```text
reports/
```

Structure:

```text
reports/
├── figures/
├── models/
├── metrics/
├── matrices/
├── tables/
├── test_cases/
└── notebooks/
```

This structure keeps generated results organized and separate from source code.

---

# 18. Reproducibility

To reproduce the project:

```text
1. Clone the repository.
2. Create a virtual environment.
3. Install the required dependencies.
4. Place the dataset in data/raw/.
5. Run the data cleaning process.
6. Run the exploration notebooks.
7. Run the visualization notebook.
8. Run preprocessing.
9. Train the Machine Learning models.
10. Evaluate the models.
11. Save the best model.
12. Run predictions.
```

---

# 19. Limitations

The dataset contains only 200 observations.

Therefore, Machine Learning performance may be affected by:

* Dataset size.
* Feature availability.
* Data quality.
* Representativeness of the observations.
* Relationships present in the dataset.

The model should be considered an educational prediction system rather than a medical or physiological measurement system.

---

# 20. Future Improvements

Future improvements may include:

* Increasing the dataset size.
* Adding additional physiological features.
* Feature engineering.
* Hyperparameter tuning.
* Cross-validation.
* Additional regression algorithms.
* Ensemble methods.
* Better error analysis.
* REST API integration.
* Web application.
* Mobile application.
* Cloud deployment.

---

# 21. Conclusion

The Calories Prediction project demonstrates a structured Machine Learning workflow.

The project combines:

* Data loading.
* Data cleaning.
* Exploratory analysis.
* Data visualization.
* Preprocessing.
* Regression models.
* Model evaluation.
* Testing.
* Prediction.

The architecture is designed to remain modular and easy to extend.
