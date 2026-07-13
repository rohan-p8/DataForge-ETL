from pathlib import Path
import logging
from venv import logger
import pandas as pd


def save_processed_csv(dataframe: pd.DataFrame, output_path: Path) -> None:
    """
    Saves the processed DataFrame to a CSV file at the specified output path.
    """
    
    # Create the output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    dataframe.to_csv(output_path, index=False)

    
    logger.info(f"Processed file saved to: {output_path}")  