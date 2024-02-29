import re
import pandas as pd
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test



def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def rename_columns(df):
    df.columns = [camel_to_snake(col) for col in df.columns]
    return df

@transformer
def transform_df(df: DataFrame, *args, **kwargs) -> DataFrame:
    
    # Rename pandas DataFrame columns from CamelCase to snake_case
    df = rename_columns(df)

    # Remove rows where the passenger  and the trip distance are not greater than 0
    greater_zero_passengers = df['passenger_count'] > 0
    greater_zero_distance = df['trip_distance'] > 0
    df = df[greater_zero_passengers & greater_zero_distance]

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date
    df["lpep_pickup_date"] = df["lpep_pickup_datetime"].dt.date
    
    return df



@test
def test_output(df) -> None:
    
    assert df is not None, 'The output is undefined'

    # Assert vendor_id is one of the existing values in the column (currently)
    assert "vendor_id" in df.columns, "Column 'vendor_id' missing"
    
    df_count = df.shape[0]
    
    # Assert passenger_count is greater than 0
    greater_zero_passengers = df['passenger_count'] > 0
    assert greater_zero_passengers.sum() == df_count, "Not all vaues in 'passenger_count' are greater than 0 "

    # Assert trip_distance is greater than 0
    greater_zero_distance = df['trip_distance'] > 0
    assert greater_zero_distance.sum() == df_count, "Not all vaues in 'passenger_count' are greater than 0 "

