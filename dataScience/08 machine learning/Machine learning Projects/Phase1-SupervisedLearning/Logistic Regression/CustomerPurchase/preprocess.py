import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from config import DATASET_PATH, TEST_SIZE, RANDOM_STATE


def loadDataset():
 
    df = pd.read_csv(DATASET_PATH)
    '''
        # EDA
        print(df.shape)
        print("\n")
        print(df.info(5))
        print("\n")
        print(df.columns)
        print("\n")
        print('Missing Values\n')
        print(df.isnull().sum())
        print('Check Duplicate\n')
        print(df.duplicated().sum())
        df = df.drop_duplicates()
        print(df.duplicated().sum())
        print("\n")
        print("Age Mean:", df["Age"].mean())
        print("\n")
        print("Age Median:", df["Age"].median())
        print("\n")
        df["Age"] = df["Age"].fillna(
            df["Age"].median()
        )
        print("\n")
        print(df.isnull().sum())

        print("\n")
        print("Salary Mean:", df["Salary"].mean())
        print("\n")
        print("Age Median:", df["Salary"].median())
        print("\n")
        df["Salary"] = df["Salary"].fillna(
            df["Salary"].median()
        )

        print("\n")
        print(df.isnull().sum())
        '''
    df["Salary"] = df["Salary"].fillna(
            df["Salary"].median()
        )
    # print("\n")
    # print(df.columns)

    X = df[['Salary']]
    y = df['Purchased']

    # print("X shape:", X.shape)

    return train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )

# X_train, X_test, y_train, y_test = load_data()

# print("X_train shape:", X_train.shape)
# print("X_test shape:", X_test.shape)


# loadDataset()