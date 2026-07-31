import tensorflow as tf
import numpy as np
import pandas as pd
import joblib

from config import MODEL_PATH, SCALER_PATH, COLUMNS_PATH


# -----------------------------------
# Load Model, Scaler and Columns
# -----------------------------------

model = tf.keras.models.load_model(MODEL_PATH)

scaler = joblib.load(SCALER_PATH)

model_columns = joblib.load(COLUMNS_PATH)


# -----------------------------------
# Customer Input
# -----------------------------------

age = float(input("Age : "))

gender = input("Gender (Male/Female) : ")

marital_status = input(
    "Marital Status (Single/Married/Divorced) : "
)

annual_income = float(
    input("Annual Income : ")
)

website_visits = float(
    input("Website Visits : ")
)

app_usage_hours = float(
    input("App Usage Hours : ")
)


# -----------------------------------
# Create DataFrame
# -----------------------------------

sample = pd.DataFrame([{
    "Age": age,
    "Gender": gender,
    "MaritalStatus": marital_status,
    "AnnualIncome": annual_income,
    "WebsiteVisits": website_visits,
    "AppUsageHours": app_usage_hours
}])


# -----------------------------------
# One-Hot Encoding
# -----------------------------------

sample = pd.get_dummies(
    sample,
    columns=[
        "Gender",
        "MaritalStatus"
    ],
    drop_first=True,
    dtype=int
)


# -----------------------------------
# Match Training Columns
# -----------------------------------

sample = sample.reindex(
    columns=model_columns,
    fill_value=0
)


# -----------------------------------
# Scaling
# -----------------------------------

sample = scaler.transform(sample)


# -----------------------------------
# Prediction
# -----------------------------------

prediction = model.predict(
    sample,
    verbose=0
)

probability = prediction[0][0]


# -----------------------------------
# Result
# -----------------------------------

print("\n==============================")

if probability >= 0.5:

    print("Prediction : CUSTOMER WILL PURCHASE")

else:

    print("Prediction : CUSTOMER WILL NOT PURCHASE")


print(
    f"Probability : {probability * 100:.2f}%"
)

print("==============================")