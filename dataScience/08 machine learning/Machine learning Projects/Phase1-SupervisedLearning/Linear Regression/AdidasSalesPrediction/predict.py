import joblib
import pandas as pd

from config import MODEL_PATH


# Load trained pipeline
model = joblib.load(MODEL_PATH)


def predictSales(
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
):

    data = pd.DataFrame({
        "Retailer": [retailer],
        "Region": [region],
        "State": [state],
        "City": [city],
        "Product": [product],
        "Price per Unit": [price_per_unit],
        "Units Sold": [units_sold],
        "Sales Method": [sales_method],
        "Year": [year],
        "Month": [month],
        "Day": [day],
        "DayOfWeek": [day_of_week]
    })

    prediction = model.predict(data)

    return float(prediction[0])


# Test prediction
sales = predictSales(
    "Foot Locker",
    "Northeast",
    "New York",
    "New York",
    "Men's Street Footwear",
    50,
    100,
    "Online",
    2021,
    8,
    15,
    6
)

print(f"Predicted Sales: {sales:.2f}")