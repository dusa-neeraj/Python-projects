#!/usr/bin/env python3
import argparse
import os
import sys

import pandas as pd

def parse_arguments() -> argparse.Namespace:
    """Define and parse command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="csv_summary_analyzer.py",
        description="Generate a clean summary report for any CSV file.",
    )
    parser.add_argument(
        "file_path",
        type=str,
        help="Path to the CSV file to analyze",
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="Optional path to save the report as a text file",
    )
    return parser.parse_args()


# --------------------------------------------------------------------------
# Data loading
# --------------------------------------------------------------------------
def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame with proper error handling.

    Raises:
        FileNotFoundError: if the file does not exist.
        ValueError: if the file is empty or not a valid CSV.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: '{file_path}'")

    if os.path.getsize(file_path) == 0:
        raise ValueError(f"The file '{file_path}' is empty.")

    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        raise ValueError(f"The file '{file_path}' has no columns/data to parse.")
    except pd.errors.ParserError as e:
        raise ValueError(f"The file '{file_path}' is not a valid CSV. ({e})")

    if df.shape[0] == 0 and df.shape[1] == 0:
        raise ValueError(f"The file '{file_path}' contains no data.")

    return df


# --------------------------------------------------------------------------
# Report sections
# NOTE: every section is built as a list of lines joined with "\n".
# This avoids accidental Python string-literal concatenation bugs that
# can happen when mixing multi-line string literals with "*" repetition.
# --------------------------------------------------------------------------
def get_shape_summary(df: pd.DataFrame) -> str:
    """Return total rows and columns as a formatted string."""
    rows, cols = df.shape
    lines = [
        "1. DATASET OVERVIEW",
        "-" * 40,
        f"Total Rows    : {rows}",
        f"Total Columns : {cols}",
    ]
    return "\n".join(lines) + "\n"


def get_column_info(df: pd.DataFrame) -> str:
    """Return column names with their data types."""
    lines = ["2. COLUMN NAMES & DATA TYPES", "-" * 40]
    for col in df.columns:
        lines.append(f"{col:<25} {str(df[col].dtype)}")
    return "\n".join(lines) + "\n"


def get_missing_values(df: pd.DataFrame) -> str:
    """Return count and percentage of missing values per column."""
    lines = ["3. MISSING VALUES PER COLUMN", "-" * 40]
    missing = df.isnull().sum()
    total_rows = len(df) if len(df) > 0 else 1

    any_missing = False
    for col, count in missing.items():
        if count > 0:
            any_missing = True
        pct = (count / total_rows) * 100
        lines.append(f"{col:<25} {count:<8} ({pct:.2f}%)")

    if not any_missing:
        lines.append("No missing values found in the dataset.")

    return "\n".join(lines) + "\n"


def get_numeric_statistics(df: pd.DataFrame) -> str:
    """Return mean, median, min, max, and std deviation for numeric columns."""
    lines = ["4. NUMERIC COLUMN STATISTICS", "-" * 40]
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        lines.append("No numeric columns found in the dataset.")
        return "\n".join(lines) + "\n"

    header = f"{'Column':<20}{'Mean':>12}{'Median':>12}{'Min':>12}{'Max':>12}{'Std Dev':>12}"
    lines.append(header)
    lines.append("-" * len(header))

    for col in numeric_df.columns:
        series = numeric_df[col].dropna()
        if series.empty:
            lines.append(f"{col:<20}{'N/A':>12}{'N/A':>12}{'N/A':>12}{'N/A':>12}{'N/A':>12}")
            continue
        mean = series.mean()
        median = series.median()
        minimum = series.min()
        maximum = series.max()
        std = series.std() if len(series) > 1 else 0.0
        lines.append(
            f"{col:<20}{mean:>12.2f}{median:>12.2f}{minimum:>12.2f}{maximum:>12.2f}{std:>12.2f}"
        )

    return "\n".join(lines) + "\n"


def build_report(df: pd.DataFrame, file_path: str) -> str:
    """Assemble the full report from all individual sections."""
    divider = "=" * 60
    header_lines = [
        divider,
        "               CSV SUMMARY ANALYZER REPORT",
        divider,
        f"File Analyzed : {file_path}",
        divider,
    ]
    header = "\n".join(header_lines) + "\n"

    sections = [
        get_shape_summary(df),
        get_column_info(df),
        get_missing_values(df),
        get_numeric_statistics(df),
    ]

    footer_lines = [
        divider,
        "                  END OF REPORT",
        divider,
    ]
    footer = "\n".join(footer_lines)

    return header + "\n" + "\n".join(sections) + "\n" + footer


# --------------------------------------------------------------------------
# Output handling
# --------------------------------------------------------------------------
def output_report(report: str, output_path: str = None) -> None:
    """Print the report to the console and optionally save it to a file."""
    print(report)

    if output_path:
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"\nReport saved to: {output_path}")
        except OSError as e:
            print(f"\nWarning: Could not save report to '{output_path}'. ({e})", file=sys.stderr)


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------
def main() -> None:
    args = parse_arguments()

    try:
        df = load_csv(args.file_path)
        report = build_report(df, args.file_path)
        output_report(report, args.output)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Catch-all for any unexpected error so the CLI never crashes ugly.
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
