import pandas as pd
import glob
import os

def run_etl(input_folder:str,output_folder:str) -> pd.DataFrame:
    """ Run the ETL pipeline:
        - Extract raw data fromt he input file
        - Transform the raw data
        - Load processed data into an output folder

    Args:
        input_folder (str): name of input data folder
        output_folder (str): name of output data folder

    Returns:
        pd.DataFrame: _description_
    """
    # Access raw data folder and list all files found
    raw_files = glob.glob(os.path.join(input_folder, "*.csv"))
    for file in raw_files:
        print(f"Found {os.path.basename(file)} CSV files in /{input_folder} folder")

    # Extract data from csv files
    for file_path in raw_files:
        # Extract
        df = pd.read_csv(file_path)

        # Transform:
        # Replace null/missing values with "Unknown"
        df = df.fillna("unknown")
        # Extract time elements
        if "created_at" in df.columns:
            df['created_at'] = pd.to_datetime(df['created_at'])
            df['hour'] = df['created_at'].dt.hour
            df['week_day'] = df['created_at'].dt.dayofweek
            df['week_day_name'] = df['created_at'].dt.day_name()
            df['day'] = df['created_at'].dt.day
            df['month'] = df['created_at'].dt.month
            df['month_name'] = df['created_at'].dt.month_name()
            df['date'] = df['created_at'].dt.date

        # Load:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        file_name = os.path.basename(file_path)  # e.g., data1.csv
        output_file = os.path.join(output_folder, file_name)
        df.to_csv(output_file, index=False)
        print(f"Loading {file_name} to /{output_folder}")

if __name__ == "__main__":
    run_etl("data/raw_data", "data/processed_data")
