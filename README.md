# 🔥 Calories Prediction

A complete Machine Learning project for predicting calories burned during running activities based on personal characteristics and running-related features.

---

## 📌 Project Overview

The **Calories Prediction** project implements a complete Machine Learning workflow, starting from raw data and continuing through data exploration, data cleaning, visualization, data analysis, preprocessing, model training, model evaluation, feature importance analysis, and prediction.

The project is designed to demonstrate a practical and structured Machine Learning workflow using Python and Scikit-learn.

The complete workflow includes:

```text
Raw Dataset
     ↓
Data Exploration
     ↓
Data Cleaning
     ↓
Data Visualization
     ↓
Data Analysis
     ↓
Data Preprocessing
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Feature Importance Analysis
     ↓
Best Model Selection
     ↓
Model Saving
     ↓
Prediction
     ↓
Testing & Reporting
```

---

# 🎯 Objectives

The main objectives of this project are:

* Explore and understand the dataset.
* Analyze the quality of the data.
* Clean and prepare the dataset.
* Handle missing and invalid values.
* Remove duplicate records.
* Perform Exploratory Data Analysis (EDA).
* Create meaningful statistical visualizations.
* Analyze relationships between variables.
* Study correlations with the target variable.
* Prepare the dataset for Machine Learning.
* Encode categorical features.
* Apply appropriate preprocessing techniques.
* Train multiple regression models.
* Evaluate model performance.
* Compare different Machine Learning models.
* Select the best-performing model.
* Analyze feature importance / coefficients of the best model.
* Save the trained model.
* Save the preprocessing pipeline.
* Build a reusable prediction workflow.
* Test the project modules.
* Generate reports, tables, metrics, matrices, and notebook PDFs.

---

# 📊 Dataset

The dataset contains:

```text
Rows:              200
Columns:           10
Total Values:      2,000
Missing Values:    0
Duplicate Rows:    0
```

## Features

| Feature             | Description                       |
| ------------------- | --------------------------------- |
| Gender              | Gender category                   |
| Age                 | Age of the person                 |
| Height(cm)          | Height in centimeters             |
| Weight(kg)          | Weight in kilograms               |
| BMI                 | Body Mass Index                   |
| Running Time(min)   | Running duration in minutes       |
| Running Speed(km/h) | Running speed                     |
| Distance(km)        | Running distance                  |
| Average Heart Rate  | Average heart rate during running |
| Calories Burned     | Target variable                   |

## Target Variable

```text
Calories Burned
```

The project is formulated as a **regression problem** because the target variable is continuous.

---

# 🧹 Data Cleaning

The data cleaning process is implemented in:

```text
src/data_cleaning.py
```

The cleaning pipeline includes:

* Column name standardization.
* Numerical data type conversion.
* Gender value cleaning.
* Missing value handling.
* Duplicate removal.
* Invalid value removal.
* Impossible value filtering.
* Index resetting.
* Cleaned dataset export.

The cleaned dataset is stored in:

```text
data/processed/dataset_clean.csv
```

---

# 📈 Data Visualization

The visualization stage analyzes the dataset using statistical and graphical techniques.

All generated figures are stored in:

```text
reports/figures/
```

The visualization module is:

```text
src/visualization.py
```

The main visualization notebook is:

```text
notebooks/01_3_data_visualization.ipynb
```

The project includes visualizations for:

* Calories Burned distribution.
* Gender distribution.
* Calories Burned by Gender.
* Correlation heatmap.
* Target correlations.
* Calories vs Running Time.
* Calories vs Distance.
* Calories vs Average Heart Rate.
* Calories vs Weight.
* Calories vs Age.
* Running Time vs Distance.
* Running Speed vs Distance.
* Numerical feature boxplots.
* Calories distribution by gender.
* Calories KDE distribution.
* Pair plot.
* Feature importance / coefficient plot for the best model.

---

# 🔥 Calories Burned Distribution

