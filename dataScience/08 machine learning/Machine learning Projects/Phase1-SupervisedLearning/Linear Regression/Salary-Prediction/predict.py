import joblib
import pandas as pd
from config import MODEL_PATH

model = joblib.load(MODEL_PATH)


def predictSalary(experience):

    data = pd.DataFrame({
        "Experience": [experience]
    })

    prediction = model.predict(data)

    # print(f"Prediction is {prediction[0]}")

    return float(prediction[0])


# predictSalary(5)