import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

import joblib

from config import *

def load_data():

    df = pd.read_csv(DATASET_PATH)
    # print(df.head())
    # print(df.shape)
    # print(df.isnull())
    # print(df.isnull().sum())
    # print(df.columns)

    

    X = df.drop(['CustomerID','Churn'],axis=1)
    # print(X.shape)
    # print(X.head())
    # ------------------------------
    # Check for scalling
    # -----------------------------
    # print(X.describe())
    # print(df.describe().T)

    # y = df['quality']


    X = pd.get_dummies(
        X,
        columns=[
            "Gender",
            "Subscription Type",
            "Contract Length",
        ],
        drop_first=True
    )

    print(X.columns.tolist())

    joblib.dump(
    X.columns.tolist(),
    "models/model_columns.pkl"
)

    y = (df["Churn"]).astype(int)

    # print(y.head())

    # ------------------------------
    #Data Split
    # -----------------------------

    X_train,X_test,y_train,y_test = train_test_split(
        X,
        y,
        random_state=RANDOM_STATE,
        test_size=TEST_SIZE
    )

    # print(X_train.shape)
    # print(X_test.shape)
    # print(y_train.shape)
    # print(y_test.shape)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Check scalling
    # print(X_train.mean(axis=0))
    # print(X_train.std(axis=0))

    joblib.dump(scaler,X_SCALER_PATH)



    # y_scaler = StandardScaler()

    # y_train = y_scaler.fit_transform(
    #     y_train.values.reshape(-1, 1)
    # )

    # y_test = y_scaler.transform(
    #     y_test.values.reshape(-1, 1)
    # )

    # # Save Y Scaler
    # joblib.dump(y_scaler, Y_SCALER_PATH)

    return (
        X_train,
        X_test,
        y_train,
        y_test
    )