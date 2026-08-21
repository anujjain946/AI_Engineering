from flask import Flask, request, jsonify
from flask_cors import CORS  # Allows frontend to talk to backend
from predict import predictTemprature

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

        Humidity = float(data.get("Humidity", 0))
        Pressure = float(data.get("Pressure", 0))
        WindSpeed = float(data.get("WindSpeed", 0))
        PreviousTemp = float(data.get("PreviousTemp", 0))
        Day = float(data.get("Day", 0))
        Month = float(data.get("Month", 0))
        DayOfWeek = float(data.get("DayOfWeek", 0))
        

        # Run prediction logic
        temprature = predictTemprature(Humidity,Pressure,WindSpeed,PreviousTemp,Day,Month,DayOfWeek)

        return jsonify({
            "status": "success",
            "Salary might ": temprature
        })

    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8081)
