# =========================================================
# Data Visualization
# =========================================================

from src.imports import (
    Path,
    re,
    pd,
    matplotlib,
    plt,
    sns,
)


# =========================================================
# Project Paths
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

FIGURES_DIR = (
    PROJECT_ROOT /
    "reports" /
    "figures"
)

FIGURES_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# =========================================================
# General Plot Settings
# =========================================================

sns.set_style("whitegrid")


# =========================================================
# Safe File Name
# =========================================================

def clean_filename(text):
    """
    Make a text safe to use as a file name.
    """

    text = str(text)

    text = re.sub(
        r'[<>:"/\\|?*]',
        "_",
        text
    )

    text = text.replace(
        " ",
        "_"
    )

    return text


# =========================================================
# Save Figure
# =========================================================

def save_figure(filename):
    """
    Save the current figure inside
    reports/figures/.
    """

    file_path = FIGURES_DIR / filename

    plt.tight_layout()

    plt.savefig(
        file_path,
        dpi=300,
        bbox_inches="tight"
    )

    print(
        f"Figure saved: {file_path}"
    )


# =========================================================
# 1. Histogram
# =========================================================

def plot_histogram(df, column):
    """
    Show the distribution of
    one numerical column.
    """

    plt.figure(
        figsize=(8, 5)
    )

    sns.histplot(
        data=df,
        x=column,
        bins=20,
        kde=True,
        color="steelblue"
    )

    plt.title(
        f"Distribution of {column}"
    )

    plt.xlabel(column)
    plt.ylabel("Frequency")

    filename = (
        f"histogram_"
        f"{clean_filename(column)}.png"
    )

    save_figure(filename)

    plt.close()


# =========================================================
# 2. Boxplot
# =========================================================

def plot_boxplot(df, column):
    """
    Show the distribution and
    possible outliers.
    """

    plt.figure(
        figsize=(8, 5)
    )

    sns.boxplot(
        data=df,
        y=column,
        color="orange"
    )

    plt.title(
        f"Boxplot of {column}"
    )

    plt.ylabel(column)

    filename = (
        f"boxplot_"
        f"{clean_filename(column)}.png"
    )

    save_figure(filename)

    plt.close()


# =========================================================
# 3. Scatter Plot
# =========================================================

def plot_scatter(df, x_column, y_column):
    """
    Show the relationship between
    two numerical columns.
    """

    plt.figure(
        figsize=(8, 5)
    )

    sns.scatterplot(
        data=df,
        x=x_column,
        y=y_column,
        color="green",
        s=70
    )

    plt.title(
        f"{x_column} vs {y_column}"
    )

    plt.xlabel(x_column)
    plt.ylabel(y_column)

    filename = (
        f"scatter_"
        f"{clean_filename(x_column)}_vs_"
        f"{clean_filename(y_column)}.png"
    )

    save_figure(filename)

    plt.close()


# =========================================================
# 4. Regression Plot
# =========================================================

def plot_regression(df, x_column, y_column):
    """
    Show the relationship between
    two variables with a regression line.
    """

    plt.figure(
        figsize=(8, 5)
    )

    sns.regplot(
        data=df,
        x=x_column,
        y=y_column,
        color="purple",
        scatter_kws={
            "s": 60
        }
    )

    plt.title(
        f"{x_column} vs {y_column}"
    )

    plt.xlabel(x_column)
    plt.ylabel(y_column)

    filename = (
        f"regression_"
        f"{clean_filename(x_column)}_vs_"
        f"{clean_filename(y_column)}.png"
    )

    save_figure(filename)

    plt.close()


# =========================================================
# 5. Correlation Heatmap
# =========================================================

def plot_correlation_heatmap(df):
    """
    Show correlations between
    numerical columns.
    """

    correlation = (
        df
        .select_dtypes(
            include="number"
        )
        .corr()
    )

    plt.figure(
        figsize=(12, 8)
    )

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5
    )

    plt.title(
        "Correlation Heatmap"
    )

    save_figure(
        "correlation_heatmap.png"
    )

    plt.close()


# =========================================================
# 6. Bar Chart
# =========================================================

def plot_bar_chart(df, column):
    """
    Show the frequency of values
    in a categorical column.
    """

    values = (
        df[column]
        .value_counts()
    )

    plt.figure(
        figsize=(8, 5)
    )

    sns.barplot(
        x=values.index,
        y=values.values,
        color="teal"
    )

    plt.title(
        f"Distribution of {column}"
    )

    plt.xlabel(column)
    plt.ylabel("Count")

    filename = (
        f"bar_chart_"
        f"{clean_filename(column)}.png"
    )

    save_figure(filename)

    plt.close()


# =========================================================
# 7. Line Plot
# =========================================================

def plot_line(df, x_column, y_column):
    """
    Show how one numerical variable
    changes according to another.
    """

    sorted_df = df.sort_values(
        by=x_column
    )

    plt.figure(
        figsize=(9, 5)
    )

    sns.lineplot(
        data=sorted_df,
        x=x_column,
        y=y_column,
        color="red"
    )

    plt.title(
        f"{y_column} according to {x_column}"
    )

    plt.xlabel(x_column)
    plt.ylabel(y_column)

    filename = (
        f"line_"
        f"{clean_filename(x_column)}_vs_"
        f"{clean_filename(y_column)}.png"
    )

    save_figure(filename)

    plt.close()


# =========================================================
# 8. Pair Plot
# =========================================================

def plot_pairplot(df):
    """
    Show relationships between
    numerical variables.
    """

    numerical_df = (
        df.select_dtypes(
            include="number"
        )
    )

    plot = sns.pairplot(
        numerical_df
    )

    plot.fig.suptitle(
        "Pair Plot of Numerical Variables",
        y=1.02
    )

    file_path = (
        FIGURES_DIR /
        "pairplot.png"
    )

    plot.savefig(
        file_path,
        dpi=300,
        bbox_inches="tight"
    )

    print(
        f"Figure saved: {file_path}"
    )

    plt.close()


