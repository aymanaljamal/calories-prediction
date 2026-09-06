from pathlib import Path
import subprocess
import sys
import shutil


PROJECT_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
OUTPUT_DIR = PROJECT_ROOT / "reports" / "notebooks"


NOTEBOOKS = [
    "01_1_data_exploration.ipynb",
    "01_2_data_exploration.ipynb",
    "01_3_data_visualization.ipynb",
    "02_data_analysis.ipynb",
    "03_machine_learning.ipynb",
]


def find_browser():
    """Find Microsoft Edge or Google Chrome."""

    possible_browsers = [
        shutil.which("msedge"),
        shutil.which("chrome"),

        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),

        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
    ]

    for browser in possible_browsers:
        if browser:
            browser_path = Path(browser)

            if browser_path.exists():
                return browser_path

    return None


def convert_notebook_to_html(notebook_path):
    """Convert Jupyter Notebook to HTML."""

    command = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        "html",
        str(notebook_path),
        "--output-dir",
        str(OUTPUT_DIR),
    ]

    result = subprocess.run(command, cwd=PROJECT_ROOT)

    if result.returncode != 0:
        return False

    return True


def convert_html_to_pdf(browser, html_path, pdf_path):
    """Convert HTML file to PDF using Edge/Chrome."""

    html_url = html_path.resolve().as_uri()

    command = [
        str(browser),
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path.resolve()}",
        html_url,
    ]

    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        timeout=120
    )

    return result.returncode == 0 and pdf_path.exists()


def main():

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("JUPYTER NOTEBOOK PDF EXPORT")
    print("=" * 70)

    browser = find_browser()

    if browser is None:
        print("\nERROR: Microsoft Edge or Google Chrome was not found.")
        print("Please install/use Microsoft Edge or Google Chrome.")
        sys.exit(1)

    print(f"\nBrowser found: {browser}")

    success_count = 0

    for notebook in NOTEBOOKS:

        notebook_path = NOTEBOOKS_DIR / notebook

        if not notebook_path.exists():
            print(f"\nWARNING: Notebook not found: {notebook}")
            continue

        print("\n" + "-" * 70)
        print(f"Processing: {notebook}")
        print("-" * 70)

        # Step 1: Notebook -> HTML
        print("1. Converting Notebook to HTML...")

        if not convert_notebook_to_html(notebook_path):
            print("FAILED: HTML conversion")
            continue

        html_path = OUTPUT_DIR / f"{notebook[:-6]}.html"
        pdf_path = OUTPUT_DIR / f"{notebook[:-6]}.pdf"

        if not html_path.exists():
            print(f"FAILED: HTML file was not created")
            continue

        print(f"HTML created: {html_path}")

        # Step 2: HTML -> PDF
        print("2. Converting HTML to PDF...")

        if convert_html_to_pdf(browser, html_path, pdf_path):
            print(f"SUCCESS: PDF created")
            print(f"PDF: {pdf_path}")
            success_count += 1
        else:
            print("FAILED: PDF conversion")

    print("\n" + "=" * 70)
    print("EXPORT COMPLETED")
    print("=" * 70)

    print(f"\nSuccessfully exported: {success_count}/{len(NOTEBOOKS)} notebooks")

    print(f"\nPDF files are located in:")
    print(OUTPUT_DIR)


if __name__ == "__main__":
    main()