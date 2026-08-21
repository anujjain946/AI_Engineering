import joblib
import pandas as pd

from config import MODEL_PATH


# Load trained pipeline
model = joblib.load(MODEL_PATH)

# dataset columns :age sex	bmi	children	smoker	region	charges
def predictIsuranceCost(
    age,  
    sex,
    bmi,
    children,
    smoker,
    region
):

    data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region],
    })


    prediction = model.predict(data)

    return float(prediction[0])


# Test prediction
predict = predictIsuranceCost(18,'male',33.77,1,'1','southwest')
# 19	female	27.9	0	yes	southwest
# 18	male	33.77	1	no	southeast	1725.5523

print(f"Predicted Insurance Cost ₹:{predict:.2f}")