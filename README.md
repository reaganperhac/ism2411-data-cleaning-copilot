# ISM2411 Data Cleaning with GitHub Copilot

This project shows a simple, professional data cleaning project, created using Python and GitHub Copilot. The goal was to take a messy sales dataset and make it into a clean version that can be used for analysis. This repository follows a clear structure that includes a cleaning script and documents how AI tools were used during development.

## Project Structure

ism2411-data-cleaning-copilot/
├── data/
│ ├── raw/
│ │ └── sales_data_raw.csv
│ └── processed/
│ └── sales_data_clean.csv
├── src/
│ └── data_cleaning.py
├── README.md
└── reflection.md

## What the Script Does

The cleaning script (`src/data_cleaning.py`) performs the following steps:

1. **Loads the raw CSV**
2. **Standardizes column names**  
   -lowercase  
   -remove spaces and dashes
3. **Standardizes core fields**
   -renaming qty to quantity
4. **Handles missing values**  
   -get rid of rows missing both price and quantity  
   -fills remaining missing numeric values with 0
5. **Removes invalid rows**  
   -changes data to numeric  
   -removes negative prices and quantities

The cleaned dataset is saved to:
data/processed/sales_data_clean.csv

## How to Run

From the project root directory:
python src/data_cleaning.py
If it works, the script will print the first few cleaned rows and update the processed data folder.

## Requirements

Python 3.8+
pandas

Install pandas (if needed):
pip install pandas

## Purpose

This project was designed to show beginner data cleaning skills, show correct use of GitHub Copilot, and produce a portfolio GitHub repository.
