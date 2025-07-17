import pandas as pd

def extract(path):
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    path_to_data = "/home/gabriel/repos/etl_apache_nifi/input/data.csv"
    raw_df = extract(path_to_data)
    print(raw_df.head(10))