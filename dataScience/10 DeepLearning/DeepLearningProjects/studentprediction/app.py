from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import joblib
from config import MODEL_PATH, SCALER_PATH

app = Flask(__name__)

# Load Model and Scaler
model = tf.keras.models.load_model(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


@app.route("/")
def home():
    return "Student Prediction API is Running"


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        hours = float(data["hours"])
        attendance = float(data["attendance"])
        assignment = float(data["assignment"])

        sample = np.array([[hours, attendance, assignment]])

        sample = scaler.transform(sample)

        prediction = model.predict(sample)

        probability = float(prediction[0][0])

        result = "PASS" if probability >= 0.5 else "FAIL"

        return jsonify({
            "status": True,
            "prediction": result,
            "probability": round(probability, 4)
        })

    except Exception as e:
        return jsonify({
            "status": False,
            "message": str(e)
        })


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)