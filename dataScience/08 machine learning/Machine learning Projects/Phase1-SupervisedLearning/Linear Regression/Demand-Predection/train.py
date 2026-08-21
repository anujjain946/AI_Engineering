import joblib
from preprocess import loadDataset
from config import MODEL_PATH
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Todo
# 1. Split Dataset

X_train, X_test, y_train, y_test = loadDataset()


# 2. pipeline : SimpleImputer,StandardScaler,LinearRegression
pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler()),
    ("regressor", LinearRegression())
])


# 3.Train model
pipeline.fit(
    X_train,
    y_train
)

# 4. Save model
joblib.dump(pipeline, MODEL_PATH)

print("Model save successfully")






