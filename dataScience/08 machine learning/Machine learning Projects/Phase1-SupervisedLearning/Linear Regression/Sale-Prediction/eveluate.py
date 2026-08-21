import joblib
import pandas as pd
import numpy as np

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from config import MODEL_PATH
from preprocess import loadDataSet

# =========================
# 1. Train Test Split
# =========================
X_train, X_test, y_train, y_test = loadDataSet()

# =========================
# 2. Load Model
# =========================
model = joblib.load(MODEL_PATH)


# =========================
# 3. Prediction
# =========================
y_pred = model.predict(X_test)


# =========================
# 4. Evaluation Metrics
# =========================
mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)


# =========================
# 7. Print Results
# =========================
print("=" * 50)
print("       SALES PREDICTION MODEL")
print("             EVALUATION")
print("=" * 50)

print(f"MAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

print("=" * 50)




