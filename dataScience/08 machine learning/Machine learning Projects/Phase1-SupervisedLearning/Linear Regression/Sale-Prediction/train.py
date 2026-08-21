from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib
from config import  MODEL_PATH
from preprocess import loadDataSet

X_train, X_test, y_train, y_test = loadDataSet()

pipeline = Pipeline(
    [
        ("imputer",SimpleImputer(strategy="mean")),
        ("scaler",StandardScaler()),
        ("regressor", LinearRegression())

    ]
)

# Train model
pipeline.fit(
    X_train,
    y_train
)

# Save model
joblib.dump(pipeline, MODEL_PATH)

print("Model Saved Successfully")



