import pandas as pd
from config import DATASET_PATH,TEST_SIZE,RANDOM_STATE
from sklearn.model_selection import train_test_split

# Todo : Create a fucntion for laod dataset and EDA 
def loadDataset():

    # load dataset 
    df = pd.read_csv(DATASET_PATH)

    # EDA for Dataset.

    # print(df.head())
    # print(df.isnull().sum())
    # print(df.duplicated().sum())
    # print(df.info())
    # print(df.describe())


#Todo :  
#       1. Remove colomn Date.
#       2. use simpleSaclling.

    # X = df.drop(columns=['Date'])  
    X = df[['Price', 'Discount', 'Promotion', 'Previous_Sales',
        'DayOfWeek', 'Month', 'IsWeekend']]
    # print(x.head())
    # print(X.shape)

    # target
    y = df['Demand']

    # print(y.shape)
    return  train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

loadDataset()
 