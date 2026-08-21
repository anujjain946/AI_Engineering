import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from config import DATASET_PATH, TEST_SIZE, RANDOM_STATE

# fixed acidity	volatile acidity	citric acid	residual sugar	chlorides	free sulfur dioxide	total sulfur dioxide	density	pH	sulphates	alcohol	quality	Id

def loadDataset():

    df = pd.read_csv(DATASET_PATH)

    # remove target value
    X = df.drop(columns=["quality","Id"])
    # check shape
    # print(X.shape)
    # print(df.isnull().sum())
    # print(df.duplicated().sum())
    
    y = df["quality"]
    # print(y.shape) 

    return train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

loadDataset()
