from src.main import load_and_process_data
import pandas as pd
import os

def test_duplicate_removal():
    # Prepare a test CSV file (test-only, doesn't touch your main data)
    test_input = 'data/test_input.csv'
    test_output = 'data/test_output.csv'
    pd.DataFrame({
        'name': ['Alice', 'Bob', 'Alice'],
        'age': [30, 25, 30],
    }).to_csv(test_input, index=False)

    result = load_and_process_data(test_input, test_output)
    assert len(result) == 2  # Only 2 unique rows should remain

    os.remove(test_input)
    os.remove(test_output)