import pandas as pd
from pathlib import Path


def extract_csv(file_path: Path) -> pd.DataFrame:
    """
    Read data from a CSV file and return a Pandas DataFrame.
    """
    return pd.read_csv(file_path)


def extract_json(file_path: Path) -> pd.DataFrame:
    """
    Read data from a JSON file and return a Pandas DataFrame.
    """
    return pd.read_json(file_path)