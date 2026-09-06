import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from config import DATASET_PATH, TEST_SIZE, RANDOM_STATE


def loadDataset():
 
    df = pd.read_csv(DATASET_PATH)
    
        # EDA


    # X = df[['Salary']]
    # y = df['Purchased']

    # # print("X shape:", X.shape)

    # return train_test_split(
    #     X,
    #     y,
    #     test_size=TEST_SIZE,
    #     random_state=RANDOM_STATE,
    #     stratify=y
    # )

# X_train, X_test, y_train, y_test = load_data()

# print("X_train shape:", X_train.shape)
# print("X_test shape:", X_test.shape)


# loadDataset()