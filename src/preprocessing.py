# =========================================================
# Data Preprocessing
# =========================================================

from src.imports import (
    Path,
    np,
    pd,
)

from src.data_loader import (
    load_raw_data,
    PROCESSED_DATA_DIR,
    PROCESSED_DATA_FILE,
)


# =========================================================
# Expected Columns
# =========================================================

NUMERIC_COLUMNS = [
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

CATEGORICAL_COLUMNS = [
    "Gender",
]

TARGET_COLUMN = "Calories Burned"


# =========================================================
# Column Validation
# =========================================================

def validate_columns(df: pd.DataFrame) -> None:
    """
    Validate that all required columns exist in the dataset.
    """

    required_columns = NUMERIC_COLUMNS + CATEGORICAL_COLUMNS

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            "Missing required columns: "
            + ", ".join(missing_columns)
        )


# =========================================================
# Clean Column Names
# =========================================================

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove unnecessary spaces from column names.
    """

    df = df.copy()

    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
    )

    return df


# =========================================================
# Convert Numeric Columns
# =========================================================

def convert_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert numeric columns to numeric data types.

    Invalid values are converted to NaN.
    """

    df = df.copy()

    for column in NUMERIC_COLUMNS:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce",
        )

    return df


# =========================================================
# Clean Gender
# =========================================================

def clean_gender(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize Gender values.
    """

    df = df.copy()

    df["Gender"] = (
        df["Gender"]
        .astype("string")
        .str.strip()
        .str.title()
    )

    gender_mapping = {
        "M": "Male",
        "F": "Female",
        "Man": "Male",
        "Woman": "Female",
    }

    df["Gender"] = df["Gender"].replace(
        gender_mapping
    )

    valid_genders = [
        "Male",
        "Female",
    ]

    df.loc[
        ~df["Gender"].isin(valid_genders),
        "Gender"
    ] = pd.NA

    return df


# =========================================================
# Remove Duplicates
# =========================================================

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicated rows.
    """

    df = df.copy()

    df = df.drop_duplicates()

    return df.reset_index(drop=True)


# =========================================================
# Handle Missing Values
# =========================================================

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values.

    Numeric feature columns are filled using their median.
    Gender is filled using its mode.

    Rows with a missing target value are removed because
    the target cannot be safely inferred.
    """

    df = df.copy()

    # Target cannot be missing
    df = df.dropna(
        subset=[TARGET_COLUMN]
    )

    # Numeric features
    numeric_features = [
        column
        for column in NUMERIC_COLUMNS
        if column != TARGET_COLUMN
    ]

    for column in numeric_features:

        if df[column].isna().any():

            median_value = df[column].median()

            df[column] = df[column].fillna(
                median_value
            )

    # Gender
    if df["Gender"].isna().any():

        mode = df["Gender"].mode()

        if not mode.empty:
            df["Gender"] = df["Gender"].fillna(
                mode.iloc[0]
            )

    return df.reset_index(drop=True)


# =========================================================
# Validate Physical Values
# =========================================================

def remove_invalid_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove physically invalid values.

    Values such as negative age, height, weight,
    distance, running time, heart rate, and calories
    are considered invalid.
    """

    df = df.copy()

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

        df = df[
            df[column] >= 0
        ]

    return df.reset_index(drop=True)


# =========================================================
# Validate BMI
# =========================================================

def process_bmi(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate BMI when it is missing.

    BMI = weight / height^2

    Height is converted from centimeters to meters.
    """

    df = df.copy()

    valid_height = df["Height(cm)"] > 0

    calculated_bmi = pd.Series(
        np.nan,
        index=df.index,
        dtype=float,
    )

    calculated_bmi.loc[valid_height] = (
        df.loc[valid_height, "Weight(kg)"]
        /
        (
            (df.loc[valid_height, "Height(cm)"] / 100)
            ** 2
        )
    )

    df["BMI"] = df["BMI"].fillna(
        calculated_bmi
    )

    return df


# =========================================================
# Final Data Types
# =========================================================

def set_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Set final data types for the cleaned dataset.
    """

    df = df.copy()

    for column in NUMERIC_COLUMNS:
        df[column] = df[column].astype(float)

    df["Gender"] = df["Gender"].astype(str)

    return df


# =========================================================
# Reorder Columns
# =========================================================

def reorder_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keep the dataset columns in a consistent order.
    """

    columns = [
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

    return df[columns]


# =========================================================
# Main Preprocessing Pipeline
# =========================================================

def preprocess_data(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Run the complete preprocessing pipeline.
    """

    print("=" * 60)
    print("STARTING DATA PREPROCESSING")
    print("=" * 60)

    print(f"Original shape: {df.shape}")

    # 1. Clean column names
    df = clean_column_names(df)

    # 2. Validate columns
    validate_columns(df)

    # 3. Convert numeric columns
    df = convert_numeric_columns(df)

    # 4. Clean Gender
    df = clean_gender(df)

    # 5. Remove duplicate rows
    before = len(df)

    df = remove_duplicates(df)

    print(
        f"Duplicates removed: "
        f"{before - len(df)}"
    )

    # 6. Handle missing values
    df = handle_missing_values(df)

    # 7. Calculate missing BMI values
    df = process_bmi(df)

    # 8. Remove invalid values
    before = len(df)

    df = remove_invalid_values(df)

    print(
        f"Invalid rows removed: "
        f"{before - len(df)}"
    )

    # 9. Remove any rows that still have missing values
    df = df.dropna().reset_index(drop=True)

    # 10. Set final data types
    df = set_data_types(df)

    # 11. Reorder columns
    df = reorder_columns(df)

    print(f"Final shape: {df.shape}")

    print(
        f"Remaining missing values: "
        f"{df.isnull().sum().sum()}"
    )

    print("=" * 60)
    print("DATA PREPROCESSING COMPLETED")
    print("=" * 60)

    return df


# =========================================================
# Save Processed Dataset
# =========================================================

def save_processed_data(
    df: pd.DataFrame,
) -> None:
    """
    Save the processed dataset to data/processed/.
    """

    PROCESSED_DATA_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        PROCESSED_DATA_FILE,
        index=False,
    )

    print(
        f"\nProcessed dataset saved to:\n"
        f"{PROCESSED_DATA_FILE}"
    )


# =========================================================
# Complete Pipeline
# =========================================================

def run_preprocessing_pipeline() -> pd.DataFrame:
    """
    Load raw data, preprocess it, and save the
    processed dataset.
    """

    raw_data = load_raw_data()

    processed_data = preprocess_data(
        raw_data
    )

    save_processed_data(
        processed_data
    )

    return processed_data


# =========================================================
# Main
# =========================================================

if __name__ == "__main__":

    data = run_preprocessing_pipeline()

    print("\nFinal dataset:")
    print(data.head())

    print("\nData types:")
    print(data.dtypes)