# =========================================================
# 9. Count Plot
# =========================================================

def plot_countplot(df, column):
    """
    Show the number of observations
    in each category.
    """

    plt.figure(
        figsize=(8, 5)
    )

    sns.countplot(
        data=df,
        x=column,
        color="cornflowerblue"
    )

    plt.title(
        f"Count of {column}"
    )

    plt.xlabel(column)
    plt.ylabel("Count")

    filename = (
        f"countplot_"
        f"{clean_filename(column)}.png"
    )

    save_figure(filename)

    plt.close()


# =========================================================
# 10. Calories Distribution
# =========================================================

def plot_calories_distribution(df):
    """
    Show the distribution of
    Calories Burned.
    """

    column = "Calories Burned"

    plt.figure(
        figsize=(8, 5)
    )

    sns.histplot(
        data=df,
        x=column,
        bins=20,
        kde=True,
        color="crimson"
    )

    plt.title(
        "Calories Burned Distribution"
    )

    plt.xlabel(
        "Calories Burned"
    )

    plt.ylabel(
        "Frequency"
    )

    save_figure(
        "calories_burned_distribution.png"
    )

    plt.close()


# =========================================================
# 11. Calories vs Running Time
# =========================================================

def plot_calories_vs_time(df):
    """
    Show the relationship between
    running time and calories burned.
    """

    plot_scatter(
        df,
        "Running Time(min)",
        "Calories Burned"
    )


# =========================================================
# 12. Calories vs Distance
# =========================================================

def plot_calories_vs_distance(df):
    """
    Show the relationship between
    distance and calories burned.
    """

    plot_scatter(
        df,
        "Distance(km)",
        "Calories Burned"
    )


# =========================================================
# 13. Calories vs Heart Rate
# =========================================================

def plot_calories_vs_heart_rate(df):
    """
    Show the relationship between
    heart rate and calories burned.
    """

    plot_scatter(
        df,
        "Average Heart Rate",
        "Calories Burned"
    )


# =========================================================
# 14. Calories vs Weight
# =========================================================

def plot_calories_vs_weight(df):
    """
    Show the relationship between
    weight and calories burned.
    """

    plot_scatter(
        df,
        "Weight(kg)",
        "Calories Burned"
    )


# =========================================================
# 15. Violin Plot
# =========================================================

def plot_violin(df, column):
    """
    Show the distribution of a
    numerical variable.
    """

    plt.figure(
        figsize=(8, 5)
    )

    sns.violinplot(
        data=df,
        y=column,
        color="mediumpurple"
    )

    plt.title(
        f"Violin Plot of {column}"
    )

    plt.ylabel(column)

    filename = (
        f"violin_"
        f"{clean_filename(column)}.png"
    )

    save_figure(filename)

    plt.close()


# =========================================================
# 16. KDE Plot
# =========================================================

def plot_kde(df, column):
    """
    Show the probability distribution
    of a numerical variable.
    """

    plt.figure(
        figsize=(8, 5)
    )

    sns.kdeplot(
        data=df,
        x=column,
        fill=True,
        color="darkcyan"
    )

    plt.title(
        f"KDE Distribution of {column}"
    )

    plt.xlabel(column)
    plt.ylabel("Density")

    filename = (
        f"kde_"
        f"{clean_filename(column)}.png"
    )

    save_figure(filename)

    plt.close()


# =========================================================
# 17. Target Correlation Bar Chart
# =========================================================

def plot_target_correlations(
    df,
    target_column="Calories Burned"
):
    """
    Show the correlation of every
    numerical feature with the target.
    """

    correlation = (
        df
        .select_dtypes(
            include="number"
        )
        .corr()[target_column]
        .drop(target_column)
        .sort_values()
    )

    plt.figure(
        figsize=(9, 6)
    )

    correlation.plot(
        kind="barh",
        color="slateblue"
    )

    plt.title(
        f"Correlation with {target_column}"
    )

    plt.xlabel("Correlation")
    plt.ylabel("Feature")

    save_figure(
        "target_correlations.png"
    )

    plt.close()


# =========================================================
# 18. Calories by Gender
# =========================================================

def plot_calories_by_gender(df):
    """
    Compare calories burned between genders.
    """

    if "Gender" not in df.columns:
        print(
            "Gender column not found."
        )
        return

    plt.figure(
        figsize=(8, 5)
    )

    sns.boxplot(
        data=df,
        x="Gender",
        y="Calories Burned",
        color="lightcoral"
    )

    plt.title(
        "Calories Burned by Gender"
    )

    plt.xlabel("Gender")
    plt.ylabel("Calories Burned")

    save_figure(
        "calories_by_gender.png"
    )

    plt.close()


# =========================================================
# 19. Scatter Plot by Gender
# =========================================================

def plot_scatter_by_gender(
    df,
    x_column,
    y_column
):
    """
    Show a relationship between two
    numerical variables separated by gender.
    """

    if "Gender" not in df.columns:
        print(
            "Gender column not found."
        )
        return

    plt.figure(
        figsize=(8, 5)
    )

    sns.scatterplot(
        data=df,
        x=x_column,
        y=y_column,
        hue="Gender",
        s=70
    )

    plt.title(
        f"{x_column} vs {y_column} by Gender"
    )

    plt.xlabel(x_column)
    plt.ylabel(y_column)

    filename = (
        f"scatter_gender_"
        f"{clean_filename(x_column)}_vs_"
        f"{clean_filename(y_column)}.png"
    )

    save_figure(filename)

    plt.close()