# =========================================================
# Data Analysis
# =========================================================

from src.imports import (
    pd,
)


# =========================================================
# BASIC DATASET INFORMATION
# =========================================================

def get_basic_info(df):
    """
    Return basic information about the dataset.
    """

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "total_values": df.size,
        "duplicate_rows": df.duplicated().sum(),
        "missing_values": df.isnull().sum().sum()
    }


# =========================================================
# MISSING VALUES
# =========================================================

def get_missing_values(df):
    """
    Return missing values for each column.
    """

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    return missing.sort_values(ascending=False)


# =========================================================
# DUPLICATES
# =========================================================

def get_duplicates(df):
    """
    Return the number of duplicated rows.
    """

    return df.duplicated().sum()


# =========================================================
# NUMERICAL COLUMNS
# =========================================================

def get_numerical_columns(df):
    """
    Return all numerical columns.
    """

    return df.select_dtypes(
        include="number"
    ).columns.tolist()


# =========================================================
# CATEGORICAL COLUMNS
# =========================================================

def get_categorical_columns(df):
    """
    Return all categorical columns.
    """

    return df.select_dtypes(
        include="object"
    ).columns.tolist()


# =========================================================
# STATISTICAL SUMMARY
# =========================================================

def get_statistics(df):
    """
    Return important statistical information
    for numerical columns.
    """

    numerical_columns = get_numerical_columns(df)

    statistics = pd.DataFrame(
        index=numerical_columns
    )

    statistics["count"] = (
        df[numerical_columns].count()
    )

    statistics["mean"] = (
        df[numerical_columns].mean()
    )

    statistics["median"] = (
        df[numerical_columns].median()
    )

    statistics["mode"] = (
        df[numerical_columns]
        .mode()
        .iloc[0]
    )

    statistics["min"] = (
        df[numerical_columns].min()
    )

    statistics["max"] = (
        df[numerical_columns].max()
    )

    statistics["range"] = (
        statistics["max"] -
        statistics["min"]
    )

    statistics["std"] = (
        df[numerical_columns].std()
    )

    statistics["variance"] = (
        df[numerical_columns].var()
    )

    statistics["Q1"] = (
        df[numerical_columns].quantile(0.25)
    )

    statistics["Q2"] = (
        df[numerical_columns].quantile(0.50)
    )

    statistics["Q3"] = (
        df[numerical_columns].quantile(0.75)
    )

    statistics["IQR"] = (
        statistics["Q3"] -
        statistics["Q1"]
    )

    statistics["90_percentile"] = (
        df[numerical_columns].quantile(0.90)
    )

    statistics["95_percentile"] = (
        df[numerical_columns].quantile(0.95)
    )

    statistics["99_percentile"] = (
        df[numerical_columns].quantile(0.99)
    )

    return statistics


# =========================================================
# UNIQUE VALUES
# =========================================================

def get_unique_values(df):
    """
    Return the number of unique values
    for every column.
    """

    return df.nunique().sort_values(
        ascending=False
    )


# =========================================================
# VALUE COUNTS
# =========================================================

def get_value_counts(df, column):
    """
    Return the frequency of each value
    in a specific column.
    """

    return df[column].value_counts()


# =========================================================
# CATEGORICAL SUMMARY
# =========================================================

def get_categorical_summary(df):
    """
    Return useful information about
    categorical columns.
    """

    categorical_columns = (
        get_categorical_columns(df)
    )

    summary = []

    for column in categorical_columns:

        summary.append({
            "column": column,
            "unique_values": df[column].nunique(),
            "most_common": df[column].mode().iloc[0],
            "most_common_count": (
                df[column]
                .value_counts()
                .iloc[0]
            )
        })

    return pd.DataFrame(summary)


# =========================================================
# CORRELATION
# =========================================================

def get_correlation(df):
    """
    Return the correlation matrix
    for numerical columns.
    """

    numerical_columns = (
        get_numerical_columns(df)
    )

    return df[numerical_columns].corr()


# =========================================================
# TARGET ANALYSIS
# =========================================================

def analyze_target(df, target_column):
    """
    Return important statistics
    for the target column.
    """

    if target_column not in df.columns:
        return None

    target = df[target_column]

    result = {
        "count": target.count(),
        "mean": target.mean(),
        "median": target.median(),
        "mode": target.mode().iloc[0],
        "min": target.min(),
        "max": target.max(),
        "range": target.max() - target.min(),
        "std": target.std(),
        "variance": target.var(),
        "Q1": target.quantile(0.25),
        "Q2": target.quantile(0.50),
        "Q3": target.quantile(0.75),
        "IQR": (
            target.quantile(0.75) -
            target.quantile(0.25)
        )
    }

    return pd.Series(result)


# =========================================================
# OUTLIERS
# =========================================================

def count_outliers(df, column):
    """
    Count possible outliers using
    the IQR method.
    """

    if column not in df.columns:
        return 0

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    return len(outliers)


# =========================================================
# OUTLIER SUMMARY
# =========================================================

def get_outlier_summary(df):
    """
    Return the number of outliers
    for every numerical column.
    """

    numerical_columns = (
        get_numerical_columns(df)
    )

    summary = {}

    for column in numerical_columns:
        summary[column] = count_outliers(
            df,
            column
        )

    return pd.Series(summary).sort_values(
        ascending=False
    )


# =========================================================
# COMPLETE ANALYSIS REPORT
# =========================================================

def generate_analysis_report(df):
    """
    Generate a complete analysis report.
    """

    report = {}

    report["basic_info"] = (
        get_basic_info(df)
    )

    report["missing_values"] = (
        get_missing_values(df)
    )

    report["duplicates"] = (
        get_duplicates(df)
    )

    report["numerical_columns"] = (
        get_numerical_columns(df)
    )

    report["categorical_columns"] = (
        get_categorical_columns(df)
    )

    report["statistics"] = (
        get_statistics(df)
    )

    report["unique_values"] = (
        get_unique_values(df)
    )

    report["categorical_summary"] = (
        get_categorical_summary(df)
    )

    report["correlation"] = (
        get_correlation(df)
    )

    report["outliers"] = (
        get_outlier_summary(df)
    )

    return report