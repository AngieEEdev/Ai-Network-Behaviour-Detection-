import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()  
    return df

def clean_data(df):
    return df.dropna()

def label_data(df):
    y = df['label']
    X = df.drop(columns=['label'])
    return X, y

def label_data(df):
    if 'label' not in df.columns:
        raise ValueError(f"Expected 'label' column, found: {df.columns}")

    y = df['label']
    X = df.drop(columns=['label'])
    return X, y