import tensorflow as tf

from preprocess import load_data

from config import *

X_train, X_test, y_train, y_test = load_data()

model = tf.keras.models.load_model(MODEL_PATH)
# model = tf.keras.models.load_model("models/best_wine_model.keras")

loss, accuracy, precision, recall, auc = model.evaluate(
    X_test,
    y_test,
    verbose=1
)

print("Loss      :", loss)
print("Accuracy  :", accuracy)
print("Precision :", precision)
print("Recall    :", recall)
print("AUC       :", auc)