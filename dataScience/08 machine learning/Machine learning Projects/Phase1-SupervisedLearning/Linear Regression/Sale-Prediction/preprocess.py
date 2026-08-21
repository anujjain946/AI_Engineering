import pandas as pd
import numpy as np
from config import DATASET_PATH,TEST_SIZE,RANDOM_STATE,MODEL_PATH
from sklearn.model_selection import train_test_split


# Create a method for load dataset and preprocess for dataset.
def loadDataSet():
    df = pd.read_csv(DATASET_PATH)

    # check null values
    # print(df.isnull().sum())
    # check Duplicate
    # print(df.duplicated().sum())
    # information
    # print(df.info())
    #descriptions
    # print(df.describe())

    X = df[['TV','Radio','Newspaper']]
    y =df['Sales']

    return train_test_split(
        X,
        y,
        test_size = TEST_SIZE,
        random_state = RANDOM_STATE
    )