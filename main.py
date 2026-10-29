import pandas as pd
import numpy as np

def analyze_and_clean_data(file_path):
    print("=" * 50)
    print("🚀 Data Quality & Cleaning Assistant Started")
    print("=" * 50)
    
    try:
        df = pd.read_csv(file_path)
        print(f"\n[+] Successfully loaded dataset: {file_path}")
        print(f"    - Total Rows: {df.shape[0]}")
        print(f"    - Total Columns: {df.shape[1]}")
    except FileNotFoundError:
        print(f"[-] Error: The file '{file_path}' was not found.")
        return
    
    # Missing Values
    print("\n--- 1. Missing Values Analysis ---")
    missing_values = df.isnull().sum()
    print(missing_values[missing_values > 0] if missing_values.sum() > 0 else "No missing values found!")
    
    # Duplicates
    print("\n--- 2. Duplicates Analysis ---")
    duplicates_count = df.duplicated().sum()
    print(f"Found {duplicates_count} duplicate rows.")
    
    # Cleaning
    print("\n--- 3. Cleaning Data... ---")
    df_cleaned = df.drop_duplicates()
    
    numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df_cleaned[col].isnull().sum() > 0:
            mean_val = df_cleaned[col].mean()
            df_cleaned[col].fillna(mean_val, inplace=True)
            print(f"    - Filled missing values in column '{col}' with mean: {mean_val:.2f}")
            
    output_file = "cleaned_dataset.csv"
    df_cleaned.to_csv(output_file, index=False)
    print(f"\n[+] Cleaned dataset successfully saved as '{output_file}'")
    print("=" * 50)

if __name__ == "__main__":
    print("Run analyze_and_clean_data('your_file.csv') to execute.")
