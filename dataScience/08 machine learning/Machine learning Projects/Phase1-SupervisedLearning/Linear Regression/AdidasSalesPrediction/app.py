from flask import Flask, request, jsonify
from flask_cors import CORS

from predict import predictSales


app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "Adidas Sales Prediction API is active",
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
        retailer = data.get("retailer")
        region = data.get("region")
        state = data.get("state")
        city = data.get("city")
        product = data.get("product")
        price_per_unit = float(data.get("price_per_unit", 0))
        units_sold = float(data.get("units_sold", 0))
        sales_method = data.get("sales_method")

        year = int(data.get("year"))
        month = int(data.get("month"))
        day = int(data.get("day"))
        day_of_week = int(data.get("day_of_week"))

        # Prediction
        sales = predictSales(
            retailer,
            region,
            state,
            city,
            product,
            price_per_unit,
            units_sold,
            sales_method,
            year,
            month,
            day,
            day_of_week
        )

        return jsonify({
            "status": "success",
            "predicted_sales": round(sales, 2)
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
    "retailer": "Foot Locker",
    "region": "Northeast",
    "state": "New York",
    "city": "New York",
    "product": "Men's Street Footwear",
    "price_per_unit": 50,
    "units_sold": 100,
    "sales_method": "Online",
    "year": 2021,
    "month": 8,
    "day": 15,
    "day_of_week": 6
}


{
    "status": "success",
    "predicted_sales": 7933
}
'''