import joblib
import pandas as pd

from config import MODEL_PATH


# Load trained pipeline
model = joblib.load(MODEL_PATH)

# # fixed acidity	volatile acidity	citric acid	residual sugar	chlorides	free sulfur dioxide	total sulfur dioxide	density	pH	sulphates	alcohol
def predictWineQuality(
    fixed_acidity,
    volatile_acidity,  
    citric_acid,
    bmresidual_sugari,
    chlorides,
    free_sulfur_dioxide,
    total_sulfur_dioxide,
    density,
    pH,
    sulphates,
    alcohol
):

    data = pd.DataFrame({
        "fixed acidity": [fixed_acidity],
        "volatile acidity": [volatile_acidity],
        "citric acid": [citric_acid],
        "residual sugar": [bmresidual_sugari],
        "chlorides": [chlorides],
        "free sulfur dioxide": [free_sulfur_dioxide],
        "total sulfur dioxide": [total_sulfur_dioxide],
        "density": [density],
        "pH": [pH],
        "sulphates": [sulphates],
        "alcohol": [alcohol],
    })


    prediction = model.predict(data)

    return float(prediction[0])


# Test prediction
predict = predictWineQuality(
    7.4,       # fixed_acidity
    0.70,      # volatile_acidity
    0.00,      # citric_acid
    1.9,       # residual_sugar
    0.076,     # chlorides
    11,        # free_sulfur_dioxide
    34,        # total_sulfur_dioxide
    0.9978,    # density
    3.51,      # pH
    0.56,      # sulphates
    9.4        # alcohol
)

print(f"Predicted Wine Quality ₹:{predict:.2f}")