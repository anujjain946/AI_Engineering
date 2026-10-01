import joblib


# Load model
model = joblib.load("model/svm_model.pkl")

# Load scaler
scaler = joblib.load("model/scaler.pkl")


# New flower
flower = [[
    5.1,   # sepal length
    3.5,   # sepal width
    1.4,   # petal length
    0.2    # petal width
]]


# Scale input
flower_scaled = scaler.transform(flower)


# Prediction
prediction = model.predict(flower_scaled)


classes = [
    "setosa",
    "versicolor",
    "virginica"
]
print("Predicted:", prediction[0])
print("Predicted flower:", classes[prediction[0]])