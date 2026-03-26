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
