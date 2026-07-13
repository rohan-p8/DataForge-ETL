from pathlib import Path

import pandas as pd


def save_processed_csv(dataframe: pd.DataFrame, output_path: Path) -> None:
    """
    Saves the processed DataFrame to a CSV file at the specified output path.
    """
    
    # Create the output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    dataframe.to_csv(output_path, index=False)

    print(f"Processed file saved to: {output_path}")