# =========================================================
# Data Loader
# =========================================================

from src.imports import (
    Path,
    pd,
)


# =========================================================
# Project Paths
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"


# =========================================================
# Dataset Files
# =========================================================

RAW_DATA_FILE = RAW_DATA_DIR / "dataset.csv"

PROCESSED_DATA_FILE = (
    PROCESSED_DATA_DIR / "dataset_clean.csv"
)


# =========================================================
# Load Raw Dataset
# =========================================================

def load_raw_data() -> pd.DataFrame:
    """
    Load the original dataset from data/raw/.
    """

    if not RAW_DATA_FILE.exists():
        raise FileNotFoundError(
            f"Raw dataset not found: {RAW_DATA_FILE}"
        )

    return pd.read_csv(RAW_DATA_FILE)


# =========================================================
# Load Processed Dataset
# =========================================================

def load_processed_data() -> pd.DataFrame:
    """
    Load the cleaned dataset from data/processed/.
    """

    if not PROCESSED_DATA_FILE.exists():
        raise FileNotFoundError(
            f"Processed dataset not found: {PROCESSED_DATA_FILE}"
        )

    return pd.read_csv(PROCESSED_DATA_FILE)


# =========================================================
# Dataset Information
# =========================================================

def get_dataset_info(df: pd.DataFrame) -> dict:
    """
    Return basic information about the dataset.
    """

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "total_values": df.size,
        "column_names": df.columns.tolist(),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
    }


# =========================================================
# Main Test
# =========================================================

if __name__ == "__main__":

    data = load_raw_data()

    print("=" * 60)
    print("DATASET LOADED SUCCESSFULLY")
    print("=" * 60)

    print(f"Rows         : {data.shape[0]}")
    print(f"Columns      : {data.shape[1]}")
    print(f"Total Values : {data.size}")

    print("\nColumns:")

    for column in data.columns:
        print(f"- {column}")