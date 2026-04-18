def create_features(df):
    df = df.dropna()
    X = df.drop(['TWF','HDF','PWF','OSF','RNF','Machine failure'],axis=1)
    Y = df["Machine failure"]
    return X,Y
