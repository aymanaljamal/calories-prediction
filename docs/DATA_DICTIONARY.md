# Data Dictionary

## Calories Prediction Dataset

This document describes the variables included in the Calories Prediction dataset.

---

# Dataset Overview

The dataset contains information about individuals and their running activities.

The target variable is:

```text
Calories Burned
```

The dataset contains:

```text
200 rows
10 columns
```

---

# Variables

| Column              | Data Type   | Role    | Description                                   |
| ------------------- | ----------- | ------- | --------------------------------------------- |
| Gender              | Categorical | Feature | Gender of the individual                      |
| Age                 | Numerical   | Feature | Age of the individual                         |
| Height(cm)          | Numerical   | Feature | Height measured in centimeters                |
| Weight(kg)          | Numerical   | Feature | Weight measured in kilograms                  |
| BMI                 | Numerical   | Feature | Body Mass Index                               |
| Running Time(min)   | Numerical   | Feature | Duration of the running activity in minutes   |
| Running Speed(km/h) | Numerical   | Feature | Running speed measured in kilometers per hour |
| Distance(km)        | Numerical   | Feature | Distance covered during the running activity  |
| Average Heart Rate  | Numerical   | Feature | Average heart rate during the activity        |
| Calories Burned     | Numerical   | Target  | Estimated calories burned during the activity |

---

# Feature Descriptions

## Gender

Represents the gender category of the individual.

Example values:

```text
Male
Female
```

This is a categorical feature and requires encoding before being used by most Machine Learning models.

---

## Age

Represents the age of the individual.

Unit:

```text
Years
```

Type:

```text
Numerical
```

---

## Height(cm)

Represents the individual's height.

Unit:

```text
Centimeters
```

Type:

```text
Numerical
```

---

## Weight(kg)

Represents the individual's body weight.

Unit:

```text
Kilograms
```

Type:

```text
Numerical
```

---

## BMI

BMI stands for Body Mass Index.

It is a numerical measurement related to body weight and height.

Type:

```text
Numerical
```

---

## Running Time(min)

Represents the duration of the running activity.

Unit:

```text
Minutes
```

Type:

```text
Numerical
```

---

## Running Speed(km/h)

Represents the running speed.

Unit:

```text
Kilometers per hour
```

Type:

```text
Numerical
```

---

## Distance(km)

Represents the distance covered during the running activity.

Unit:

```text
Kilometers
```

Type:

```text
Numerical
```

---

## Average Heart Rate

Represents the average heart rate recorded during the running activity.

Type:

```text
Numerical
```

---

# Target Variable

## Calories Burned

This is the target variable that the Machine Learning models attempt to predict.

Type:

```text
Numerical
```

Problem type:

```text
Regression
```

The model receives the available features and produces an estimated calories-burned value.

---

# Data Types Summary

## Numerical Features

```text
Age
Height(cm)
Weight(kg)
BMI
Running Time(min)
Running Speed(km/h)
Distance(km)
Average Heart Rate
Calories Burned
```

## Categorical Features

```text
Gender
```

---

# Data Quality

Initial dataset validation found:

```text
Rows:              200
Columns:           10
Missing Values:    0
Duplicate Rows:    0
```

The dataset therefore starts with no missing values or duplicate rows according to the initial validation.

---

# Machine Learning Usage

The preprocessing pipeline should:

1. Separate features from the target.
2. Encode categorical variables.
3. Scale numerical variables when required.
4. Split the dataset into training and testing sets.
5. Train regression models.
6. Evaluate model predictions.

---

# Important Note

The variables in this document describe the structure of the dataset.

Correlation does not imply causation, and Machine Learning predictions should not be interpreted as medical measurements.
