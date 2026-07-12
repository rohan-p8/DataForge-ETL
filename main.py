from pathlib import Path

from etl.extractor import extract_csv, extract_json
from etl.validator import (
    validate_required_columns,
    validate_missing_values,
    validate_positive_numbers,
)

from etl.transformer import (
    standardize_column_names,
    remove_extra_spaces,
    convert_to_title_case,
    remove_duplicates,
)


def main():
    raw_data_dir = Path("data") / "raw"

    try:
        # Extract data from CSV file
        dataframe = extract_csv(raw_data_dir / "sales_july.csv")
        
        # Validate the extracted data
        validate_required_columns(dataframe)
        validate_missing_values(dataframe)
        validate_positive_numbers(dataframe)

        # Transform the data
        dataframe = standardize_column_names(dataframe)
        dataframe = remove_extra_spaces(dataframe)
        dataframe = convert_to_title_case(dataframe)
        dataframe = remove_duplicates(dataframe)


        # Output
        print("\nETL pipeline executed successfully. Here is the transformed data:\n")
        print(dataframe)
        
    except Exception as e:
        print(f"ETL pipeline error: {e}")

if __name__ == "__main__":
    main()