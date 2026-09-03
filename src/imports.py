# =========================================================
# Standard Library
# =========================================================

from pathlib import Path
import re


# =========================================================
# Data Analysis
# =========================================================

import numpy as np
import pandas as pd


# =========================================================
# Data Visualization
# =========================================================

import matplotlib

# Use a non-GUI backend.
# This allows us to save figures without opening windows.
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns


# =========================================================
# Machine Learning
# =========================================================

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import (
    StandardScaler,
    OneHotEncoder,
)

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline


# =========================================================
# Regression Models
# =========================================================

from sklearn.linear_model import LinearRegression

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
)


# =========================================================
# Model Evaluation
# =========================================================

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


# =========================================================
# Model Saving
# =========================================================

import joblib