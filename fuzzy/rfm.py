import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def calculate_recency(df,present_day):
    # Get the most recency purchase of each customer
    recency_df = df.groupby(by="user_id").date.max().reset_index()
    recency_df.columns = ["user_id","most_recent_purchase"]
    recency_df["most_recent_purchase"] = pd.to_datetime(recency_df["most_recent_purchase"])

    # Calculate recency score
    present_day = pd.to_datetime(present_day)
    recency_df["recency"] = (present_day - recency_df["most_recent_purchase"]).dt.days
    return recency_df

def find_k(df,score_name):
    # Use k-means to determine the optimal number of clusters
    sse = {}
    score = df[[score_name]]

    for k in range(1,10):
        kmeans = KMeans(n_clusters=k,max_iter=1000).fit(score)
        score["cluster"] = kmeans.labels_
        sse[k] = kmeans.inertia_

    plt.figure()
    plt.plot(list(sse.keys()),list(sse.values()))
    plt.xlabel("No. of clusters (k)")
    plt.show()

# Build a function to re-order the clusters as kmeans did not know the hiarchy of the cluters
def reorder_cluster(df,cluster_col,score_col,ascending):
    new_df = df.groupby(by=cluster_col)[score_col].mean().reset_index()
    new_df = new_df.sort_values(by=score_col,ascending=ascending).reset_index(drop=True)
    new_df["new_cluster"] = new_df.index
    final_df = pd.merge(df,new_df[[cluster_col,"new_cluster"]],on=cluster_col)
    final_df = final_df.drop([cluster_col],axis=1)
    final_df = final_df.rename(columns={"new_cluster":cluster_col})

    return final_df

def calculate_frequency(df):
    # Get the number of purchases of each customer
    freq_df = df.groupby(by="user_id").order_id.count().reset_index()
    freq_df.columns = ["user_id","frequency"]
    return freq_df

def calculate_monetary(df):
    # Find the total spending per customer
    monetary_df = pd.DataFrame(df.groupby("user_id").price_usd.sum())
    monetary_df.columns = ["monetary"]
    monetary_df["monetary"] = monetary_df["monetary"].astype(int)
    return monetary_df