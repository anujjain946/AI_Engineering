from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
import joblib
from config import  MODEL_PATH
from preprocess import loadDataset



# Split data
X_train, X_test, y_train, y_test = loadDataset()

# fixed acidity	volatile acidity	citric acid	residual sugar	chlorides	free sulfur dioxide	total sulfur dioxide	density	pH	sulphates	alcohol	quality	Id




#Pipeline




pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler()),
    ("regressor", LinearRegression())
])



# Train model
pipeline.fit(X_train, y_train)

# Save model
joblib.dump(pipeline, MODEL_PATH)

print("Model Saved Successfully")