# =========================================================
# Train Model - Calories Prediction
# =========================================================

from src.imports import (
    Path,
    pd,
    joblib,
    train_test_split,
    LinearRegression,
    DecisionTreeRegressor,
    RandomForestRegressor,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from src.data_loader import load_processed_data


# =========================================================
# Project Paths
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODELS_DIR = PROJECT_ROOT / "models"

BEST_MODEL_FILE = MODELS_DIR / "best_model.pkl"


# =========================================================
# Load Dataset
# =========================================================

df = load_processed_data()

print("Dataset loaded successfully")
print("Shape:", df.shape)


# =========================================================
# Prepare Data
# =========================================================

df["Gender"] = df["Gender"].map({
    "Male": 0,
    "Female": 1
})

X = df.drop("Calories Burned", axis=1)

y = df["Calories Burned"]


# =========================================================
# Split Data
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================================================
# Models
# =========================================================

models = {
    "Linear Regression": LinearRegression(),

    "Decision Tree": DecisionTreeRegressor(
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
}


# =========================================================
# Train and Evaluate
# =========================================================

best_model = None
best_model_name = None
best_r2 = -float("inf")

for name, model in models.items():

    print("\nTraining:", name)

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

    r2 = r2_score(
        y_test,
        predictions
    )

    print("MAE :", round(mae, 2))
    print("MSE :", round(mse, 2))
    print("R2  :", round(r2, 2))

    if r2 > best_r2:
        best_r2 = r2
        best_model = model
        best_model_name = name


# =========================================================
# Save Best Model
# =========================================================

MODELS_DIR.mkdir(
    parents=True,
    exist_ok=True
)

joblib.dump(
    best_model,
    BEST_MODEL_FILE
)


# =========================================================
# Result
# =========================================================

print("\n" + "=" * 50)
print("BEST MODEL")
print("=" * 50)

print("Model:", best_model_name)
print("R2:", round(best_r2, 2))

print("\nModel saved to:")
print(BEST_MODEL_FILE)