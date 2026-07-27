import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from config import *


def load_data():
    # Load Dataset
    df = pd.read_csv(DATASET_PATH)

    # Features
    X = df[["Area", "Bedrooms", "Bathrooms", "Floors", "Age"]]

    # Target
    y = df["Price"]

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
    joblib.dump(x_scaler, "models/x_scaler.pkl")

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
    joblib.dump(y_scaler, "models/y_scaler.pkl")

    return (
        X_train,
        X_test,
        y_train,
        y_test
    )