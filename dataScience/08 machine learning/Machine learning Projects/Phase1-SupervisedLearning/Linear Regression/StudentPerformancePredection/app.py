from flask import Flask, request, jsonify
from flask_cors import CORS

from predict import predictStudenPerformence


app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "Student Perform Prediction API is active",
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


        # Get input values
        ExtracurricularActivities = data.get("ExtracurricularActivities")
        HoursStudied = data.get("HoursStudied")
        PreviousScores = data.get("PreviousScores")
        SleepHours = data.get("SleepHours")
        SampleQuestionPapersPracticed = data.get("SampleQuestionPapersPracticed")
        

        

        # Prediction
        Prediction = predictStudenPerformence(
            ExtracurricularActivities,  
            HoursStudied,
            PreviousScores,
            SleepHours,
            SampleQuestionPapersPracticed
        )

        return jsonify({
            "status": "success",
            "Student predicte Performence": round(Prediction, 2)
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
  "ExtracurricularActivities": "Yes",
  "HoursStudied": 7,
  "PreviousScores": 85,
  "SleepHours": 8,
  "SampleQuestionPapersPracticed": 6
}
'''