import pandas as pd
from pathlib import Path


def extract_csv(file_path: Path) -> pd.DataFrame:
    
    # Read data from a CSV file.

    # Args:
    #     file_path (Path): Path to the CSV file.

    # Returns:
    #     pd.DataFrame: Data loaded from the CSV file.

    # Raises:
    #     FileNotFoundError: If the file does not exist.
    #     ValueError: If the CSV file is empty.
    
    if not file_path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    dataframe = pd.read_csv(file_path)

    if dataframe.empty:
        raise ValueError(f"The file {file_path} is empty.")
    
    return dataframe


def extract_json(file_path: Path) -> pd.DataFrame:
    
    # Read data from a JSON file.

    # Args:
    #     file_path (Path): Path to the JSON file.

    # Returns:
    #     pd.DataFrame: Data loaded from the JSON file.

    # Raises:
    #     FileNotFoundError: If the file does not exist.
    #     ValueError: If the JSON file is empty.
    
    if not file_path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    dataframe = pd.read_json(file_path)

    if dataframe.empty:
        raise ValueError(f"The file {file_path} is empty.")
    
    return dataframe