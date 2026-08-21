from flask import Flask, request, jsonify
from flask_cors import CORS  # Allows frontend to talk to backend
from predict import predictCarPrice

app = Flask(__name__)
CORS(app)  # Prevents browser cross-origin blocking blocks

@app.route("/")
def home():
    return jsonify({
        "message": "Temprature Prediction API is active. Send a POST request to /predict."
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract JSON data safely
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        

        Year = float(data.get("Year", 0))
        Selling_Price = float(data.get("Selling_Price", 0))
        Kms_Driven = float(data.get("Kms_Driven", 0))
        Owner = float(data.get("Owner", 0))
        

        # Run prediction logic
        carPrice = predictCarPrice(Year,Selling_Price,Kms_Driven,Owner)

        return jsonify({
            "status": "success",
            "Salary might ": carPrice
        })

    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8081)
