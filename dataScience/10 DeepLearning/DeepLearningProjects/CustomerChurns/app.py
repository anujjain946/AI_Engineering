from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import joblib

from config import *


# ==========================================
# Flask App
# ==========================================

app = Flask(__name__)


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
# Home Route
# ==========================================

@app.route("/")
def home():

    return "Customer Churn Prediction API is Running"


# ==========================================
# Prediction Route
# ==========================================

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:

        # ==================================
        # Get JSON Data
        # ==================================

        data = request.get_json()


        # ==================================
        # Numeric Features
        # ==================================

        age = float(
            data["age"]
        )

        tenure = float(
            data["tenure"]
        )

        usage_frequency = float(
            data["usage_frequency"]
        )

        support_calls = float(
            data["support_calls"]
        )

        payment_delay = float(
            data["payment_delay"]
        )

        total_spend = float(
            data["total_spend"]
        )

        last_interaction = float(
            data["last_interaction"]
        )


        # ==================================
        # Gender
        # ==================================

        gender = data["gender"].strip().lower()

        gender_male = (
            1 if gender == "male"
            else 0
        )


        # ==================================
        # Subscription Type
        # ==================================

        subscription_type = (
            data["subscription_type"]
            .strip()
            .lower()
        )

        subscription_premium = (
            1
            if subscription_type == "premium"
            else 0
        )

        subscription_standard = (
            1
            if subscription_type == "standard"
            else 0
        )


        # ==================================
        # Contract Length
        # ==================================

        contract_length = (
            data["contract_length"]
            .strip()
            .lower()
        )

        contract_monthly = (
            1
            if contract_length == "monthly"
            else 0
        )

        contract_quarterly = (
            1
            if contract_length == "quarterly"
            else 0
        )


        # ==================================
        # Create Sample
        # ==================================

        sample = np.array([[
            age,
            tenure,
            usage_frequency,
            support_calls,
            payment_delay,
            total_spend,
            last_interaction,
            gender_male,
            subscription_premium,
            subscription_standard,
            contract_monthly,
            contract_quarterly
        ]], dtype=float)


        # ==================================
        # Scaling
        # ==================================

        sample = scaler.transform(
            sample
        )


        # ==================================
        # Prediction
        # ==================================

        prediction = model.predict(
            sample,
            verbose=0
        )


        # ==================================
        # Probability
        # ==================================

        probability = float(
            prediction[0][0]
        )


        # ==================================
        # Result
        # ==================================

        if probability >= 0.5:

            result = "CUSTOMER WILL CHURN"

        else:

            result = "CUSTOMER WILL STAY"


        # ==================================
        # Response
        # ==================================

        return jsonify({

            "status": True,

            "prediction": result,

            "probability": round(
                probability,
                4
            )

        })


    except Exception as e:

        return jsonify({

            "status": False,

            "message": str(e)

        }), 400


# ==========================================
# Run Flask
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )