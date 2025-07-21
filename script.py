#!/usr/bin/env python3
import pandas as pd
import sys
import io

def extract(path):
    df = pd.read_csv(path)
    return df


def transform(df):
    df['married'] = df['married'].map({'TRUE': 1, 'FALSE': 0, 'yes': 1, 'no': 0, '0': 0, '1': 1})
    df['married'] = df['married'].fillna(0)
    df['married'] = df['married'].astype(int)
    return df


def load(df):
    df.to_csv(sys.stdout, index=False, lineterminator='\n')


if __name__ == "__main__":
    csv_content = sys.stdin.read()
    csv_data = io.StringIO(csv_content)
    raw_df = extract(csv_data)
    cleaned_df = transform(raw_df)
    load(cleaned_df)
