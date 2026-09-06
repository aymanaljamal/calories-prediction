# =========================================================
# Tests for preprocessing.py
# =========================================================

import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


import pandas as pd
import numpy as np

from src.preprocessing import (
    clean_column_names,
    convert_numeric_columns,
    clean_gender,
    remove_duplicates,
    handle_missing_values,
    remove_invalid_values,
    process_bmi,
    set_data_types,
    reorder_columns,
    preprocess_data,
)

# =========================================================
# Test Data
# =========================================================

def create_test_dataframe():
    return pd.DataFrame({
        "Gender": ["Male", "Female", "Male"],
        "Age": [25, 30, 35],
        "Height(cm)": [175, 165, 180],
        "Weight(kg)": [70, 60, 80],
        "BMI": [22.86, 22.04, 24.69],
        "Running Time(min)": [30, 40, 35],
        "Running Speed(km/h)": [10, 8, 12],
        "Distance(km)": [5, 5.33, 7],
        "Average Heart Rate": [140, 135, 150],
        "Calories Burned": [300, 350, 400],
    })


# =========================================================
# Test Column Names
# =========================================================

def test_clean_column_names():

    df = pd.DataFrame({
        " Age ": [20],
        " Weight(kg) ": [70],
    })

    result = clean_column_names(df)

    assert "Age" in result.columns
    assert "Weight(kg)" in result.columns


# =========================================================
# Test Numeric Conversion
# =========================================================

def test_convert_numeric_columns():

    df = create_test_dataframe()

    df["Age"] = ["25", "30", "invalid"]

    result = convert_numeric_columns(df)

    assert pd.api.types.is_numeric_dtype(
        result["Age"]
    )

    assert pd.isna(result.loc[2, "Age"])


# =========================================================
# Test Gender Cleaning
# =========================================================

def test_clean_gender():

    df = create_test_dataframe()

    df["Gender"] = [
        "male",
        " FEMALE ",
        "M",
    ]

    result = clean_gender(df)

    assert result.loc[0, "Gender"] == "Male"
    assert result.loc[1, "Gender"] == "Female"
    assert result.loc[2, "Gender"] == "Male"


# =========================================================
# Test Invalid Gender
# =========================================================

def test_invalid_gender():

    df = create_test_dataframe()

    df["Gender"] = [
        "Male",
        "Female",
        "Unknown",
    ]

    result = clean_gender(df)

    assert pd.isna(
        result.loc[2, "Gender"]
    )


# =========================================================
# Test Duplicate Removal
# =========================================================

def test_remove_duplicates():

    df = create_test_dataframe()

    duplicated_df = pd.concat(
        [df, df.iloc[[0]]],
        ignore_index=True,
    )

    result = remove_duplicates(
        duplicated_df
    )

    assert len(result) == len(df)
    assert result.duplicated().sum() == 0


# =========================================================
# Test Missing Values
# =========================================================

def test_handle_missing_values():

    df = create_test_dataframe()

    df.loc[0, "Age"] = np.nan
    df.loc[1, "Weight(kg)"] = np.nan
    df.loc[2, "Gender"] = pd.NA

    result = handle_missing_values(df)

    assert result["Age"].isna().sum() == 0
    assert result["Weight(kg)"].isna().sum() == 0
    assert result["Gender"].isna().sum() == 0


# =========================================================
# Test Missing Target
# =========================================================

def test_missing_target_is_removed():

    df = create_test_dataframe()

    df.loc[0, "Calories Burned"] = np.nan

    result = handle_missing_values(df)

    assert len(result) == len(df) - 1
    assert result["Calories Burned"].isna().sum() == 0


# =========================================================
# Test Invalid Values
# =========================================================

def test_remove_invalid_values():

    df = create_test_dataframe()

    df.loc[0, "Age"] = -10
    df.loc[1, "Weight(kg)"] = -50

    result = remove_invalid_values(df)

    assert len(result) == len(df) - 2

    assert (result["Age"] >= 0).all()
    assert (result["Weight(kg)"] >= 0).all()


# =========================================================
# Test BMI Calculation
# =========================================================

def test_process_bmi():

    df = create_test_dataframe()

    df.loc[0, "BMI"] = np.nan

    result = process_bmi(df)

    expected_bmi = (
        70 / (1.75 ** 2)
    )

    assert np.isclose(
        result.loc[0, "BMI"],
        expected_bmi,
    )


# =========================================================
# Test BMI Existing Values
# =========================================================

def test_existing_bmi_is_not_changed():

    df = create_test_dataframe()

    original_bmi = df.loc[0, "BMI"]

    result = process_bmi(df)

    assert result.loc[0, "BMI"] == original_bmi


# =========================================================
# Test Data Types
# =========================================================

def test_set_data_types():

    df = create_test_dataframe()

    result = set_data_types(df)

    for column in [
        "Age",
        "Height(cm)",
        "Weight(kg)",
        "BMI",
        "Running Time(min)",
        "Running Speed(km/h)",
        "Distance(km)",
        "Average Heart Rate",
        "Calories Burned",
    ]:
        assert pd.api.types.is_float_dtype(
            result[column]
        )

    assert result["Gender"].dtype == object


# =========================================================
# Test Column Order
# =========================================================

def test_reorder_columns():

    df = create_test_dataframe()

    # Shuffle columns
    df = df[
        list(reversed(df.columns))
    ]

    result = reorder_columns(df)

    expected_columns = [
        "Gender",
        "Age",
        "Height(cm)",
        "Weight(kg)",
        "BMI",
        "Running Time(min)",
        "Running Speed(km/h)",
        "Distance(km)",
        "Average Heart Rate",
        "Calories Burned",
    ]

    assert result.columns.tolist() == (
        expected_columns
    )


# =========================================================
# Test Complete Preprocessing Pipeline
# =========================================================

def test_preprocess_data():

    df = create_test_dataframe()

    result = preprocess_data(df)

    # No missing values
    assert result.isnull().sum().sum() == 0

    # No duplicated rows
    assert result.duplicated().sum() == 0

    # Correct number of columns
    assert result.shape[1] == 10

    # Gender values
    assert set(result["Gender"]).issubset({
        "Male",
        "Female",
    })

    # Numeric columns should contain valid values
    assert (result["Age"] >= 0).all()
    assert (result["Height(cm)"] >= 0).all()
    assert (result["Weight(kg)"] >= 0).all()
    assert (result["BMI"] >= 0).all()
    assert (result["Calories Burned"] >= 0).all()


# =========================================================
# Test Pipeline With Dirty Data
# =========================================================

def test_preprocess_dirty_data():

    df = create_test_dataframe()

    # Add dirty values
    df.loc[0, "Age"] = "25"
    df.loc[1, "Weight(kg)"] = "60"
    df.loc[2, "Gender"] = "M"

    # Add missing BMI
    df.loc[0, "BMI"] = np.nan

    result = preprocess_data(df)

    assert result.isnull().sum().sum() == 0

    assert result.loc[2, "Gender"] == "Male"

    assert pd.api.types.is_numeric_dtype(
        result["Age"]
    )

    assert pd.api.types.is_numeric_dtype(
        result["Weight(kg)"]
    )

    assert result.loc[0, "BMI"] > 0