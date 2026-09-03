# Model Card

# Calories Prediction Model

## 1. Model Overview

The Calories Prediction project uses Machine Learning regression models to estimate the number of calories burned during a running activity.

The system is designed for educational and experimental purposes.

---

# 2. Machine Learning Task

Task:

```text
Regression
```

Target:

```text
Calories Burned
```

The model receives information about the individual and the running activity and predicts a numerical calories-burned value.

---

# 3. Input Features

The model can use the following features:

```text
Gender
Age
Height(cm)
Weight(kg)
BMI
Running Time(min)
Running Speed(km/h)
Distance(km)
Average Heart Rate
```

---

# 4. Output

The model produces:

```text
Predicted Calories Burned
```

The prediction is a continuous numerical value.

---

# 5. Candidate Models

The project evaluates multiple regression algorithms:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

The final model should be selected according to the actual evaluation results.

---

# 6. Preprocessing

The preprocessing pipeline handles:

* Numerical features.
* Categorical features.
* Feature transformation.
* Encoding.
* Scaling where appropriate.

The fitted preprocessing object is stored in:

```text
models/preprocessor.pkl
```

---

# 7. Model Storage

The selected model is stored in:

```text
models/best_model.pkl
```

The model and preprocessor should always be used together when making predictions.

---

# 8. Evaluation Metrics

The following metrics are used:

## MAE

Mean Absolute Error measures the average absolute difference between actual and predicted values.

Lower is better.

## MSE

Mean Squared Error penalizes larger errors more strongly.

Lower is better.

## RMSE

Root Mean Squared Error represents the square root of MSE.

Lower is better.

## R²

R² measures how well the model explains variation in the target.

Higher values are generally better.

---

# 9. Dataset Size

The initial dataset contains:

```text
200 observations
10 columns
```

The relatively small dataset size should be considered when interpreting model performance.

---

# 10. Limitations

The model has several limitations:

* The dataset is relatively small.
* Model performance depends on the quality of the available data.
* Important physiological variables may not be included.
* Predictions may not generalize to all individuals.
* The model should not be used as a medical diagnostic system.

---

# 11. Intended Use

The model is intended for:

* Educational Machine Learning projects.
* Demonstrating regression workflows.
* Data Science experimentation.
* Learning model preprocessing and evaluation.
* Demonstrating prediction pipelines.

---

# 12. Out-of-Scope Use

The model should not be used for:

* Medical diagnosis.
* Clinical decision-making.
* Professional health assessment.
* Safety-critical decisions.
* Replacing professional medical or fitness advice.

---

# 13. Reproducibility

To reproduce the model:

```text
1. Load the original dataset.
2. Clean the dataset.
3. Perform preprocessing.
4. Split the data.
5. Train candidate models.
6. Evaluate the models.
7. Select the best-performing model.
8. Save the model.
9. Save the preprocessing pipeline.
10. Use both objects for prediction.
```

---

# 14. Future Improvements

Potential improvements include:

* More training data.
* Cross-validation.
* Hyperparameter optimization.
* Feature engineering.
* Additional algorithms.
* Better data collection.
* External validation.
* Error analysis.
* Model monitoring after deployment.

---

# 15. Disclaimer

This model is an educational Machine Learning system.

Predictions are estimates and should not be interpreted as exact physiological measurements.
