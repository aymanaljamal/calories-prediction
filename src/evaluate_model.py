# =========================================================
# Model Evaluation - Calories Prediction
# =========================================================

from src.imports import (
    pd,
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
# Load Dataset
# =========================================================

df = load_processed_data()

print("\n" + "=" * 70)
print("                 MODEL EVALUATION")
print("=" * 70)


# =========================================================
# Prepare Data
# =========================================================

# Convert Gender to numbers
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
# Evaluation
# =========================================================

results = []

best_model = None
best_model_name = None
best_r2 = float("-inf")


for name, model in models.items():

    # Train model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Metrics
    mae = mean_absolute_error(
        y_test,
        predictions
    )

    mse = mean_squared_error(
        y_test,
        predictions
    )

    rmse = mse ** 0.5

    r2 = r2_score(
        y_test,
        predictions
    )

    # Save results
    results.append({
        "Model": name,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2": r2
    })

    # Find best model
    if r2 > best_r2:

        best_r2 = r2
        best_model = model
        best_model_name = name


# =========================================================
# Results Table
# =========================================================

results_df = pd.DataFrame(results)


print("\n" + "-" * 70)
print("                    RESULTS")
print("-" * 70)

print(
    results_df.to_string(
        index=False,
        formatters={
            "MAE": "{:.2f}".format,
            "MSE": "{:.2f}".format,
            "RMSE": "{:.2f}".format,
            "R2": "{:.4f}".format,
        }
    )
)


# =========================================================
# Best Model
# =========================================================

print("\n" + "=" * 70)
print("                    BEST MODEL")
print("=" * 70)

print(f"Model : {best_model_name}")
print(f"R²    : {best_r2:.4f}")


# =========================================================
# Metric Explanation
# =========================================================

print("\n" + "=" * 70)
print("                 METRIC MEANING")
print("=" * 70)

print("MAE  : Lower is better")
print("MSE  : Lower is better")
print("RMSE : Lower is better")
print("R²   : Higher is better")


# =========================================================
# Main
# =========================================================

if __name__ == "__main__":
    print("\nEvaluation completed successfully.")