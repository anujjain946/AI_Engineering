from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import joblib

from config import MODEL_PATH, X_SCALER_PATH


# ==========================================
# Flask App
# ==========================================

app = Flask(__name__)


# ==========================================
# Load Model and Scaler
# ==========================================

model = tf.keras.models.load_model(
    MODEL_PATH
)

scaler = joblib.load(
    X_SCALER_PATH
)


# ==========================================
# Home API
# ==========================================

@app.route("/")
def home():

    return "Wine Quality Prediction API is Running"


# ==========================================
# Prediction API
# ==========================================

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:

        # ----------------------------------
        # Get JSON Data
        # ----------------------------------

        data = request.get_json()


        # ----------------------------------
        # Get Input Values
        # ----------------------------------

        fixed_acidity = float(
            data["fixed_acidity"]
        )

        volatile_acidity = float(
            data["volatile_acidity"]
        )

        citric_acid = float(
            data["citric_acid"]
        )

        residual_sugar = float(
            data["residual_sugar"]
        )

        chlorides = float(
            data["chlorides"]
        )

        free_sulfur_dioxide = float(
            data["free_sulfur_dioxide"]
        )

        total_sulfur_dioxide = float(
            data["total_sulfur_dioxide"]
        )

        density = float(
            data["density"]
        )

        ph = float(
            data["ph"]
        )

        sulphates = float(
            data["sulphates"]
        )

        alcohol = float(
            data["alcohol"]
        )


        # ----------------------------------
        # Create Sample
        # ----------------------------------

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


        # ----------------------------------
        # Scaling
        # ----------------------------------

        sample = scaler.transform(
            sample
        )


        # ----------------------------------
        # Prediction
        # ----------------------------------

        prediction = model.predict(
            sample,
            verbose=0
        )


        # ----------------------------------
        # Probability
        # ----------------------------------

        probability = float(
            prediction[0][0]
        )


        # ----------------------------------
        # Result
        # ----------------------------------

        result = (
            "GOOD WINE"
            if probability >= 0.5
            else "BAD WINE"
        )


        # ----------------------------------
        # Response
        # ----------------------------------

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