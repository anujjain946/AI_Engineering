import tensorflow as tf

import numpy as np

import joblib

from config import *

model = tf.keras.models.load_model(MODEL_PATH)

scaler = joblib.load(SCALER_PATH)

hours = float(input("Hours Studied : "))

attendance = float(input("Attendance : "))

assignment = float(input("Assignment Marks : "))

sample = np.array([[

    hours,

    attendance,

    assignment

]])

sample = scaler.transform(sample)

prediction = model.predict(sample)

if prediction[0][0] >= 0.5:

    print("\nPrediction : PASS")

else:

    print("\nPrediction : FAIL")