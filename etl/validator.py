import pandas as pd 

REQUIRED_COLUMNS = ["transaction_id",
                    "customer_id",
                    "product_name",
                    "quantity",
                    "unit_price",
                    "transaction_date"]

def validate_required_columns(dataframe: pd.DataFrame) -> None:
    """
    Ensures that the DataFrame contains all required columns.
    """
    
    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )


def validate_missing_values(dataframe: pd.DataFrame) -> None:
    """
    Ensures that there are no missing values in the DataFrame.
    """
    
    if dataframe.isnull().values.any():
        raise ValueError("DataFrame contains missing values.")
    

def validate_positive_numbers(dataframe: pd.DataFrame) -> None:
    """
    Ensures that the 'quantity' and 'price' columns contain only positive numbers.
    """
    
    if (dataframe["quantity"] <= 0).any():
        raise ValueError("Quantity must be greater than zero.")
    
    if (dataframe["unit_price"] <= 0).any():
        raise ValueError("Unit price must be greater than zero.")