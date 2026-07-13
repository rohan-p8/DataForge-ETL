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

from etl.loader import save_processed_csv


def main():
    raw_data_dir = Path("data") / "raw"
    processed_data_dir = Path("data") / "processed"

    input_file = raw_data_dir / "sales_july.csv"
    output_file = processed_data_dir / "sales_july_processed.csv"

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

        # Load the processed data to a CSV file
        save_processed_csv(dataframe, output_file)


        # Output
        print("\nETL pipeline executed successfully. Here is the transformed data:\n")
        print(dataframe)
        
    except Exception as e:
        print(f"ETL pipeline error: {e}")

if __name__ == "__main__":
    main()