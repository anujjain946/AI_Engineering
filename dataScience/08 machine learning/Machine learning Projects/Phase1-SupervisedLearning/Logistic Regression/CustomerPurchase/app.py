from flask import Flask, request, jsonify
from flask_cors import CORS

from predict import predictPurchased


app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "Adidas Prediction API is active",
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
        salary = data.get("salary")
       

        # Prediction
        purchased = predictPurchased(
            salary,
        )

        return jsonify({
            "status": "success",
            "predicted_purchased": purchased
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
    "salary": 50000
}


{
    "status": "success",
    "predicted_purchased": 1
}
'''
