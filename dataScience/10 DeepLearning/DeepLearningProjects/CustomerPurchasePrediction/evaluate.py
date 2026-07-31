import tensorflow as tf

from preprocess import load_data

from config import *


# X_train, X_test, y_train, y_test = load_data()

# model = tf.keras.models.load_model(MODEL_PATH)

# loss, accuracy = model.evaluate(

#     X_test,

#     y_test

# )

# print("Loss :", loss)

# print("Accuracy :", accuracy)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix
)

# Load test data
X_train, X_test, y_train, y_test = load_data()

# Load trained model
model = tf.keras.models.load_model(MODEL_PATH)

# --------------------------------
# Basic Keras Evaluation
# --------------------------------
loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=1
)

print("\n==============================")
print("Keras Evaluation")
print("==============================")
print(f"Loss     : {loss:.4f}")
print(f"Accuracy : {accuracy:.4f}")
print(f"Accuracy : {accuracy * 100:.2f}%")

# --------------------------------
# Prediction Probability
# --------------------------------
y_pred_prob = model.predict(
    X_test,
    verbose=0
).ravel()

# --------------------------------
# Convert Probability to 0/1
# --------------------------------
y_pred = (y_pred_prob >= 0.5).astype(int)

# --------------------------------
# Classification Metrics
# --------------------------------
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_prob)

print("\n==============================")
print("Classification Metrics")
print("==============================")

print(f"Accuracy  : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")
print(f"AUC       : {auc:.4f}")

# --------------------------------
# Classification Report
# --------------------------------
print("\n==============================")
print("Classification Report")
print("==============================")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=["No Purchase", "Purchase"]
    )
)

# --------------------------------
# Confusion Matrix
# --------------------------------
print("\n==============================")
print("Confusion Matrix")
print("==============================")

cm = confusion_matrix(y_test, y_pred)

print(cm)