The histogram shows the distribution of the target variable, **Calories Burned**.

![Calories Burned Distribution](./reports/figures/calories_burned_distribution.png)

---

# 👥 Gender Distribution

The following visualization shows the distribution of observations across gender categories.

![Gender Distribution](./reports/figures/countplot_Gender.png)

---

# 🔥 Calories Burned by Gender

This visualization compares the distribution of calories burned between gender categories.

![Calories Burned by Gender](./reports/figures/calories_by_gender.png)

---

# 📊 Correlation Heatmap

The correlation heatmap provides an overview of relationships between numerical variables.

![Correlation Heatmap](./reports/figures/correlation_heatmap.png)

---

# 🎯 Target Correlations

This visualization shows the correlation between numerical features and the target variable, **Calories Burned**.

![Target Correlations](./reports/figures/target_correlations.png)

---

# 🏃 Calories vs Running Time

This scatter plot shows the relationship between running duration and calories burned.

![Calories vs Running Time](./reports/figures/scatter_Running_Time\(min\)_vs_Calories_Burned.png)

---

# 📏 Calories vs Distance

This visualization shows the relationship between running distance and calories burned.

![Calories vs Distance](./reports/figures/scatter_Distance\(km\)_vs_Calories_Burned.png)

---

# ❤️ Calories vs Average Heart Rate

This visualization analyzes the relationship between average heart rate and calories burned.

![Calories vs Heart Rate](./reports/figures/scatter_Average_Heart_Rate_vs_Calories_Burned.png)

---

# ⚖️ Calories vs Weight

This scatter plot shows the relationship between body weight and calories burned.

![Calories vs Weight](./reports/figures/scatter_Weight\(kg\)_vs_Calories_Burned.png)

---

# 🎂 Calories vs Age

This visualization shows the relationship between age and calories burned.

![Calories vs Age](./reports/figures/scatter_Age_vs_Calories_Burned.png)

---

# 🏃 Running Time vs Distance

This visualization analyzes the relationship between running duration and distance.

![Running Time vs Distance](./reports/figures/scatter_Running_Time\(min\)_vs_Distance\(km\).png)

---

# ⚡ Running Speed vs Distance

This visualization analyzes the relationship between running speed and distance.

![Running Speed vs Distance](./reports/figures/scatter_Running_Speed\(km_h\)_vs_Distance\(km\).png)

---

# 📦 Numerical Feature Boxplots

Boxplots are used to understand numerical feature distributions and identify potential outliers.

![Age Boxplot](./reports/figures/boxplot_Age.png)

![Weight Boxplot](./reports/figures/boxplot_Weight\(kg\).png)

![Calories Boxplot](./reports/figures/boxplot_Calories_Burned.png)

---

# 🎻 Calories Distribution by Gender

The violin plot provides a detailed view of the distribution of calories burned across gender categories.

![Calories Violin Plot](./reports/figures/violin_calories_by_gender.png)

---

# 📈 Calories KDE Distribution

The KDE plot provides a smoothed representation of the probability density of calories burned.

![Calories KDE](./reports/figures/kde_Calories_Burned.png)

---

# 🔎 Pair Plot

The pair plot provides an overall view of relationships between numerical variables.

![Pair Plot](./reports/figures/pairplot.png)

---

# 🔬 Data Analysis

The data analysis stage is implemented in:

```text
src/data_analysis.py
```

The analysis includes:

* Descriptive statistics.
* Dataset structure analysis.
* Numerical feature analysis.
* Correlation analysis.
* Target variable analysis.
* Feature relationships.
* Distribution analysis.
* Outlier investigation.
* Running time and distance relationship.
* Running speed and distance relationship.
* BMI consistency analysis.

The analysis notebook is:

```text
notebooks/02_data_analysis.ipynb
```

Generated analysis results are stored in:

```text
reports/tables/
```

## Feature Correlation with Target

The correlation of each numerical feature with the target variable, **Calories Burned**, was computed and ranked by absolute correlation:

