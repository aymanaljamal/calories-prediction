# =========================================================
# Visualization Test
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

from src.visualization import (
    FIGURES_DIR,
    plot_histogram,
    plot_boxplot,
    plot_scatter,
    plot_regression,
    plot_correlation_heatmap,
    plot_bar_chart,
    plot_line,
    plot_pairplot,
    plot_countplot,
    plot_calories_distribution,
    plot_calories_vs_time,
    plot_calories_vs_distance,
    plot_calories_vs_heart_rate,
    plot_calories_vs_weight,
    plot_violin,
    plot_kde,
    plot_target_correlations,
    plot_calories_by_gender,
    plot_scatter_by_gender,
)


# =========================================================
# Load Dataset
# =========================================================

print("\n" + "=" * 60)
print("VISUALIZATION TEST")
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
# Numerical Columns
# =========================================================

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


# =========================================================
# 1. Histograms
# =========================================================

print("\n" + "-" * 60)
print("1. HISTOGRAMS")
print("-" * 60)

for column in numerical_columns:

    print(
        f"Creating histogram: {column}"
    )

    plot_histogram(
        df,
        column
    )


# =========================================================
# 2. Boxplots
# =========================================================

print("\n" + "-" * 60)
print("2. BOXPLOTS")
print("-" * 60)

for column in numerical_columns:

    print(
        f"Creating boxplot: {column}"
    )

    plot_boxplot(
        df,
        column
    )


# =========================================================
# 3. Violin Plots
# =========================================================

print("\n" + "-" * 60)
print("3. VIOLIN PLOTS")
print("-" * 60)

for column in numerical_columns:

    print(
        f"Creating violin plot: {column}"
    )

    plot_violin(
        df,
        column
    )


# =========================================================
# 4. KDE Plots
# =========================================================

print("\n" + "-" * 60)
print("4. KDE PLOTS")
print("-" * 60)

for column in numerical_columns:

    print(
        f"Creating KDE plot: {column}"
    )

    plot_kde(
        df,
        column
    )


# =========================================================
# 5. Correlation Heatmap
# =========================================================

print("\n" + "-" * 60)
print("5. CORRELATION HEATMAP")
print("-" * 60)

plot_correlation_heatmap(df)


# =========================================================
# 6. Calories Distribution
# =========================================================

print("\n" + "-" * 60)
print("6. CALORIES DISTRIBUTION")
print("-" * 60)

plot_calories_distribution(df)


# =========================================================
# 7. Calories Relationships
# =========================================================

print("\n" + "-" * 60)
print("7. CALORIES RELATIONSHIPS")
print("-" * 60)

plot_calories_vs_time(df)

plot_calories_vs_distance(df)

plot_calories_vs_heart_rate(df)

plot_calories_vs_weight(df)


# =========================================================
# 8. Regression Plots
# =========================================================

print("\n" + "-" * 60)
print("8. REGRESSION PLOTS")
print("-" * 60)

plot_regression(
    df,
    "Running Time(min)",
    "Calories Burned"
)

plot_regression(
    df,
    "Distance(km)",
    "Calories Burned"
)

plot_regression(
    df,
    "Average Heart Rate",
    "Calories Burned"
)

plot_regression(
    df,
    "Weight(kg)",
    "Calories Burned"
)


# =========================================================
# 9. Scatter Plots
# =========================================================

print("\n" + "-" * 60)
print("9. SCATTER PLOTS")
print("-" * 60)

plot_scatter(
    df,
    "Age",
    "Calories Burned"
)

plot_scatter(
    df,
    "BMI",
    "Calories Burned"
)

plot_scatter(
    df,
    "Running Speed(km/h)",
    "Calories Burned"
)


# =========================================================
# 10. Line Plot
# =========================================================

print("\n" + "-" * 60)
print("10. LINE PLOT")
print("-" * 60)

plot_line(
    df,
    "Running Time(min)",
    "Calories Burned"
)


# =========================================================
# 11. Pair Plot
# =========================================================

print("\n" + "-" * 60)
print("11. PAIR PLOT")
print("-" * 60)

plot_pairplot(df)


# =========================================================
# 12. Gender Visualizations
# =========================================================

if "Gender" in df.columns:

    print("\n" + "-" * 60)
    print("12. GENDER VISUALIZATIONS")
    print("-" * 60)

    plot_bar_chart(
        df,
        "Gender"
    )

    plot_countplot(
        df,
        "Gender"
    )

    plot_calories_by_gender(
        df
    )

    plot_scatter_by_gender(
        df,
        "Running Time(min)",
        "Calories Burned"
    )


# =========================================================
# 13. Target Correlations
# =========================================================

print("\n" + "-" * 60)
print("13. TARGET CORRELATIONS")
print("-" * 60)

plot_target_correlations(
    df,
    "Calories Burned"
)


# =========================================================
# Check Figures Folder
# =========================================================

print("\n" + "-" * 60)
print("CHECKING FIGURES")
print("-" * 60)

figure_files = list(
    FIGURES_DIR.glob("*.png")
)

print(
    f"Number of PNG files: "
    f"{len(figure_files)}"
)

assert len(figure_files) > 0


# =========================================================
# Completed
# =========================================================

print("\n" + "=" * 60)
print("VISUALIZATION TEST PASSED")
print("=" * 60)

print(
    f"\nFigures location:\n{FIGURES_DIR}"
)