import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

import joblib

from config import *

def load_data():

    df = pd.read_csv(DATASET_PATH)

    X = df[['hours','attendance','assignment']]

    y = df['result']

    scaler = StandardScaler()

    X = scaler.fit_transform(X)

    joblib.dump(scaler, SCALER_PATH)

    return train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )