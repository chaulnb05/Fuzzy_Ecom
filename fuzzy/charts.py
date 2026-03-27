import pandas as pd
import matplotlib.pyplot as plt

def data_over_time(df:pd.DataFrame,time_intervals:list,title):
    fig, subplots = plt.subplots(nrows=len(time_intervals),squeeze=False,figsize=(10,8))
    fig.suptitle(title)
    col_name = df.columns[0]
    for plot,interval in zip(subplots.flatten(),time_intervals):
        time_df = pd.DataFrame(df.groupby(by=interval).count()[col_name])
        plot.bar(time_df.index,time_df[col_name])
        plot.set_xlabel(interval)
    fig.tight_layout()
    return fig

def time_series_count(df:pd.DataFrame,title:str="Time series",):
    id_col = df.columns[0]
    df_by_date = df.groupby(by="date").count()[id_col]
    df_by_date
    return df_by_date.plot(figsize=(12,5),title=title)

def categorical_time_series(df,category,target):
    id_col = df.columns[0]
    df = df.groupby(by=["date",category]).count()[[id_col]]
    df.columns = [target]
    df.reset_index(inplace=True)
    piv_df = df.pivot(columns=category,index="date")
    piv_df.fillna(0,inplace=True)
    piv_df.plot(figsize=(15,5))