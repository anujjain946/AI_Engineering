import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from config import DATASET_PATH, TEST_SIZE, RANDOM_STATE


def loadDataset():

    df = pd.read_csv(DATASET_PATH)

    # remove target value
    X = df.drop(columns="Performance Index")
    # check shape
    # print(X.shape)
    
    y = df["Performance Index"]
    # print(y.shape) 

    return train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

# loadDataset()
