# =========================================================
# Imports Test
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
# Import Project Imports
# =========================================================

try:

    from src.imports import (
        Path,
        re,
        np,
        pd,
        matplotlib,
        plt,
        sns,
        train_test_split,
        StandardScaler,
        OneHotEncoder,
        ColumnTransformer,
        Pipeline,
        LinearRegression,
        DecisionTreeRegressor,
        RandomForestRegressor,
        GradientBoostingRegressor,
        mean_absolute_error,
        mean_squared_error,
        r2_score,
        joblib,
    )

    print("\n" + "=" * 60)
    print("IMPORTS TEST")
    print("=" * 60)

    print("All imports loaded successfully!")

    print("\nLibraries:")
    print(f"- NumPy       : {np.__version__}")
    print(f"- Pandas      : {pd.__version__}")
    print(f"- Matplotlib  : {matplotlib.__version__}")
    print(f"- Seaborn     : {sns.__version__}")

    print("\nMatplotlib Backend:")
    print(f"- {matplotlib.get_backend()}")

    print("\n" + "=" * 60)
    print("IMPORTS TEST PASSED")
    print("=" * 60)


except Exception as error:

    print("\n" + "=" * 60)
    print("IMPORTS TEST FAILED")
    print("=" * 60)

    print(f"Error: {error}")

    raise