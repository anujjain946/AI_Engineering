import joblib
import pandas as pd

from config import MODEL_PATH


# Load trained pipeline
model = joblib.load(MODEL_PATH)


def predictPurchased(salary):

    data = pd.DataFrame({
        "Salary": [salary]
    })

    prediction = model.predict(data)

    return prediction[0]


# Test prediction
purchased = predictPurchased(
    50000
)

print(f"Predicted Purchase: {purchased  }")