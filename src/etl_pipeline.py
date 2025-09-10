import pandas as pd
import sqlite3
import os

def run_etl(input_path, output_dir="data/processed", db_path="outputs/datasets/company.db"):
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Extract
    df = pd.read_csv(input_path)

    # Transform
    df['joining_date'] = pd.to_datetime(df['joining_date'])
    df['tenure_years'] = (pd.Timestamp.now() - df['joining_date']).dt.days / 365

    processed_path = os.path.join(output_dir, "employees_processed.csv")
    df.to_csv(processed_path, index=False)

    # Load
    conn = sqlite3.connect(db_path)
    df.to_sql("employees", conn, if_exists="replace", index=False)
    conn.close()

    return processed_path, db_path
