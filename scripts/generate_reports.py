from pathlib import Path
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FILE = PROJECT_ROOT / "data" / "processed" / "dataset_clean.csv"

REPORTS_DIR = PROJECT_ROOT / "reports"
METRICS_DIR = REPORTS_DIR / "metrics"
MATRICES_DIR = REPORTS_DIR / "matrices"
TABLES_DIR = REPORTS_DIR / "tables"


def create_directories():
    METRICS_DIR.mkdir(parents=True, exist_ok=True)
    MATRICES_DIR.mkdir(parents=True, exist_ok=True)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)


def load_data():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )

    df = pd.read_csv(DATA_FILE)

    print("Dataset loaded successfully.")
    print("Shape:", df.shape)

    return df


def generate_dataset_summary(df):
    summary = pd.DataFrame({
        "Metric": [
            "Number of Rows",
            "Number of Columns",
            "Missing Values",
            "Duplicate Rows",
        ],
        "Value": [
            len(df),
            len(df.columns),
            int(df.isnull().sum().sum()),
            int(df.duplicated().sum()),
        ],
    })

    summary.to_csv(
        TABLES_DIR / "dataset_summary.csv",
        index=False
    )

    print("Created: dataset_summary.csv")


def generate_descriptive_statistics(df):
    stats = df.describe().transpose()

    stats.to_csv(
        TABLES_DIR / "descriptive_statistics.csv"
    )

    print("Created: descriptive_statistics.csv")


def generate_correlation_matrix(df):
    numeric_df = df.select_dtypes(include=np.number)

    correlation = numeric_df.corr()

    correlation.to_csv(
        MATRICES_DIR / "correlation_matrix.csv"
    )

    print("Created: correlation_matrix.csv")


def generate_feature_matrix(df):
    feature_df = df.copy()

    if "Gender" in feature_df.columns:
        feature_df["Gender"] = feature_df["Gender"].map({
            "Male": 0,
            "Female": 1
        })

    feature_df.to_csv(
        MATRICES_DIR / "feature_matrix.csv",
        index=False
    )

    print("Created: feature_matrix.csv")


def generate_target_correlations(df):
    numeric_df = df.select_dtypes(include=np.number)

    target = "Calories Burned"

    correlations = (
        numeric_df.corr()[target]
        .drop(target)
        .sort_values(
            key=lambda x: x.abs(),
            ascending=False
        )
    )

    result = pd.DataFrame({
        "Feature": correlations.index,
        "Correlation": correlations.values,
        "Absolute Correlation": correlations.abs().values
    })

    result.to_csv(
        TABLES_DIR / "target_correlations.csv",
        index=False
    )

    print("Created: target_correlations.csv")


def train_and_evaluate_models(df):

    data = df.copy()

    data["Gender"] = data["Gender"].map({
        "Male": 0,
        "Female": 1
    })

    X = data.drop("Calories Burned", axis=1)
    y = data["Calories Burned"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    models = {
        "Linear Regression": LinearRegression(),

        "Decision Tree": DecisionTreeRegressor(
            random_state=42
        ),

        "Random Forest": RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ),
    }

    results = []

    for name, model in models.items():

        print(f"Training: {name}")

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        mae = mean_absolute_error(
            y_test,
            predictions
        )

        mse = mean_squared_error(
            y_test,
            predictions
        )

        rmse = np.sqrt(mse)

        r2 = r2_score(
            y_test,
            predictions
        )

        results.append({
            "Model": name,
            "MAE": mae,
            "MSE": mse,
            "RMSE": rmse,
            "R2": r2
        })

    return pd.DataFrame(results)


def generate_model_reports(df):

    results = train_and_evaluate_models(df)

    results.to_csv(
        METRICS_DIR / "model_metrics.csv",
        index=False
    )

    results.to_csv(
        TABLES_DIR / "model_comparison.csv",
        index=False
    )

    with open(
        METRICS_DIR / "model_metrics.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write("MODEL EVALUATION RESULTS\n")
        file.write("=" * 70 + "\n\n")

        for _, row in results.iterrows():

            file.write(
                f"Model: {row['Model']}\n"
            )

            file.write(
                f"MAE : {row['MAE']:.2f}\n"
            )

            file.write(
                f"MSE : {row['MSE']:.2f}\n"
            )

            file.write(
                f"RMSE: {row['RMSE']:.2f}\n"
            )

            file.write(
                f"R2  : {row['R2']:.4f}\n"
            )

            file.write("\n")

    best_row = results.loc[
        results["R2"].idxmax()
    ]

    with open(
        METRICS_DIR / "best_model.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write("BEST MODEL\n")
        file.write("=" * 40 + "\n\n")

        file.write(
            f"Model: {best_row['Model']}\n"
        )

        file.write(
            f"MAE: {best_row['MAE']:.2f}\n"
        )

        file.write(
            f"MSE: {best_row['MSE']:.2f}\n"
        )

        file.write(
            f"RMSE: {best_row['RMSE']:.2f}\n"
        )

        file.write(
            f"R2: {best_row['R2']:.4f}\n"
        )

    print("Created: model_metrics.csv")
    print("Created: model_metrics.txt")
    print("Created: best_model.txt")
    print("Created: model_comparison.csv")


def main():

    print("=" * 70)
    print("GENERATING PROJECT REPORTS")
    print("=" * 70)

    create_directories()

    df = load_data()

    generate_dataset_summary(df)

    generate_descriptive_statistics(df)

    generate_correlation_matrix(df)

    generate_feature_matrix(df)

    generate_target_correlations(df)

    generate_model_reports(df)

    print("\n" + "=" * 70)
    print("REPORT GENERATION COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    main()