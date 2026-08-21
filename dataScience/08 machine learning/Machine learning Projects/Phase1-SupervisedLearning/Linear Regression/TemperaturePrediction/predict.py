import joblib
import pandas as pd
from config import MODEL_PATH

model = joblib.load(MODEL_PATH)


def predictTemprature(Humidity,Pressure,WindSpeed,PreviousTemp,Day,Month,DayOfWeek):

    data = pd.DataFrame({
        "Humidity": [Humidity],
        "Pressure": [Pressure],
        "WindSpeed": [WindSpeed],
        "PreviousTemp": [PreviousTemp],
        "Day": [Day],
        "Month": [Month],
        "DayOfWeek": [DayOfWeek],
    })

    prediction = model.predict(data)

    print(f"Prediction is {prediction[0]}")

    return float(prediction[0])


# predictTemprature(67.88,1016.47,8.55,12.77,1,1,1)


