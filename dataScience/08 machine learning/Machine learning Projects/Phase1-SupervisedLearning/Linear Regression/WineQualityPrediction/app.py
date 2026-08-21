from flask import Flask, request, jsonify
from flask_cors import CORS

from predict import predictWineQuality


app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "Wine Quality Prediction API is active",
        "endpoint": "POST /predict"
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get JSON data
        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "No JSON data provided"
            }), 400


# dataset columns :age sex	bmi	children	smoker	region	charges
        # Get input values
        fixed_acidity = data.get("fixed_acidity")
        volatile_acidity = data.get("volatile_acidity")
        citric_acid = data.get("citric_acid")
        residual_sugar = data.get("residual_sugar")
        chlorides = data.get("chlorides")
        free_sulfur_dioxide = data.get("free_sulfur_dioxide")
        total_sulfur_dioxide = data.get("total_sulfur_dioxide")
        density = data.get("density")
        pH = data.get("pH")
        sulphates = data.get("sulphates")
        alcohol = data.get("alcohol")


        # Prediction
        Prediction = predictWineQuality(
            fixed_acidity,
            volatile_acidity,
            citric_acid,
            residual_sugar,
            chlorides,
            free_sulfur_dioxide,
            total_sulfur_dioxide,
            density,
            pH,
            sulphates,
            alcohol
        )
        return jsonify({
            "status": "success",
            "Wine Quality Predict": round(Prediction, 2)
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5001
    )


'''
{
  "fixed_acidity": 7.4,
  "volatile_acidity": 0.7,
  "citric_acid": 0.0,
  "residual_sugar": 1.9,
  "chlorides": 0.076,
  "free_sulfur_dioxide": 11,
  "total_sulfur_dioxide": 34,
  "density": 0.9978,
  "pH": 3.51,
  "sulphates": 0.56,
  "alcohol": 9.4
}
'''