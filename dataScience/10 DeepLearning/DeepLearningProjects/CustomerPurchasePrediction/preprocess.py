import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

import joblib

from config import *

def load_data():

    df = pd.read_csv(DATASET_PATH)

    
    X = df[['Age','Gender','MaritalStatus','AnnualIncome','WebsiteVisits','AppUsageHours']]

    X = pd.get_dummies(
        X,
        columns=[
            "Gender",
            "MaritalStatus"
        ],
        drop_first=True
    )

    print(X.columns.tolist())

    joblib.dump(
    X.columns.tolist(),
    COLUMNS_PATH
    # "model/model_columns.pkl"
)

    # print(X.head())
    # print(X.dtypes)


    y = df['Purchased']

    scaler = StandardScaler()

    X = scaler.fit_transform(X)

    joblib.dump(scaler, SCALER_PATH)

    return train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )