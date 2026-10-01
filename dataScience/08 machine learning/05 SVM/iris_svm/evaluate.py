import joblib

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


iris = load_iris()

X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


model = joblib.load("model/svm_model.pkl")
scaler = joblib.load("model/scaler.pkl")


X_test_scaled = scaler.transform(X_test)

y_pred = model.predict(X_test_scaled)


print("Accuracy:")
print(accuracy_score(y_test, y_pred))


print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)


print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))