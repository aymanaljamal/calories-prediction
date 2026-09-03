# =========================================================
# Data Loader Test
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

from src.data_loader import (
    RAW_DATA_FILE,
    PROCESSED_DATA_FILE,
    load_raw_data,
    get_dataset_info,
)


# =========================================================
# Start Test
# =========================================================

print("\n" + "=" * 60)
print("DATA LOADER TEST")
print("=" * 60)


# =========================================================
# Check Raw Dataset
# =========================================================

print("\nChecking raw dataset...")

print(
    f"Raw dataset path:\n{RAW_DATA_FILE}"
)

if not RAW_DATA_FILE.exists():

    raise FileNotFoundError(
        f"Raw dataset not found: {RAW_DATA_FILE}"
    )

print("Raw dataset exists!")


# =========================================================
# Load Dataset
# =========================================================

print("\nLoading dataset...")

df = load_raw_data()

print("Dataset loaded successfully!")


# =========================================================
# Dataset Information
# =========================================================

info = get_dataset_info(df)

print("\nDataset Information:")

for key, value in info.items():

    print(
        f"{key}: {value}"
    )


# =========================================================
# Basic Checks
# =========================================================

assert len(df) > 0

assert len(df.columns) > 0

assert "Calories Burned" in df.columns


# =========================================================
# Processed Dataset
# =========================================================

print("\nProcessed dataset path:")

print(PROCESSED_DATA_FILE)


# =========================================================
# Completed
# =========================================================

print("\n" + "=" * 60)
print("DATA LOADER TEST PASSED")
print("=" * 60)