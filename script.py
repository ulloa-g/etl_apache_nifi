import pandas as pd

def extract(path):
    df = pd.read_csv(path)
    return df

def transform(df):
    df['married'] = df['married'].map({'TRUE': 1, 'FALSE': 0, 'yes': 1, 'no': 0, '0': 0, '1': 1})
    df['married'] = df['married'].fillna(0)
    df['married'] = df['married'].astype(int)
    return df

if __name__ == "__main__":
    path_to_data = "/home/gabriel/repos/etl_apache_nifi/input/data.csv"
    raw_df = extract(path_to_data)
    cleaned_df = transform(raw_df)
