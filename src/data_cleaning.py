# =========================================================
# Data Cleaning
# =========================================================

from src.imports import (
    pd,
)


# =========================================================
# Remove Duplicate Rows
# =========================================================

def remove_duplicates(df):
    """
    Remove duplicated rows from the dataset.
    """

    cleaned_df = df.drop_duplicates().copy()

    return cleaned_df


# =========================================================
# Handle Missing Values
# =========================================================

def handle_missing_values(df):
    """
    Handle missing values in the dataset.

    Numerical columns:
    Missing values are replaced with the median.

    Categorical columns:
    Missing values are replaced with the mode.
    """

    cleaned_df = df.copy()

    # Numerical columns
    numerical_columns = (
        cleaned_df
        .select_dtypes(include="number")
        .columns
    )

    for column in numerical_columns:

        if cleaned_df[column].isnull().any():

            cleaned_df[column] = (
                cleaned_df[column]
                .fillna(
                    cleaned_df[column].median()
                )
            )

    # Categorical columns
    categorical_columns = (
        cleaned_df
        .select_dtypes(include="object")
        .columns
    )

    for column in categorical_columns:

        if cleaned_df[column].isnull().any():

            mode = cleaned_df[column].mode()

            if not mode.empty:

                cleaned_df[column] = (
                    cleaned_df[column]
                    .fillna(mode.iloc[0])
                )

    return cleaned_df


# =========================================================
# Standardize Column Names
# =========================================================

def standardize_column_names(df):
    """
    Remove unnecessary spaces from column names.
    """

    cleaned_df = df.copy()

    cleaned_df.columns = (
        cleaned_df.columns
        .str.strip()
    )

    return cleaned_df


# =========================================================
# Clean Gender Values
# =========================================================

def clean_gender_values(df):
    """
    Clean values in the Gender column.
    """

    cleaned_df = df.copy()

    if "Gender" not in cleaned_df.columns:
        return cleaned_df

    cleaned_df["Gender"] = (
        cleaned_df["Gender"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    return cleaned_df


# =========================================================
# Convert Numerical Columns
# =========================================================

def convert_numerical_columns(df):
    """
    Convert numerical columns to numeric data types.
    """

    cleaned_df = df.copy()

    numerical_columns = [
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

    for column in numerical_columns:

        if column in cleaned_df.columns:

            cleaned_df[column] = pd.to_numeric(
                cleaned_df[column],
                errors="coerce"
            )

    return cleaned_df


# =========================================================
# Remove Invalid Values
# =========================================================

def remove_invalid_values(df):
    """
    Remove rows containing negative values
    in numerical measurement columns.
    """

    cleaned_df = df.copy()

    non_negative_columns = [
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

    for column in non_negative_columns:

        if column in cleaned_df.columns:

            cleaned_df = cleaned_df[
                cleaned_df[column] >= 0
            ]

    return cleaned_df


# =========================================================
# Remove Impossible Values
# =========================================================

def remove_impossible_values(df):
    """
    Remove clearly impossible values
    based on simple domain rules.
    """

    cleaned_df = df.copy()

    # Age
    if "Age" in cleaned_df.columns:

        cleaned_df = cleaned_df[
            cleaned_df["Age"] > 0
        ]

    # Height
    if "Height(cm)" in cleaned_df.columns:

        cleaned_df = cleaned_df[
            cleaned_df["Height(cm)"] > 0
        ]

    # Weight
    if "Weight(kg)" in cleaned_df.columns:

        cleaned_df = cleaned_df[
            cleaned_df["Weight(kg)"] > 0
        ]

    # BMI
    if "BMI" in cleaned_df.columns:

        cleaned_df = cleaned_df[
            cleaned_df["BMI"] > 0
        ]

    # Running Time
    if "Running Time(min)" in cleaned_df.columns:

        cleaned_df = cleaned_df[
            cleaned_df["Running Time(min)"] > 0
        ]

    # Running Speed
    if "Running Speed(km/h)" in cleaned_df.columns:

        cleaned_df = cleaned_df[
            cleaned_df["Running Speed(km/h)"] > 0
        ]

    # Distance
    if "Distance(km)" in cleaned_df.columns:

        cleaned_df = cleaned_df[
            cleaned_df["Distance(km)"] > 0
        ]

    # Average Heart Rate
    if "Average Heart Rate" in cleaned_df.columns:

        cleaned_df = cleaned_df[
            cleaned_df["Average Heart Rate"] > 0
        ]

    # Calories Burned
    if "Calories Burned" in cleaned_df.columns:

        cleaned_df = cleaned_df[
            cleaned_df["Calories Burned"] > 0
        ]

    return cleaned_df


# =========================================================
# Clean Dataset
# =========================================================

def clean_dataset(df):
    """
    Perform the complete data cleaning process.
    """

    cleaned_df = df.copy()

    # 1. Standardize column names
    cleaned_df = standardize_column_names(
        cleaned_df
    )

    # 2. Convert numerical columns
    cleaned_df = convert_numerical_columns(
        cleaned_df
    )

    # 3. Clean categorical values
    cleaned_df = clean_gender_values(
        cleaned_df
    )

    # 4. Handle missing values
    cleaned_df = handle_missing_values(
        cleaned_df
    )

    # 5. Remove duplicates
    cleaned_df = remove_duplicates(
        cleaned_df
    )

    # 6. Remove invalid values
    cleaned_df = remove_invalid_values(
        cleaned_df
    )

    # 7. Remove impossible values
    cleaned_df = remove_impossible_values(
        cleaned_df
    )

    # Reset index
    cleaned_df = cleaned_df.reset_index(
        drop=True
    )

    return cleaned_df


# =========================================================
# Save Cleaned Dataset
# =========================================================

def save_cleaned_data(
    df,
    output_path
):
    """
    Save the cleaned dataset to a CSV file.
    """

    output_path = str(output_path)

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"Cleaned dataset saved to: {output_path}"
    )


# =========================================================
# Cleaning Report
# =========================================================

def get_cleaning_report(
    original_df,
    cleaned_df
):
    """
    Return a summary of the cleaning process.
    """

    report = {
        "original_rows": len(original_df),

        "cleaned_rows": len(cleaned_df),

        "rows_removed": (
            len(original_df)
            - len(cleaned_df)
        ),

        "original_columns": (
            len(original_df.columns)
        ),

        "cleaned_columns": (
            len(cleaned_df.columns)
        ),

        "missing_values_before": int(
            original_df
            .isnull()
            .sum()
            .sum()
        ),

        "missing_values_after": int(
            cleaned_df
            .isnull()
            .sum()
            .sum()
        ),

        "duplicates_before": int(
            original_df
            .duplicated()
            .sum()
        ),

        "duplicates_after": int(
            cleaned_df
            .duplicated()
            .sum()
        ),
    }

    return report


# =========================================================
# Complete Cleaning Pipeline
# =========================================================

def run_cleaning_pipeline(
    df,
    output_path=None
):
    """
    Run the complete data cleaning pipeline.
    """

    cleaned_df = clean_dataset(df)

    report = get_cleaning_report(
        df,
        cleaned_df
    )

    if output_path is not None:

        save_cleaned_data(
            cleaned_df,
            output_path
        )

    return cleaned_df, report