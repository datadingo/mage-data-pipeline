import io
import pandas as pd
import requests
from pandas import DataFrame

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(**kwargs) -> DataFrame:

    # Define base url
    base_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/"
    year = 2020

    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID':pd.Int64Dtype(),
        'store_and_fwd_flag':str,
        'PULocationID':pd.Int64Dtype(),
        'DOLocationID':pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra':float,
        'mta_tax':float,
        'tip_amount':float,
        'tolls_amount':float,
        'improvement_surcharge':float,
        'total_amount':float,
        'congestion_surcharge':float
    }
    datetime_cols = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    
    # Initialize an empty list to store DataFrames
    dfs = []
    months = [10, 11, 12]

    # Loop through the months for which we want to get files
    for month in months:
        url = f"{base_url}green_tripdata_{year}-{month}.csv.gz"
        dfs.append(pd.read_csv(url, sep=',', compression='gzip', dtype=taxi_dtypes, parse_dates=datetime_cols))
    
    # Concatenate all DataFrames in the list into a single DataFrame
    df = pd.concat(dfs, ignore_index=True)

    return df 


@test
def test_output(df) -> None:
    assert df is not None, 'The output is undefined'
