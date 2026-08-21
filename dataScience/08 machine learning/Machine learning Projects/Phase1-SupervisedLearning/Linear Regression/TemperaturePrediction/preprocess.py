import pandas as pd
from config import DATASET_PATH,TEST_SIZE,RANDOM_STATE
from sklearn.model_selection import train_test_split


# loadDatase method
def loadDataset():
    df = pd.read_csv(DATASET_PATH)
# EDA
    # print(df.shape)
    # print(df.head())
    # print(df.isnull().sum())
    # print(df.duplicated().sum())
    # Drop Duplicated value
    df.drop_duplicates(inplace=True)
    # print(df.info())
    # print(df.describe())

# Define features
    df["Date"] = pd.to_datetime(df["Date"])

    df["Day"] = df["Date"].dt.day
    df["Month"] = df["Date"].dt.month
    df["DayOfWeek"] = df["Date"].dt.dayofweek
   
    X = df.drop(columns=["Date", "Temperature"])

    # print(X.head())

    y = df["Temperature"]

    # print(df.head())
    
    return train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )