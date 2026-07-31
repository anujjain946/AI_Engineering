import tensorflow as tf
import numpy as np
import pandas as pd
import joblib

from config import *

# ==============================
# Load Model & Scalers
# ==============================
model = tf.keras.models.load_model(MODEL_PATH)

x_scaler = joblib.load(X_SCALER_PATH)
y_scaler = joblib.load(Y_SCALER_PATH)

# ==============================
# User Input
# ==============================
housing_median_age = float(input("Housing Median Age : "))
total_rooms = float(input("Total Rooms : "))
total_bedrooms = float(input("Total Bedrooms : "))
population = float(input("Population : "))
households = float(input("Households : "))
median_income = float(input("Median Income : "))

# print("\nOcean Proximity Options")
# print("1. INLAND")
# print("2. ISLAND")
# print("3. NEAR BAY")
# print("4. NEAR OCEAN")
# print("5. <1H OCEAN")

# choice = int(input("Choose Option (1-5): "))

# # ==============================
# # One-Hot Encoding
# # (Modify according to your training columns)
# # ==============================

# inland = 0
# island = 0
# near_bay = 0
# near_ocean = 0

# # <1H OCEAN is assumed to be dropped (drop_first=True)

# if choice == 1:
#     inland = 1
# elif choice == 2:
#     island = 1
# elif choice == 3:
#     near_bay = 1
# elif choice == 4:
#     near_ocean = 1

# ==============================
# Create DataFrame
# Column order MUST match training data
# ==============================

sample = pd.DataFrame([{
    "housing_median_age": housing_median_age,
    "total_rooms": total_rooms,
    "total_bedrooms": total_bedrooms,
    "population": population,
    "households": households,
    "median_income": median_income,
    'ocean_proximity':3
}])

# ==============================
# Scale Features
# ==============================

sample_scaled = x_scaler.transform(sample)

# ==============================
# Prediction
# ==============================

prediction_scaled = model.predict(sample_scaled, verbose=0)

prediction = y_scaler.inverse_transform(prediction_scaled)

print("\n===================================")
print(f"Predicted House Price : ${prediction[0][0]:,.2f}")
print("===================================")