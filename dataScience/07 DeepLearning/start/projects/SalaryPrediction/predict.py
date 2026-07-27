import tensorflow as tf
import numpy as np
import joblib

from config import *

# Load Model
model = tf.keras.models.load_model(MODEL_PATH)

# Load Scalers
x_scaler = joblib.load("models/x_scaler.pkl")
y_scaler = joblib.load("models/y_scaler.pkl")

# User Input
Experience = float(input("Experience(Years)"))


# Create Input Array
sample = np.array([[
    Experience
]])

# Scale Features
sample = x_scaler.transform(sample)

# Predict (Scaled Price)
prediction = model.predict(sample, verbose=0)

# Convert Back to Actual Price
price = y_scaler.inverse_transform(prediction)

print("\n========== Salary Prediction ==========")
print(f"Predicted Salary : ₹{price[0][0]:,.2f}")
print("============================================")