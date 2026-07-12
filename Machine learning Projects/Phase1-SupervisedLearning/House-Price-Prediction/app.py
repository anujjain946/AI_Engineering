from flask import Flask, request, jsonify
from flask_cors import CORS  # Allows frontend to talk to backend
from predict import predict_price

app = Flask(__name__)
CORS(app)  # Prevents browser cross-origin blocking blocks

@app.route("/")
def home():
    return jsonify({
        "message": "House Price Prediction API is active. Send a POST request to /predict."
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract JSON data safely
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        area = float(data.get("area", 0))
        bedrooms = int(data.get("bedrooms", 0))
        bathrooms = int(data.get("bathrooms", 0))

        # Run prediction logic
        price = predict_price(area, bedrooms, bathrooms)

        return jsonify({
            "status": "success",
            "predicted_price": price
        })

    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