| Feature              | Correlation | Absolute Correlation |
| --------------------- | ----------: | --------------------: |
| Height(cm)            |    0.100808 |               0.100808 |
| Weight(kg)             |    0.070512 |               0.070512 |
| BMI                    |   -0.059128 |               0.059128 |
| Running Time(min)      |   -0.056699 |               0.056699 |
| Distance(km)           |   -0.051363 |               0.051363 |
| Age                    |    0.035348 |               0.035348 |
| Average Heart Rate     |    0.014701 |               0.014701 |
| Running Speed(km/h)    |    0.013207 |               0.013207 |

All correlations are weak (the strongest, Height(cm), is only ~0.10), which is consistent with the low R² achieved by the trained models and suggests that, in this dataset, no single feature has a strong linear relationship with Calories Burned.

---

# 🤖 Machine Learning

The Machine Learning stage is implemented and completed.

The main training module is:

```text
src/train_model.py
```

The evaluation module is:

```text
src/evaluate_model.py
```

The prediction module is:

```text
src/prediction.py
```

The Machine Learning task is a regression problem.

The implemented models are:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor

---

# ⚙️ Preprocessing

The preprocessing pipeline is implemented in:

```text
src/preprocessing.py
```

The preprocessing workflow includes:

1. Separating features and target.
2. Identifying numerical features.
3. Identifying categorical features.
4. Cleaning categorical values.
5. Encoding categorical variables.
6. Handling missing values.
7. Processing numerical features.
8. Applying scaling when appropriate.
9. Splitting data into training and testing sets.
10. Creating a reusable preprocessing pipeline.

The preprocessing pipeline is saved as:

```text
models/preprocessor.pkl
```

---

# 🧠 Model Training

The model training process compares several regression algorithms.

The models are trained using a consistent training/testing split.

The training process:

```text
Load Processed Dataset
        ↓
Prepare Features
        ↓
Prepare Target
        ↓
Preprocessing
        ↓
Train Models
        ↓
Generate Predictions
        ↓
Calculate Metrics
        ↓
Compare Models
        ↓
Select Best Model
        ↓
Save Best Model
```

The trained model is saved in:

```text
models/best_model.pkl
```

---

# 📊 Model Evaluation

The models are evaluated using:

* MAE
* MSE
* RMSE
* R²

## Evaluation Metrics

### MAE

Mean Absolute Error measures the average absolute difference between actual and predicted values.

```text
Lower is better.
```

### MSE

Mean Squared Error measures the average squared prediction error.

```text
Lower is better.
```

### RMSE

Root Mean Squared Error is the square root of MSE.

```text
Lower is better.
```

### R²

R² measures the proportion of target variance explained by the model.

```text
Higher is better.
```

---

# 🏆 Final Model Results

The final evaluation produced the following results:

| Model             |        MAE |          MSE |       RMSE |         R² |
| ----------------- | ---------: | -----------: | ---------: | ---------: |
| Linear Regression |     178.41 |     42871.96 |     207.06 |    -0.0185 |
| Decision Tree     |     273.70 |    113156.10 |     336.39 |    -1.6883 |
| Random Forest     | **167.92** | **38772.13** | **196.91** | **0.0789** |

## 🥇 Best Model

The best-performing model among the evaluated models is:

```text
Random Forest Regressor
```

with:

```text
MAE  = 167.92
MSE  = 38772.13
RMSE = 196.91
R²   = 0.0789
```

The trained best model is stored in:

```text
models/best_model.pkl
```

---

# 📌 Model Performance Interpretation

The Random Forest model achieved the best performance among the evaluated models.

An MAE of approximately:

```text
167.92 calories
```

means that the model's predictions differ from the actual calorie values by approximately 168 calories on average.

The RMSE is:

```text
196.91 calories
```

which indicates that larger prediction errors also exist in the dataset.

The R² value is:

```text
0.0789
```

This indicates that the current features explain only a relatively small portion of the variation in Calories Burned.

The result is retained as the actual model evaluation result and is not artificially modified.

The relatively weak predictive performance is likely related to the limited dataset size and the weak or inconsistent relationships between some activity measurements and the target variable — consistent with the weak feature correlations reported above.

---

# 🌟 Feature Importance Analysis

After selecting the best model, feature importance (for tree-based models) or coefficients (for linear models) are extracted and visualized to understand which features contribute most to the predictions.

The relevant snippet from the training/analysis notebook:

```python
if hasattr(train_model.best_model, "feature_importances_"):
    values = train_model.best_model.feature_importances_
    value_label = "Feature Importance"
elif hasattr(train_model.best_model, "coef_"):
    values = train_model.best_model.coef_
    value_label = "Coefficient"
else:
    values = None

if values is not None:
    importance = (
        pd.Series(values, index=train_model.X.columns)
        .sort_values()
    )

    plt.figure(figsize=(9, 6))
    plt.barh(importance.index, importance.values, color="#55A868")
    plt.title(f"{value_label} — {train_model.best_model_name}")
    plt.xlabel(value_label)
    plt.ylabel("Feature")
    plt.axvline(0, color="black", linewidth=0.8)
    plt.show()
else:
    print(f"{train_model.best_model_name} does not expose feature_importances_ or coef_.")
```

This logic automatically adapts to the type of the best-selected model:

* If the model exposes `feature_importances_` (e.g. Random Forest, Decision Tree), those values are plotted as **Feature Importance**.
* If the model exposes `coef_` instead (e.g. Linear Regression), those values are plotted as **Coefficient**.
* If neither attribute is available, a message is printed instead of failing.

The resulting horizontal bar chart ranks features by their contribution to the Random Forest model's predictions, and is stored alongside the other generated figures in `reports/figures/`.

---

# 🔮 Prediction

A reusable prediction workflow is implemented in:

```text
src/prediction.py
```

The prediction workflow loads:

```text
models/best_model.pkl
```

and:

```text
models/preprocessor.pkl
```

to generate predictions for new running activity records.

The prediction workflow follows:

```text
New User Data
      ↓
Data Validation
      ↓
Preprocessing
      ↓
Loaded Model
      ↓
Prediction
      ↓
Calories Burned
```

---

# 🧪 Testing

The project contains tests for the main modules:

```text
tests/

├── test_imports.py
├── test_data_loader.py
├── test_data_analysis.py
├── test_data_cleaning.py
└── test_visualization.py
```

The tests can be executed individually:

```powershell
python tests\test_imports.py
python tests\test_data_loader.py
python tests\test_data_analysis.py
python tests\test_data_cleaning.py
python tests\test_visualization.py
```

The testing results are stored in:

```text
reports/test_cases/
```

---

# 📓 Jupyter Notebooks

The project contains the following notebooks:

```text
notebooks/

├── 01_1_data_exploration.ipynb
├── 01_2_data_exploration.ipynb
├── 01_3_data_visualization.ipynb
├── 02_data_analysis.ipynb
└── 03_machine_learning.ipynb
```

## Recommended Execution Order

```text
01_1_data_exploration
        ↓
01_2_data_exploration
        ↓
01_3_data_visualization
        ↓
02_data_analysis
        ↓
03_machine_learning
```

PDF versions of the notebooks are stored in:

```text
reports/notebooks/
```

---

# 📁 Reports

All project reports are organized inside the `reports` directory.

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

## Figures

Location:

```text
reports/figures/
```

Contains all generated charts and visualizations, including the feature importance / coefficient plot.

## Metrics

Location:

```text
reports/metrics/
```

Contains model evaluation results such as:

```text
MAE
MSE
RMSE
R²
```

## Matrices

Location:

```text
reports/matrices/
```

Contains evaluation matrices and model-related matrix outputs.

## Tables

Location:

```text
reports/tables/
```

