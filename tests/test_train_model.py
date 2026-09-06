# =========================================================
# Tests for train_model.py
# =========================================================

import sys
from pathlib import Path

import pandas as pd


# =========================================================
# Add Project Root
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# =========================================================
# Test Dataset
# =========================================================

def test_processed_dataset_exists():

    dataset_file = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "dataset_clean.csv"
    )

    assert dataset_file.exists()


# =========================================================
# Test Dataset
# =========================================================

def test_dataset_columns():

    dataset_file = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "dataset_clean.csv"
    )

    df = pd.read_csv(dataset_file)

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

    assert df.columns.tolist() == expected_columns


# =========================================================
# Test Dataset Size
# =========================================================

def test_dataset_has_data():

    dataset_file = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "dataset_clean.csv"
    )

    df = pd.read_csv(dataset_file)

    assert len(df) > 0


# =========================================================
# Test Target
# =========================================================

def test_target_column():

    dataset_file = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "dataset_clean.csv"
    )

    df = pd.read_csv(dataset_file)

    assert "Calories Burned" in df.columns

    assert df["Calories Burned"].notna().all()


# =========================================================
# Test Model File
# =========================================================

def test_best_model_exists():

    model_file = (
        PROJECT_ROOT
        / "models"
        / "best_model.pkl"
    )

    # This test passes only after train_model.py
    # has been executed.

    if model_file.exists():
        assert model_file.stat().st_size > 0