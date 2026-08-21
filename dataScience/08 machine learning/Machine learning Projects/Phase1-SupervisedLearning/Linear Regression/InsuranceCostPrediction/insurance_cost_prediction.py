import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Load dataset
df = pd.read_csv("dataset/insurance.csv")


# Convert categorical columns
df = pd.get_dummies(
    df,
    columns=["sex", "smoker", "region"],
    drop_first=True
)


# Features and target
X = df.drop("charges", axis=1)
y = df["charges"]


# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Model
model = LinearRegression()

model.fit(X_train, y_train)


# Prediction
y_pred = model.predict(X_test)


# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)


print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)


# Save model
joblib.dump(model, "model/insurance_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")
joblib.dump(X.columns.tolist(), "model/columns.pkl")