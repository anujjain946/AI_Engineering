from config import MODEL_PATH
from preprocess import loadDataset
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

# split dataset
X_train,X_test,y_train,y_test = loadDataset()

pipeline = Pipeline([
    ("imputer",SimpleImputer(strategy="mean")),
    ("scaler",StandardScaler()),
    ("regressor",LinearRegression())
])

# X_train = pipeline.fit_transform(X_train)
# X_test = pipeline.transform(X_test)

# train model
pipeline.fit(
    X_train,
    y_train
)

# dump joblib
joblib.dump(pipeline,MODEL_PATH)

print("Model save sucessfully.")