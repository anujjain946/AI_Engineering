from flask import Flask, request, jsonify
from flask_cors import CORS  # Allows frontend to talk to backend
from predict import predictSalary

app = Flask(__name__)
CORS(app)  # Prevents browser cross-origin blocking blocks

@app.route("/")
def home():
    return jsonify({
        "message": "Salary Prediction API is active. Send a POST request to /predict."
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract JSON data safely
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        experiance = float(data.get("experiance", 0))
        

        # Run prediction logic
        salary = predictSalary(experiance)

        return jsonify({
            "status": "success",
            "Salary might ": salary
        })

    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8081)
