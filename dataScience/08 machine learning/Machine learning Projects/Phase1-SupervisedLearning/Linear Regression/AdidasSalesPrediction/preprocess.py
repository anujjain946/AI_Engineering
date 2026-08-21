import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from config import DATASET_PATH, TEST_SIZE, RANDOM_STATE


def loadDataset():

    df = pd.read_excel(
        DATASET_PATH,
        header=4
    )

    df["Invoice Date"] = pd.to_datetime(df["Invoice Date"])

    df["Year"] = df["Invoice Date"].dt.year
    df["Month"] = df["Invoice Date"].dt.month
    df["Day"] = df["Invoice Date"].dt.day
    df["DayOfWeek"] = df["Invoice Date"].dt.dayofweek

    # df.drop(columns=['Unnamed: 0', 'Retailer ID','Invoice Date','Total Sales'], inplace=True)
    # print(df.head())

 

    X = df[
        [
            "Retailer",
            "Region",
            "State",
            "City",
            "Product",
            "Price per Unit",
            "Units Sold",
            "Sales Method",
            "Year",
            "Month",
            "Day",
            "DayOfWeek"
        ]
    ]

    y = df["Total Sales"]



    return train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

# load_data()

# X_train, X_test, y_train, y_test = load_data()

# print("X_train shape:", X_train.shape)
# print("X_test shape:", X_test.shape)