import pandas as pd
import os

def load_and_process_data(input_path='data/dataset.csv', output_path='data/processed_dataset.csv'):
    df = pd.read_csv(input_path)
    df_clean = df.drop_duplicates()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_clean.to_csv(output_path, index=False)
    return df_clean