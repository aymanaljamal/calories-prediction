# =========================================================
# Test - Model Evaluation
# =========================================================

import sys
from pathlib import Path

import pandas as pd


# =========================================================
# Project Root
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# =========================================================
# Dataset Path
# =========================================================

DATASET_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "dataset_clean.csv"
)


# =========================================================
# Test 1 - Dataset Exists
# =========================================================

def test_dataset_exists():

    assert DATASET_FILE.exists(), (
        f"Dataset not found: {DATASET_FILE}"
    )

    print("✓ Dataset exists")


# =========================================================
# Test 2 - Dataset Can Be Loaded
# =========================================================

def test_dataset_can_be_loaded():

    df = pd.read_csv(DATASET_FILE)

    assert len(df) > 0

    print("✓ Dataset loaded successfully")


# =========================================================
# Test 3 - Required Columns
# =========================================================

def test_required_columns():

    df = pd.read_csv(DATASET_FILE)

    required_columns = [
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

    for column in required_columns:
        assert column in df.columns, (
            f"Missing column: {column}"
        )

    print("✓ All required columns exist")


# =========================================================
# Test 4 - Target Has No Missing Values
# =========================================================

def test_target_values():

    df = pd.read_csv(DATASET_FILE)

    assert df["Calories Burned"].notna().all()

    print("✓ Target values are valid")


# =========================================================
# Test 5 - Gender Values
# =========================================================

def test_gender_values():

    df = pd.read_csv(DATASET_FILE)

    valid_values = {
        "Male",
        "Female"
    }

    assert set(df["Gender"]).issubset(
        valid_values
    )

    print("✓ Gender values are valid")


# =========================================================
# Test 6 - Numeric Columns
# =========================================================

def test_numeric_columns():

    df = pd.read_csv(DATASET_FILE)

    numeric_columns = [
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

    for column in numeric_columns:

        assert pd.api.types.is_numeric_dtype(
            df[column]
        ), f"{column} is not numeric"

    print("✓ Numeric columns are valid")


# =========================================================
# Run Tests
# =========================================================

if __name__ == "__main__":

    print("\n" + "=" * 60)
    print("             MODEL EVALUATION TESTS")
    print("=" * 60)

    tests = [
        test_dataset_exists,
        test_dataset_can_be_loaded,
        test_required_columns,
        test_target_values,
        test_gender_values,
        test_numeric_columns,
    ]

    passed = 0
    failed = 0

    for test in tests:

        try:
            test()
            passed += 1

        except Exception as error:

            failed += 1

            print(
                f"✗ {test.__name__} FAILED"
            )

            print(
                f"  Error: {error}"
            )

    print("\n" + "=" * 60)
    print("                     SUMMARY")
    print("=" * 60)

    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    if failed == 0:
        print("\n✓ All tests passed!")

    else:
        print("\n✗ Some tests failed.")