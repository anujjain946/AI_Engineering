import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from config import DATASET_PATH, TEST_SIZE, RANDOM_STATE


def load_data():
 
    df = pd.read_csv(DATASET_PATH)

    df['Experience'] = np.random.randint(1, 20, size=len(df))

    df['Salary'] = (
        30000
        + df['Experience'] * 6000
        + np.random.randint(-5000, 5000, size=len(df))
    )

    X = df[['Experience']]
    y = df['Salary']



    return train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

# X_train, X_test, y_train, y_test = load_data()

# print("X_train shape:", X_train.shape)
# print("X_test shape:", X_test.shape)

