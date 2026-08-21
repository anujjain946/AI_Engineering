# Todo : 
# 1. load model
# 2. Create a method for prediction.
# 3. 

import joblib
import pandas as pd
from config import MODEL_PATH

model = joblib.load(MODEL_PATH)

def predictDemand(
    Price,
    Discount,
    Promotion,
    Previous_Sales,
    DayOfWeek,
    Month,
    IsWeekend
):

    data = pd.DataFrame({
        "Price": [Price],
        "Discount": [Discount],
        "Promotion": [Promotion],
        "Previous_Sales": [Previous_Sales],
        "DayOfWeek": [DayOfWeek],
        "Month": [Month],
        "IsWeekend": [IsWeekend]
    })

    prediction = model.predict(data)

    return float(prediction[0])

prediction = predictDemand(
    500,
    10,
    1,
    120,
    2,
    8,
    0
)

print(f"Predicted Demand: {prediction:.2f}")