# CSV Data Validation Tool

A simple command-line Python tool for validating structured CSV files against required fields and parameter constraints.

## Overview
This project performs basic data quality checks on CSV files, ensuring that required columns are present, mandatory values are populated, and numeric parameters fall within acceptable ranges.

The tool was designed to reflect real-world data validation scenarios, where datasets may be incomplete, malformed, or inconsistent, and must be checked defensively before further processing.

## Features
- Verifies presence of required CSV columns
- Checks required fields for missing or empty values
- Validates numeric fields and value ranges
- Flags invalid rows and reports total error count
- Uses only Python standard library modules

## Technologies
- Python
- csv (standard library)

## Validation Rules
- Required fields must be present in the CSV header
- Required fields must contain non-empty values
- `concentration` must be a non-negative number
- Optional `temp` field must fall within an acceptable range if provided

## Usage
1. Place your CSV file in the project directory and name it `file.csv`
2. Run the script: python cli_csv_audit_tool.py


