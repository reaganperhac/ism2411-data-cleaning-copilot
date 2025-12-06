"""
data_cleaning.py
Purpose: Load a messy sales dataset, clean it, and save a cleaned version
This project demonstrates basic data cleaning and use of GitHub Copilot
"""
#code was edited slighlty by me because i had many errors
import pandas as pd

#1 — load_data
# copilot

#return a pandas DataFrame.


def load_data(file_path: str):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: Could not find file at {file_path}")
        return pd.DataFrame()   # safe fallback instead of returning None

    
#2 — clean_column_names
#copilot 
#cleans up column names


def clean_column_names(df):
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )    
    return df

def standardize_core_columns(df):
    df = df.copy()
    df = df.rename(columns={
        "qty": "quantity"
    })
    return df

#3 — handle_missing_values

#handle missing values
#rows missing both price and quantity cant be used


def handle_missing_values(df):
    df = df.copy()

    df = df.dropna(subset=["price", "quantity"], how="all")

    df["price"] = df["price"].fillna(0)
    df["quantity"] = df["quantity"].fillna(0)

    return df




#4 remove_invalid_rows


#remove negative quantities and prices
#negative values usually data entry errors


def remove_invalid_rows(df):
    df = df.copy()

    #convert to numbers because of the errors
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    #get rid of negative values
    df = df[(df["price"] >= 0) & (df["quantity"] >= 0)]

    return df



#main script

if __name__ == "__main__":

    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)

    df_clean = clean_column_names(df_raw)

    df_clean = standardize_core_columns(df_clean)

    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())
