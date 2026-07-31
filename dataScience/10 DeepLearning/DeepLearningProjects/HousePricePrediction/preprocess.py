from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
from config import *
import pandas as pd
import joblib


def load_data():
    # Load Dataset
    df = pd.read_csv(DATASET_PATH)
    # print(df.columns)

    # Features
    # X = df[["Area", "Bedrooms", "Bathrooms", "Floors", "Age"]]
    
    X = df[['housing_median_age', 'total_rooms','total_bedrooms', 'population', 'households', 'median_income',
       'ocean_proximity']]


    # -----------------------------
    # preprocess Data
    # -----------------------------

    le = LabelEncoder()
    X["ocean_proximity"] = le.fit_transform(df["ocean_proximity"])

    # print(df[])
    # print(X)
    # print(X.head())
    # print(X.isnull().sum())
    # print(X.info())
    # print(X[X.duplicated()])
    # print(X.describe())
    X["total_bedrooms"] = X["total_bedrooms"].fillna(X["total_bedrooms"].median())

    # -----------------------------
    # plot
    # -----------------------------

    # import matplotlib.pyplot as plt
    # df.hist(figsize=(10,5))
    # plt.show()

   

     # Target
    # y = df["result"]
    y = df["median_house_value"]

    # -----------------------------
    # Train Test Split
    # -----------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

    # -----------------------------
    # Scale Features (X)
    # -----------------------------
    x_scaler = StandardScaler()

    X_train = x_scaler.fit_transform(X_train)
    X_test = x_scaler.transform(X_test)

    # Save X Scaler
    joblib.dump(x_scaler,X_SCALER_PATH)

    # -----------------------------
    # Scale Target (y)
    # -----------------------------
    y_scaler = StandardScaler()

    y_train = y_scaler.fit_transform(
        y_train.values.reshape(-1, 1)
    )

    y_test = y_scaler.transform(
        y_test.values.reshape(-1, 1)
    )



    # Save Y Scaler
    joblib.dump(y_scaler,Y_SCALER_PATH)

    return (
        X_train,
        X_test,
        y_train,
        y_test
    )