import pandas as pd


def standardize_column_names(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Standardizes column names by converting them to lowercase.
    """
    
    dataframe.columns = dataframe.columns.str.lower()
    
    return dataframe


def remove_extra_spaces(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Removes leading and trailing spaces from string columns in the DataFrame.
    """
    
    string_columns = dataframe.select_dtypes(include=["object"]).columns

    for column in string_columns:
        dataframe[column] = dataframe[column].str.strip()
    
    return dataframe


def convert_to_title_case(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Converts customer and product names to title case.
    """

    dataframe["customer_name"] = dataframe["customer_name"].str.title()

    dataframe["product"] = dataframe["product"].str.title()

    return dataframe


def remove_duplicates(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicate rows from the DataFrame.
    """
    
    return dataframe.drop_duplicates()