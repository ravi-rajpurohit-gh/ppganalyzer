import pandas as pd

def load_signal(file_path):
    """
    Loads a signal from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing signal data.

    Returns:
        pd.DataFrame: A DataFrame containing the time and signal values.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading signal: {e}")
        return None
