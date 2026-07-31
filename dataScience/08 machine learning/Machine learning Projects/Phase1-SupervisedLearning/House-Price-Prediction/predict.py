import joblib
import pandas as pd

model = joblib.load("model/model.pkl")

def predict_price(area, bedrooms, bathrooms):

    data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms]
    })

    prediction = model.predict(data)

    return prediction[0]