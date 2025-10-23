# Data Preprocessing Script by Telugu Rakesh
# preprocess.py
import pandas as pd

def load_data(path):
    """Load CSV file"""
    return pd.read_csv(path)

def basic_clean(df):
    """Simple data cleaning"""
    df = df.dropna()
    df = df.drop_duplicates()
    return df

if __name__ == "__main__":
    print("Preprocessing script ready!")
#TODO: Add feature scaling
