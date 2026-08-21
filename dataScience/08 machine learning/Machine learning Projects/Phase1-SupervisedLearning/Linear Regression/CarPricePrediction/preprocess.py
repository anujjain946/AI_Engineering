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
    X = df.drop(columns=["Present_Price","Car_Name","Fuel_Type","Seller_Type","Transmission"])



    # print(X.head())

    y = df["Present_Price"]

    # print(df.head())
    
    return train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )