# ✈️ Flight Price Prediction

## 📌 Project Overview

Flight Price Prediction is a **Supervised Machine Learning Regression project** that predicts the price of a flight based on different flight-related features.

The model uses information such as airline, source, destination, number of stops, journey date, departure time, arrival time, and flight duration to predict the expected ticket price.

---

## 🎯 Objective

The main objective of this project is to build a Machine Learning model that can predict flight ticket prices.

```text
Flight Details
      ↓
Data Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Categorical Encoding
      ↓
Train/Test Split
      ↓
Model Training
      ↓
Prediction
      ↓
Model Evaluation
```

---

## 🤖 Machine Learning Problem

This is a:

```text
Supervised Learning
        ↓
Regression
        ↓
Flight Price Prediction
```

The target variable is the flight `Price`.

---

## 📊 Dataset

The dataset contains flight information and ticket prices.

| Feature           | Description                   | Type        |
| ----------------- | ----------------------------- | ----------- |
| `Airline`         | Airline company               | Categorical |
| `Date_of_Journey` | Date of journey               | Date        |
| `Source`          | Departure city                | Categorical |
| `Destination`     | Arrival city                  | Categorical |
| `Route`           | Flight route                  | Categorical |
| `Dep_Time`        | Departure time                | Time        |
| `Arrival_Time`    | Arrival time                  | Time        |
| `Duration`        | Flight duration               | Time        |
| `Total_Stops`     | Number of stops               | Categorical |
| `Additional_Info` | Additional flight information | Categorical |
| `Price`           | Flight ticket price           | Target      |
Airline	Date_of_Journey	Source	Destination	Route	Dep_Time	Arrival_Time	Duration	Total_Stops	Additional_Info

---

## 🎯 Target Variable

```text
Price
```

The model learns the relationship between the flight features and its ticket price.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Flask

---

## 📁 Project Structure

```text
flight_price_prediction/
│
├── dataset/
│   └── flight_price.csv
│
├── model/
│   ├── flight_price_model.pkl
│   ├── scaler.pkl
│   └── columns.pkl
│
├── config.py
├── preprocess.py
├── train.py
├── evaluate.py
├── predict.py
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔄 Machine Learning Workflow

```text
Load Dataset
     ↓
Data Cleaning
     ↓
Check Missing Values
     ↓
Check Duplicates
     ↓
EDA
     ↓
Feature Engineering
     ↓
Categorical Encoding
     ↓
Feature Scaling
     ↓
Train/Test Split
     ↓
Model Training
     ↓
Prediction
     ↓
Evaluation
     ↓
Save Model
```

---

# 🧹 Data Preprocessing

## 1. Check Dataset

```python
import pandas as pd

df = pd.read_csv("dataset/flight_price.csv")

print(df.head())
print(df.info())
print(df.describe())
```

---

## 2. Check Missing Values

```python
print(df.isnull().sum())
```

Missing values should be handled before model training.

---

## 3. Check Duplicate Records

```python
print(df.duplicated().sum())
```

Duplicates should be investigated before training the model.

---

# 🔧 Feature Engineering

Flight datasets often contain date and time information as strings.

These values can be converted into useful numerical features.

### Journey Date

From:

```text
24/03/2019
```

Extract:

```text
journey_day
journey_month
journey_year
```

### Departure Time

From:

```text
10:20
```

Extract:

```text
dep_hour
dep_minute
```

### Arrival Time

From:

```text
13:15
```

Extract:

```text
arrival_hour
arrival_minute
```

### Duration

Convert:

```text
2h 55m
```

into:

```text
175 minutes
```

This makes the feature easier for Machine Learning models to process.

---

# 🔤 Categorical Encoding

Features such as:

```text
Airline
Source
Destination
Total_Stops
```

contain categorical values.

They need to be converted into numerical representations.

One-hot encoding can be used:

```python
pd.get_dummies(
    df,
    columns=[
        "Airline",
        "Source",
        "Destination"
    ],
    drop_first=True
)
```

---

# ✂️ Train/Test Split

The dataset is divided into training and testing data.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The training data is used to train the model, while the test data is used to evaluate its performance.

---

# 📏 Feature Scaling

If required, numerical features can be scaled using `StandardScaler`.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

Important:

```text
Training Data → fit_transform()
Testing Data  → transform()
```

Never fit the scaler separately on the test dataset.

---

# 🧠 Machine Learning Models

The following regression algorithms can be compared:

```text
Linear Regression
Decision Tree Regressor
Random Forest Regressor
Gradient Boosting Regressor
Random Forest
```

A tree-based model such as **Random Forest Regressor** can be used as one of the main models because flight pricing can have nonlinear relationships.

---

# 📈 Model Training

Example:

```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
```

---

# 📏 Model Evaluation

Since this is a regression problem, the following metrics can be used.

## MAE — Mean Absolute Error

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)

print("MAE:", mae)
```

MAE represents the average absolute difference between the actual and predicted prices.

---

## MSE — Mean Squared Error

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)

print("MSE:", mse)
```

---

## RMSE — Root Mean Squared Error

```python
rmse = mean_squared_error(y_test, y_pred) ** 0.5

print("RMSE:", rmse)
```

---

## R² Score

```python
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)

print("R2 Score:", r2)
```

A higher R² generally indicates that the model explains more of the variation in the target.

---

# 🔮 Prediction Input

A simplified API input can look like:

```json
{
    "airline": "IndiGo",
    "source": "Delhi",
    "destination": "Cochin",
    "total_stops": 1,
    "duration_minutes": 170,
    "journey_day": 24,
    "journey_month": 3,
    "dep_hour": 10,
    "dep_minute": 20,
    "arrival_hour": 13,
    "arrival_minute": 15
}
```

---

# 🧩 Prediction Function

```python
def predictFlightPrice(
    airline,
    source,
    destination,
    total_stops,
    duration_minutes,
    journey_day,
    journey_month,
    dep_hour,
    dep_minute,
    arrival_hour,
    arrival_minute
):
    pass
```

---

# 💾 Save Model

The trained model can be saved using Joblib.

```python
import joblib

joblib.dump(
    model,
    "model/flight_price_model.pkl"
)

joblib.dump(
    scaler,
    "model/scaler.pkl"
)
```

If one-hot encoding is used, the training feature names should also be saved so that prediction data can be created with the exact same columns.

```python
joblib.dump(
    X.columns.tolist(),
    "model/columns.pkl"
)
```

---

# ⚠️ Common Issues

## 1. Feature Name Mismatch

The feature names during prediction must match the names used during training.

For example:

```text
Training:
duration_minutes

Prediction:
Duration
```

These are different feature names.

Always maintain consistent feature names.

---

## 2. Different Number of Features

If the model was trained using 25 features but prediction provides only 12 features, prediction will fail.

The prediction DataFrame must contain all required encoded features.

---

## 3. Categorical Values

Values such as:

```text
IndiGo
Delhi
Cochin
```

cannot directly be passed to most numerical Machine Learning models.

They must first be encoded.

---

## 4. Date and Time Values

Raw values such as:

```text
24/03/2019
10:20
13:15
2h 55m
```

should generally be transformed into useful numerical features.

---

## 5. Data Leakage

Do not use the target `Price` as an input feature.

Correct:

```python
X = df.drop("Price", axis=1)
y = df["Price"]
```

---

## 6. Scaling Test Data

Incorrect:

```python
X_test = scaler.fit_transform(X_test)
```

Correct:

```python
X_test = scaler.transform(X_test)
```

---

# 📊 EDA Visualizations

Important visualizations for this project include:

### Price Distribution

```python
plt.hist(df["Price"])

plt.title("Flight Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()
```

### Airline vs Price

```python
sns.boxplot(
    x="Airline",
    y="Price",
    data=df
)

plt.xticks(rotation=45)
plt.show()
```

### Total Stops vs Price

```python
sns.boxplot(
    x="Total_Stops",
    y="Price",
    data=df
)

plt.show()
```

These visualizations can help identify pricing patterns and unusual values.

---

# 🚀 Future Improvements

* Compare multiple regression models
* Hyperparameter tuning
* Cross-validation
* Feature importance analysis
* Better date/time feature engineering
* Outlier analysis
* Flask REST API
* Docker deployment
* Web-based prediction interface
* Model monitoring
* MLflow experiment tracking

---

# 📚 Key Learning Outcomes

This project helps practice:

* Data preprocessing
* Exploratory Data Analysis
* Data visualization
* Feature engineering
* Date/time feature extraction
* Categorical encoding
* Feature scaling
* Train/Test Split
* Regression algorithms
* Model evaluation
* Model serialization
* Flask API development

---

# 👨‍💻 Author

**Anuj Jain**

Python | Django | Data Science | Machine Learning | AI/ML
