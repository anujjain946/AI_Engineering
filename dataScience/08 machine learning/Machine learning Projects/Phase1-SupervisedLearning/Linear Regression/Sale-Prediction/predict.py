import joblib
import pandas as pd
from config import MODEL_PATH

# Load model
model = joblib.load(MODEL_PATH)


def predictSale(TV, Radio, Newspaper):

    data = pd.DataFrame({
        "TV": [TV],
        "Radio": [Radio],
        "Newspaper": [Newspaper]
    })

    prediction = model.predict(data)

    return  float(prediction[0])

    
    # print(f"Sales might be: {prediction[0]:.2f}")


# predictSale(230.1, 37.8, 69.2)