# =========================================================
# Data Analysis Test
# =========================================================

import sys
from pathlib import Path


# =========================================================
# Add Project Root
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(
    str(PROJECT_ROOT)
)


# =========================================================
# Imports
# =========================================================

from src.data_loader import load_raw_data

from src.data_analysis import (
    get_basic_info,
    get_missing_values,
    get_duplicates,
    get_numerical_columns,
    get_categorical_columns,
    get_statistics,
    get_unique_values,
    get_value_counts,
    get_categorical_summary,
    get_correlation,
    analyze_target,
    count_outliers,
    get_outlier_summary,
    generate_analysis_report,
)


# =========================================================
# Load Dataset
# =========================================================

print("\n" + "=" * 60)
print("DATA ANALYSIS TEST")
print("=" * 60)

df = load_raw_data()

print("\nDataset loaded successfully!")

print(
    f"Rows    : {df.shape[0]}"
)

print(
    f"Columns : {df.shape[1]}"
)


# =========================================================
# 1. Basic Information
# =========================================================

print("\n" + "-" * 60)
print("1. BASIC INFORMATION")
print("-" * 60)

basic_info = get_basic_info(df)

print(basic_info)


# =========================================================
# 2. Missing Values
# =========================================================

print("\n" + "-" * 60)
print("2. MISSING VALUES")
print("-" * 60)

missing = get_missing_values(df)

print(missing)

print(
    f"Missing values: {df.isnull().sum().sum()}"
)


# =========================================================
# 3. Duplicates
# =========================================================

print("\n" + "-" * 60)
print("3. DUPLICATES")
print("-" * 60)

duplicates = get_duplicates(df)

print(
    f"Duplicate rows: {duplicates}"
)


# =========================================================
# 4. Numerical Columns
# =========================================================

print("\n" + "-" * 60)
print("4. NUMERICAL COLUMNS")
print("-" * 60)

numerical_columns = (
    get_numerical_columns(df)
)

print(
    f"Number of numerical columns: "
    f"{len(numerical_columns)}"
)

for column in numerical_columns:
    print(f"- {column}")


# =========================================================
# 5. Categorical Columns
# =========================================================

print("\n" + "-" * 60)
print("5. CATEGORICAL COLUMNS")
print("-" * 60)

categorical_columns = (
    get_categorical_columns(df)
)

print(
    f"Number of categorical columns: "
    f"{len(categorical_columns)}"
)

for column in categorical_columns:
    print(f"- {column}")


# =========================================================
# 6. Statistical Summary
# =========================================================

print("\n" + "-" * 60)
print("6. STATISTICAL SUMMARY")
print("-" * 60)

statistics = get_statistics(df)

print(
    statistics.to_string()
)


# =========================================================
# 7. Unique Values
# =========================================================

print("\n" + "-" * 60)
print("7. UNIQUE VALUES")
print("-" * 60)

unique_values = get_unique_values(df)

print(
    unique_values.to_string()
)


# =========================================================
# 8. Value Counts
# =========================================================

print("\n" + "-" * 60)
print("8. VALUE COUNTS")
print("-" * 60)

if "Gender" in df.columns:

    gender_counts = get_value_counts(
        df,
        "Gender"
    )

    print(
        gender_counts.to_string()
    )

else:

    print(
        "Gender column not found."
    )


# =========================================================
# 9. Categorical Summary
# =========================================================

print("\n" + "-" * 60)
print("9. CATEGORICAL SUMMARY")
print("-" * 60)

categorical_summary = (
    get_categorical_summary(df)
)

if categorical_summary.empty:

    print(
        "No categorical columns found."
    )

else:

    print(
        categorical_summary.to_string(
            index=False
        )
    )


# =========================================================
# 10. Correlation
# =========================================================

print("\n" + "-" * 60)
print("10. CORRELATION")
print("-" * 60)

correlation = get_correlation(df)

print(
    correlation.to_string()
)


# =========================================================
# 11. Target Analysis
# =========================================================

print("\n" + "-" * 60)
print("11. TARGET ANALYSIS")
print("-" * 60)

target_analysis = analyze_target(
    df,
    "Calories Burned"
)

print(
    target_analysis.to_string()
)


# =========================================================
# 12. Outliers
# =========================================================

print("\n" + "-" * 60)
print("12. OUTLIER ANALYSIS")
print("-" * 60)

outlier_summary = (
    get_outlier_summary(df)
)

print(
    outlier_summary.to_string()
)


# =========================================================
# 13. Complete Report
# =========================================================

print("\n" + "-" * 60)
print("13. COMPLETE ANALYSIS REPORT")
print("-" * 60)

report = generate_analysis_report(df)

print(
    f"Report sections: {len(report)}"
)

for section in report:

    print(
        f"- {section}"
    )


# =========================================================
# Assertions
# =========================================================

print("\n" + "-" * 60)
print("RUNNING CHECKS")
print("-" * 60)

assert basic_info["rows"] == 200

assert basic_info["columns"] == 10

assert basic_info["missing_values"] == 0

assert basic_info["duplicate_rows"] == 0

assert "Calories Burned" in df.columns

assert len(statistics) > 0

assert not correlation.empty

assert target_analysis is not None

assert len(report) > 0

print("All checks passed!")


# =========================================================
# Completed
# =========================================================

print("\n" + "=" * 60)
print("DATA ANALYSIS TEST PASSED")
print("=" * 60)