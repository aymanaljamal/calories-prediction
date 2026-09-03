# =========================================================
# Data Cleaning Tests
# =========================================================

import sys
from pathlib import Path

import pandas as pd


# =========================================================
# Project Root
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(
    str(PROJECT_ROOT)
)


# =========================================================
# Imports
# =========================================================

from src.data_loader import (
    load_raw_data,
)

from src.data_cleaning import (
    remove_duplicates,
    handle_missing_values,
    standardize_column_names,
    clean_gender_values,
    convert_numerical_columns,
    remove_invalid_values,
    remove_impossible_values,
    clean_dataset,
    save_cleaned_data,
    get_cleaning_report,
    run_cleaning_pipeline,
)


# =========================================================
# Test Header
# =========================================================

print("\n" + "=" * 60)
print("DATA CLEANING TEST")
print("=" * 60)


# =========================================================
# Load Dataset
# =========================================================

print("\nLoading raw dataset...")

df = load_raw_data()

print("Raw dataset loaded successfully!")

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")


# =========================================================
# Test 1: Remove Duplicates
# =========================================================

print("\n" + "-" * 60)
print("TEST 1: Remove Duplicates")
print("-" * 60)

test_df = pd.DataFrame({
    "Name": ["A", "B", "A"],
    "Age": [20, 21, 20]
})

result = remove_duplicates(test_df)

assert len(result) == 2
assert result.duplicated().sum() == 0

print("Duplicate rows removed successfully!")


# =========================================================
# Test 2: Handle Missing Values
# =========================================================

print("\n" + "-" * 60)
print("TEST 2: Handle Missing Values")
print("-" * 60)

test_df = pd.DataFrame({
    "Age": [20, None, 30],
    "Weight": [70, 80, None],
    "Gender": ["Male", None, "Female"]
})

result = handle_missing_values(test_df)

assert result.isnull().sum().sum() == 0

print("Missing values handled successfully!")


# =========================================================
# Test 3: Standardize Column Names
# =========================================================

print("\n" + "-" * 60)
print("TEST 3: Standardize Column Names")
print("-" * 60)

test_df = pd.DataFrame({
    " Age ": [20],
    " Weight ": [70]
})

result = standardize_column_names(test_df)

assert "Age" in result.columns
assert "Weight" in result.columns

print("Column names standardized successfully!")


# =========================================================
# Test 4: Clean Gender Values
# =========================================================

print("\n" + "-" * 60)
print("TEST 4: Clean Gender Values")
print("-" * 60)

test_df = pd.DataFrame({
    "Gender": [
        " male ",
        "female",
        " MALE "
    ]
})

result = clean_gender_values(test_df)

assert result["Gender"].tolist() == [
    "Male",
    "Female",
    "Male"
]

print("Gender values cleaned successfully!")


# =========================================================
# Test 5: Convert Numerical Columns
# =========================================================

print("\n" + "-" * 60)
print("TEST 5: Convert Numerical Columns")
print("-" * 60)

test_df = pd.DataFrame({
    "Age": ["20", "25", "30"],
    "Weight(kg)": ["70", "75", "80"],
    "Calories Burned": ["200", "250", "300"]
})

result = convert_numerical_columns(test_df)

assert pd.api.types.is_numeric_dtype(
    result["Age"]
)

assert pd.api.types.is_numeric_dtype(
    result["Weight(kg)"]
)

assert pd.api.types.is_numeric_dtype(
    result["Calories Burned"]
)

print("Numerical columns converted successfully!")


# =========================================================
# Test 6: Remove Invalid Values
# =========================================================

print("\n" + "-" * 60)
print("TEST 6: Remove Invalid Values")
print("-" * 60)

test_df = pd.DataFrame({
    "Age": [20, -5, 30],
    "Weight(kg)": [70, 75, -10],
    "Calories Burned": [200, 250, 300]
})

result = remove_invalid_values(test_df)

assert len(result) == 1

print("Invalid negative values removed successfully!")


# =========================================================
# Test 7: Remove Impossible Values
# =========================================================

print("\n" + "-" * 60)
print("TEST 7: Remove Impossible Values")
print("-" * 60)

