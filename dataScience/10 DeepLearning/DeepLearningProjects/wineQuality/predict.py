import tensorflow as tf
import numpy as np
import joblib

from config import *


# ==========================================
# Load Model
# ==========================================

model = tf.keras.models.load_model(
    MODEL_PATH
)


# ==========================================
# Load Scaler
# ==========================================

scaler = joblib.load(
    X_SCALER_PATH
)


# ==========================================
# User Input
# ==========================================

fixed_acidity = float(
    input("Fixed Acidity : ")
)

volatile_acidity = float(
    input("Volatile Acidity : ")
)

citric_acid = float(
    input("Citric Acid : ")
)

residual_sugar = float(
    input("Residual Sugar : ")
)

chlorides = float(
    input("Chlorides : ")
)

free_sulfur_dioxide = float(
    input("Free Sulfur Dioxide : ")
)

total_sulfur_dioxide = float(
    input("Total Sulfur Dioxide : ")
)

density = float(
    input("Density : ")
)

ph = float(
    input("pH : ")
)

sulphates = float(
    input("Sulphates : ")
)

alcohol = float(
    input("Alcohol : ")
)


# ==========================================
# Create Sample
# ==========================================

sample = np.array([[
    fixed_acidity,
    volatile_acidity,
    citric_acid,
    residual_sugar,
    chlorides,
    free_sulfur_dioxide,
    total_sulfur_dioxide,
    density,
    ph,
    sulphates,
    alcohol
]])


# ==========================================
# Scaling
# ==========================================

sample = scaler.transform(sample)


# ==========================================
# Prediction
# ==========================================

prediction = model.predict(
    sample,
    verbose=0
)


probability = prediction[0][0]


# ==========================================
# Result
# ==========================================

if probability >= 0.5:

    print("\nPrediction : GOOD WINE")

else:

    print("\nPrediction : BAD WINE")


print(
    "Probability :",
    f"{probability * 100:.2f}%"
)