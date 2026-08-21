from flask import Flask, request, jsonify
from flask_cors import CORS
from predict import predictSale

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Sales Prediction API is active. Send a POST request to /predict."
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get JSON data
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No JSON data provided"
            }), 400

        # Extract input values
        TV = float(data.get("tv", 0))
        Radio = float(data.get("radio", 0))
        Newspaper = float(data.get("newspaper", 0))

        # Run prediction
        sales = predictSale(
            TV,
            Radio,
            Newspaper
        )

        return jsonify({
            "status": "success",
            "Sales might": round(sales, 1)
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )