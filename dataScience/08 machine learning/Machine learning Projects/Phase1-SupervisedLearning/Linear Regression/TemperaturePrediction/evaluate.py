from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from preprocess import loadDataset
from config import MODEL_PATH
import joblib
import pandas as pd
import numpy as np


# load dataset 
X_train,X_test,y_train,y_test = loadDataset()
model = joblib.load(MODEL_PATH)
y_pred = model.predict(X_test)

print(y_pred)

# =========================
# 6. Evaluation Metrics
# =========================

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)


# =========================
# . Print Results
# =========================

print("=" * 50)
print("       TEMPRATURE PREDICTION MODEL")
print("             EVALUATION")
print("=" * 50)

print(f"MAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

print("=" * 50)








