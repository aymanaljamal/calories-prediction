from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def run_command(command, name):

    print("\n")
    print("=" * 70)
    print(name)
    print("=" * 70)

    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT
    )

    if result.returncode != 0:
        print(f"\nFAILED: {name}")
        return False

    print(f"\nSUCCESS: {name}")
    return True


def main():

    print("=" * 70)
    print("CALORIES PREDICTION - FULL PIPELINE")
    print("=" * 70)

    python = sys.executable

    steps = [

        (
            [
                python,
                "-m",
                "src.preprocessing"
            ],
            "DATA PREPROCESSING"
        ),

        (
            [
                python,
                "-m",
                "src.train_model"
            ],
            "MODEL TRAINING"
        ),

        (
            [
                python,
                "-m",
                "src.evaluate_model"
            ],
            "MODEL EVALUATION"
        ),

        (
            [
                python,
                "scripts/generate_reports.py"
            ],
            "REPORT GENERATION"
        ),

        (
            [
                python,
                "scripts/export_notebooks.py"
            ],
            "NOTEBOOK PDF EXPORT"
        ),
    ]

    for command, name in steps:

        success = run_command(
            command,
            name
        )

        if not success:
            print("\nPipeline stopped.")
            sys.exit(1)

    print("\n")
    print("=" * 70)
    print("ALL PROJECT STEPS COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()