from pathlib import Path

from etl.extractor import extract_csv, extract_json


def main():
    try:
        raw_data_dir = Path("data") / "raw"

        csv_file = raw_data_dir / "sales_july.csv"
        json_file = raw_data_dir / "sales_july.json"

        csv_data = extract_csv(csv_file)
        json_data = extract_json(json_file)

        print("CSV Data:")
        print(csv_data)

        print("\nJSON Data:")
        print(json_data)
        
    except Exception as e:
        print(f"ETL pipeline error: {e}")

if __name__ == "__main__":
    main()