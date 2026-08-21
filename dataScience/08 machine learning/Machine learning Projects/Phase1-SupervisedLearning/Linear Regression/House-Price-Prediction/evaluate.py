import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# =========================
# 1. Load Dataset
# =========================

DATA_PATH = "Housing.csv"

df = pd.read_csv(DATA_PATH)


# =========================
# 2. Select Features
# =========================

X = df[[
    "area",
    "bedrooms",
    "bathrooms"
]]

y = df["price"]


# =========================
# 3. Train/Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================
# 4. Load Trained Model
# =========================

model = joblib.load("model.pkl")


# =========================
# 5. Make Predictions
# =========================

y_pred = model.predict(X_test)


# =========================
# 6. Calculate Metrics
# =========================

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)


# =========================
# 7. Display Results
# =========================

print("=" * 50)
print("       HOUSE PRICE MODEL EVALUATION")
print("=" * 50)

print(f"MAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

print("=" * 50)