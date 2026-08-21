import joblib
import pandas as pd
from config import MODEL_PATH

model = joblib.load(MODEL_PATH)


def predictCarPrice(Year,Selling_Price,Kms_Driven,Owner):	

    data = pd.DataFrame({
        "Year": [Year],
        "Selling_Price": [Selling_Price],
        "Kms_Driven": [Kms_Driven],
        "Owner": [Owner],
        
    })

    prediction = model.predict(data)

    print(f"Prediction is {prediction[0]}")

    return float(prediction[0])


predictCarPrice(2014,3.35,27000,0)


