from flask import Flask, request, jsonify
from flask_cors import CORS  # Allows frontend to talk to backend
from predict import predictDemand

app = Flask(__name__)
CORS(app)  # Prevents browser cross-origin blocking blocks

@app.route("/")
def home():
    return jsonify({
        "message": "Demand Prediction API is active. Send a POST request to /predict."
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract JSON data safely
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        price = float(data.get("Price", 0))
        discount = float(data.get("Discount", 0))
        promotion = int(data.get("Promotion", 0))
        previous_sales = int(data.get("Previous_Sales", 0))
        day_of_week = int(data.get("DayOfWeek", 0))
        month = int(data.get("Month", 0))
        is_weekend = int(data.get("IsWeekend", 0))

        # Run prediction logic with all features
        demand = predictDemand(
            price,
            discount,
            promotion,
            previous_sales,
            day_of_week,
            month,
            is_weekend
        )

        return jsonify({
            "status": "success",
            "Demand might ": demand
        })

    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8081)
