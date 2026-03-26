import glob
import os
import pandas as pd

def all_csv_to_df(input_folder:str) -> dict[str,pd.DataFrame]:
    all_files = glob.glob(os.path.join(input_folder, "*.csv"))
    all_df = {os.path.basename(f): pd.read_csv(f) for f in all_files}
    print("Importing:")
    for name,df in all_df.items():
        if "created_at" in df.columns:
            df["created_at"] = pd.to_datetime(df["created_at"])
        print(f"{name}: {df.shape[0]} rows, {df.shape[1]} columns")
    return all_df

def ordered_time(series:pd.Series,type:str=["week","month"]):
    if type == "month":
        month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        return pd.Categorical(series, categories=month_order, ordered=True)
    elif type == "week":
        week_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return pd.Categorical(series, categories=week_order, ordered=True)
    else:
        print("wrong type")