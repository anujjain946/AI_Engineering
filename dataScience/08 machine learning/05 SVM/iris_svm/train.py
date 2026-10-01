import os
import pandas as pd
import joblib

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# -----------------------------
# 1. Load Dataset
# -----------------------------

iris = load_iris()

X = iris.data
y = iris.target

print("Features:")
print(iris.feature_names)

print("\nClasses:")
print(iris.target_names)


# -----------------------------
# 2. DataFrame
# -----------------------------

df = pd.DataFrame(
    X,
    columns=iris.feature_names
)

df["target"] = y

print("\nDataset:")
print(df.head())


# -----------------------------
# 3. Train Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# -----------------------------
# 4. Scaling
# -----------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# -----------------------------
# 5. SVM Model
# -----------------------------

model = SVC(
    kernel="linear",
    C=1.0
)

# RBF
# model = SVC(
#     kernel="rbf",
#     C=1.0,
#     gamma="scale"
# )

# polynomial
# model = SVC(
#     kernel="poly",
#     C=1.0,
#     degree=3
# )

# sigmoid
# model = SVC(
#     kernel="sigmoid",
#     C=1.0,
#     gamma="scale"
# )

model.fit(X_train_scaled, y_train)


# -----------------------------
# 6. Prediction
# -----------------------------

y_pred = model.predict(X_test_scaled)


# -----------------------------
# 7. Evaluation
# -----------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)


# -----------------------------
# 8. Save Model
# -----------------------------

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/svm_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("\nModel saved successfully.")