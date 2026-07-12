from pathlib import Path

from etl.extractor import extract_csv, extract_json
from etl.validator import (
    validate_required_columns,
    validate_missing_values,
    validate_positive_numbers,
)


def main():
    raw_data_dir = Path("data") / "raw"

    try:
        dataframe = extract_csv(raw_data_dir / "sales_july.csv")
        
        
        validate_required_columns(dataframe)
        validate_missing_values(dataframe)
        validate_positive_numbers(dataframe)

        print("Validation successful. Data is ready for further processing.")
        print(dataframe)
        
    except Exception as e:
        print(f"ETL pipeline error: {e}")

if __name__ == "__main__":
    main()