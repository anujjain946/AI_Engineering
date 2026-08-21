# Insurance Cost Prediction

## 📌 Project Overview

Insurance Cost Prediction is a **Machine Learning Regression project** that predicts the medical insurance cost of a person based on personal and health-related information.

The project uses **Scikit-Learn** to train a regression model and evaluate its performance using standard regression metrics.

---

## 🎯 Objective

The main objective of this project is to predict:

> **Medical Insurance Charges**

based on features such as:

* Age
* Sex
* BMI
* Number of Children
* Smoking Status
* Region

---

## 📊 Dataset

The dataset contains the following columns:

| Column     | Description            | Type        |
| ---------- | ---------------------- | ----------- |
| `age`      | Age of the person      | Numerical   |
| `sex`      | Gender                 | Categorical |
| `bmi`      | Body Mass Index        | Numerical   |
| `children` | Number of children     | Numerical   |
| `smoker`   | Smoking status         | Categorical |
| `region`   | Residential region     | Categorical |
| `charges`  | Medical insurance cost | Target      |


### Target Variable

```text
charges
```

---

## 🤖 Machine Learning Problem

This is a:

```text
Supervised Learning
        ↓
Regression
        ↓
Insurance Cost Prediction
```

The model learns the relationship between the input features and insurance charges.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Joblib

---

## 📁 Project Structure

```text


insurance_cost_prediction/
│
├── dataset/
│   └── insurance.csv
│
├── model/
│   ├── insurance_model.pkl
│
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
Exploratory Data Analysis
     ↓
Categorical Encoding
     ↓
Train/Test Split
     ↓
Feature Scaling
     ↓
Model Training
     ↓
Prediction
     ↓
Model Evaluation
     ↓
Save Model
```

---

## 🧹 Data Preprocessing

### 1. Categorical Encoding

Categorical columns are converted into numerical values using:

```python
pd.get_dummies()
```

Example:

```text
sex
male
female
```

is converted into numerical features such as:

```text
sex_male
```

### 2. Feature Scaling

Numerical features are scaled using:

```python
StandardScaler
```

Example:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

---

## 🧠 Machine Learning Model

The initial model used in this project is:

```text
Linear Regression
```

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)
```

The model predicts insurance charges based on the input features.

---

## 📏 Model Evaluation

The model can be evaluated using:

### Mean Absolute Error — MAE

Measures the average absolute difference between actual and predicted values.

```python
mean_absolute_error(y_test, y_pred)
```

### Mean Squared Error — MSE

Measures the average squared difference between actual and predicted values.

```python
mean_squared_error(y_test, y_pred)
```

### Root Mean Squared Error — RMSE

```python
rmse = mean_squared_error(y_test, y_pred) ** 0.5
```

### R² Score

Measures how well the model explains the variation in the target variable.

```python
r2_score(y_test, y_pred)
```

---

## 📈 Models for Comparison

The project can be extended by comparing multiple regression algorithms:

```text
Linear Regression
       ↓
Ridge Regression
       ↓
Lasso Regression
       ↓
Decision Tree Regressor
       ↓
Random Forest Regressor
       ↓
Gradient Boosting Regressor
```

The best model can be selected based on **MAE, RMSE and R² Score**.

---

## 💾 Model Saving

The trained model can be saved using Joblib:

```python
import joblib

joblib.dump(model, "model/insurance_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")
joblib.dump(X.columns.tolist(), "model/columns.pkl")
```

Saved files:

```text
insurance_model.pkl
scaler.pkl
columns.pkl
```

---

## 🔮 Sample Prediction Input

```json
{
    "age": 35,
    "sex": "male",
    "bmi": 28.5,
    "children": 2,
    "smoker": "no",
    "region": "southeast"
}
```

### Output

```json
{
    "predicted_insurance_cost": 7345.52
}
```

> The predicted value is an example. Actual results depend on the trained model.

---

## 🚀 Future Improvements

* Compare multiple regression algorithms
* Hyperparameter tuning
* Cross-validation
* Feature importance analysis
* Flask REST API
* Docker deployment
* Web-based prediction interface
* Model monitoring

---

## 📌 Key Learning Outcomes

Through this project, you can practice:

* Data preprocessing
* Exploratory Data Analysis
* Categorical encoding
* Feature scaling
* Train/Test Split
* Regression
* Model training
* Model evaluation
* Model serialization using Joblib
* Prediction using trained ML models

---

## 👨‍💻 Author

**Anuj Jain**

Python | Django | Machine Learning | AI/ML


