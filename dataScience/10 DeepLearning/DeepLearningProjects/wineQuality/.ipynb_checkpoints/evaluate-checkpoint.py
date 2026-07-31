import tensorflow as tf

from preprocess import load_data

from config import *

X_train, X_test, y_train, y_test = load_data()

model = tf.keras.models.load_model(MODEL_PATH)

loss, accuracy = model.evaluate(

    X_test,

    y_test

)

print("Loss :", loss)

print("Accuracy :", accuracy)