test_df = pd.DataFrame({
    "Age": [20, 0, 30],
    "Weight(kg)": [70, 75, 80],
    "Running Time(min)": [30, 0, 40],
    "Calories Burned": [200, 250, 300]
})

result = remove_impossible_values(test_df)

assert len(result) == 2

print("Impossible values removed successfully!")


# =========================================================
# Test 8: Clean Complete Dataset
# =========================================================

print("\n" + "-" * 60)
print("TEST 8: Clean Complete Dataset")
print("-" * 60)

cleaned_df = clean_dataset(df)

assert isinstance(
    cleaned_df,
    pd.DataFrame
)

assert len(cleaned_df.columns) == 10

assert "Calories Burned" in cleaned_df.columns

assert cleaned_df.isnull().sum().sum() == 0

assert cleaned_df.duplicated().sum() == 0

print("Complete dataset cleaning passed!")


# =========================================================
# Test 9: Dataset Row Count
# =========================================================

print("\n" + "-" * 60)
print("TEST 9: Dataset Row Count")
print("-" * 60)

assert len(df) == 200
assert len(cleaned_df) == 200

print("Dataset row count is correct!")
print(f"Original rows : {len(df)}")
print(f"Cleaned rows  : {len(cleaned_df)}")


# =========================================================
# Test 10: Cleaning Report
# =========================================================

print("\n" + "-" * 60)
print("TEST 10: Cleaning Report")
print("-" * 60)

report = get_cleaning_report(
    df,
    cleaned_df
)

assert isinstance(
    report,
    dict
)

assert report["original_rows"] == 200

assert report["cleaned_rows"] == 200

assert report["rows_removed"] == 0

assert report["missing_values_after"] == 0

assert report["duplicates_after"] == 0

print("Cleaning report generated successfully!")

print("\nCleaning Report:")

for key, value in report.items():

    print(
        f"{key}: {value}"
    )


# =========================================================
# Test 11: Save Cleaned Dataset
# =========================================================

print("\n" + "-" * 60)
print("TEST 11: Save Cleaned Dataset")
print("-" * 60)

processed_dir = (
    PROJECT_ROOT
    / "data"
    / "processed"
)

processed_dir.mkdir(
    parents=True,
    exist_ok=True
)

test_output_file = (
    processed_dir
    / "dataset_clean_test.csv"
)

save_cleaned_data(
    cleaned_df,
    test_output_file
)

assert test_output_file.exists()

saved_df = pd.read_csv(
    test_output_file
)

assert len(saved_df) == 200

assert len(saved_df.columns) == 10

print("Cleaned dataset saved successfully!")

# Remove test file
test_output_file.unlink()

print("Temporary test file removed.")


# =========================================================
# Test 12: Complete Cleaning Pipeline
# =========================================================

print("\n" + "-" * 60)
print("TEST 12: Complete Cleaning Pipeline")
print("-" * 60)

pipeline_output_file = (
    processed_dir
    / "dataset_clean_test.csv"
)

cleaned_pipeline_df, pipeline_report = (
    run_cleaning_pipeline(
        df,
        pipeline_output_file
    )
)

assert isinstance(
    cleaned_pipeline_df,
    pd.DataFrame
)

assert isinstance(
    pipeline_report,
    dict
)

assert pipeline_output_file.exists()

assert len(cleaned_pipeline_df) == 200

assert cleaned_pipeline_df.isnull().sum().sum() == 0

assert cleaned_pipeline_df.duplicated().sum() == 0

print("Complete cleaning pipeline passed!")

# Remove temporary file
pipeline_output_file.unlink()

print("Temporary pipeline file removed.")


# =========================================================
# Final Result
# =========================================================

print("\n" + "=" * 60)
print("DATA CLEANING TEST PASSED")
print("=" * 60)

print("\nAll data cleaning tests completed successfully!")

print("\nFinal Dataset:")
print(f"- Rows              : {len(cleaned_df)}")
print(f"- Columns           : {len(cleaned_df.columns)}")
print(
    f"- Missing Values    : "
    f"{cleaned_df.isnull().sum().sum()}"
)
print(
    f"- Duplicate Rows    : "
    f"{cleaned_df.duplicated().sum()}"
)

print("\n" + "=" * 60)