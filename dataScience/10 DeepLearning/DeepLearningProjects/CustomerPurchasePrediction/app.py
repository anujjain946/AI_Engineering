from flask import Flask, request, jsonify
import tensorflow as tf
import pandas as pd
import joblib

from config import MODEL_PATH, SCALER_PATH,COLUMNS_PATH

app = Flask(__name__)

# -----------------------------------
# Load Model and Scaler
# -----------------------------------

model = tf.keras.models.load_model(MODEL_PATH)

scaler = joblib.load(SCALER_PATH)
column_list = joblib.load(COLUMNS_PATH)


# -----------------------------------
# Home
# -----------------------------------

@app.route("/")
def home():
    return "Customer Purchase Prediction API is Running"


# -----------------------------------
# Prediction API
# -----------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get JSON data
        data = request.get_json()

        # -----------------------------------
        # Get Input Values
        # -----------------------------------

        age = float(data["age"])

        gender = data["gender"]

        marital_status = data["marital_status"]

        annual_income = float(
            data["annual_income"]
        )

        website_visits = float(
            data["website_visits"]
        )

        app_usage_hours = float(
            data["app_usage_hours"]
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
        # IMPORTANT
        # -----------------------------------
        # Training ke columns ke according
        # sample ko arrange karna zaroori hai.
        #
        # Agar aapne model_columns.pkl save
        # nahi kiya hai, to neeche manually
        # columns define kiye gaye hain.

      

        sample = sample.reindex(
            columns=column_list,
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

        probability = float(
            prediction[0][0]
        )

        # -----------------------------------
        # Result
        # -----------------------------------

        result = (
            "PURCHASE"
            if probability >= 0.5
            else "NO PURCHASE"
        )

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


# -----------------------------------
# Run Flask
# -----------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )