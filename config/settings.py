from pathlib import Path

from utils.logger import LOG_FILE

# ------------------------
# Project Directories
# ------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

LOG_DIR = BASE_DIR / "logs"


#------------------------
# File Names
#------------------------

INPUT_FILE_NAME = "sales_july.csv"

OUTPUT_FILE_NAME = INPUT_FILE_NAME.replace(".csv", "_processed.csv")


#------------------------
# File Paths
#------------------------

INPUT_FILE = RAW_DATA_DIR / INPUT_FILE_NAME

OUTPUT_FILE = PROCESSED_DATA_DIR / OUTPUT_FILE_NAME

LOG_FILE = LOG_DIR / "etl.log"


DATABASE_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "dataforge_etl"
}