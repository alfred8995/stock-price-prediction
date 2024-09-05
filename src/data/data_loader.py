import pandas as pd

def load_data(file_path):
    """Loads the data from the specified file path."""
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """Performs data cleaning operations like handling missing values."""
    data = data.dropna()
    return data