Contains statistical summaries, correlation tables (including the feature/target correlation table), analysis tables, and other generated tabular results.

## Test Cases

Location:

```text
reports/test_cases/
```

Contains testing documentation and test results.

## Notebook PDFs

Location:

```text
reports/notebooks/
```

Contains PDF versions of the project notebooks.

---

# 📂 Scripts

Project automation and utility scripts are stored in:

```text
C:\Users\ayman\OneDrive\Desktop\calories-prediction\scripts
```

The scripts directory is used for project-level execution and automation tasks.

---

# 📁 Complete Project Structure

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
│   │   ├── calories_burned_distribution.png
│   │   ├── countplot_Gender.png
│   │   ├── calories_by_gender.png
│   │   ├── correlation_heatmap.png
│   │   ├── target_correlations.png
│   │   ├── scatter_Running_Time(min)_vs_Calories_Burned.png
│   │   ├── scatter_Distance(km)_vs_Calories_Burned.png
│   │   ├── scatter_Average_Heart_Rate_vs_Calories_Burned.png
│   │   ├── scatter_Weight(kg)_vs_Calories_Burned.png
│   │   ├── scatter_Age_vs_Calories_Burned.png
│   │   ├── scatter_Running_Time(min)_vs_Distance(km).png
│   │   ├── scatter_Running_Speed(km_h)_vs_Distance(km).png
│   │   ├── boxplot_Age.png
│   │   ├── boxplot_Weight(kg).png
│   │   ├── boxplot_Calories_Burned.png
│   │   ├── violin_calories_by_gender.png
│   │   ├── kde_Calories_Burned.png
│   │   ├── pairplot.png
│   │   └── feature_importance.png
│   │
│   ├── models/
│   │
│   ├── metrics/
│   │
│   ├── matrices/
│   │
│   ├── tables/
│   │
│   ├── test_cases/
│   │
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
├── LICENSE
└── requirements.txt
```

---

# 🛠️ Technologies

The project was developed using:

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Jupyter Notebook

---

# 🚀 Installation

## 1. Create Virtual Environment

```bash
python -m venv venv
```

## 2. Activate Virtual Environment on Windows

```powershell
venv\Scripts\activate
```

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Run the preprocessing pipeline:

```powershell
python -m src.preprocessing
```

Run the model training:

```powershell
python -m src.train_model
```

Run model evaluation:

```powershell
python -m src.evaluate_model
```

Run the prediction workflow:

```powershell
python -m src.prediction
```

---

# 📊 Generated Outputs

The project generates and stores its outputs in organized directories:

```text
models/
reports/figures/
reports/metrics/
reports/matrices/
reports/tables/
reports/test_cases/
reports/notebooks/
```

This structure keeps the source code, datasets, trained models, visualizations, analysis results, and documentation separated and organized.

---

# ⚠️ Limitations

Although the complete Machine Learning workflow has been implemented, the dataset contains only 200 observations.

The final Random Forest model achieved:

```text
R² = 0.0789
```

Therefore, the current model has limited predictive power. This is further supported by the feature correlation analysis, where the strongest individual feature (Height(cm)) correlates with Calories Burned at only ~0.10.

The project demonstrates the complete Machine Learning workflow rather than providing a production-level calorie estimation system.

Potential improvements include:

* Increasing the dataset size.
* Collecting higher-quality real-world data.
* Adding additional physiological features.
* Improving feature engineering.
* Performing hyperparameter tuning.
* Using cross-validation.
* Investigating inconsistencies between activity measurements.
* Testing additional regression algorithms.

---

# ⚠️ Disclaimer

This project is intended for educational and Machine Learning demonstration purposes.

Calories burned are influenced by many physiological and activity-related factors. The predictions generated by this model should not be considered medical or physiological advice.

---

# 👨‍💻 Author

**Ayman Al-Jamal**

Computer Science Graduate

Junior Backend / Machine Learning Developer

---

# 📄 License

This project is distributed under the license included in the repository.
