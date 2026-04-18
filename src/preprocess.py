import pandas as pd

def preprocess_data(df):
    df = df.drop(['UDI','Product ID'],axis=1)
    df['Type'] = df['Type'].map({'L':0,'M':1,'H':2})
    df = df.fillna(df.mean(numeric_only=True))
    return df