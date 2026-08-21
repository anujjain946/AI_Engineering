import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from config import DATASET_PATH, TEST_SIZE, RANDOM_STATE


def loadDataset():

    df = pd.read_excel(
        DATASET_PATH,
    )
    

    df["Date_of_Journey"] = pd.to_datetime(df["Date_of_Journey"])

    df["Year"] = df["Date_of_Journey"].dt.year
    df["Month"] = df["Date_of_Journey"].dt.month
    df["Day"] = df["Date_of_Journey"].dt.day
    # df["DayOfWeek"] = df["Invoice Date"].dt.dayofweek

    # Airline	Date_of_Journey	Source	Destination	Route	Dep_Time	Arrival_Time	Duration	Total_Stops	Additional_Info


    # df.drop(columns=['Unnamed: 0', 'Retailer ID','Invoice Date','Total Sales'], inplace=True)
    # print(df.head())

 

    X = df[
        [
            "Airline",
            "Source",
            "Destination",
            "Route",
            "Dep_Time",
            "Arrival_Time",
            "Duration",
            "Total_Stops",
            "Additional_Info"
        ]
    ]

    y = df["Price"]



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