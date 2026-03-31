import pandas as pd
import pytest
from etl import extract_date,impute_missing  

def test_date_extracted():
    # Test data
    raw_data = pd.DataFrame({
        "created_at": ["2013-01-01 17:45:00"],
        "user_id": [None]
    })
    
    # Apply function
    output_df = extract_date(raw_data)
    
    # Check if your function did its job
    assert output_df["month_name"].iloc[0] == "January"
    assert output_df["week_day_name"].iloc[0] == "Tuesday"
    assert output_df["hour"].iloc[0] == 17

def test_impute():
    # Test data
    raw_data = pd.DataFrame({
        "created_at": ["2013-01-01 17:45:00"],
        "user_id": [None]
    })
    
    # Apply function
    output_df = impute_missing(raw_data)
    
    # Check if your function did its job
    assert output_df["user_id"].iloc[0] == "unknown"


