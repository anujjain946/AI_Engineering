# Wine Quality Prediction

## 📌 Project Overview

Wine Quality Prediction is a **Machine Learning classification/regression project** that predicts the quality of wine based on its physicochemical properties.

The project uses wine-related measurements such as acidity, sugar, chlorides, sulfur dioxide, density, pH, and alcohol to predict the wine quality score.

---

## 🎯 Objective

The main objective is to build a Machine Learning model that can predict wine quality using the available chemical properties.

```text
Wine Chemical Properties
          ↓
Data Preprocessing
          ↓
Exploratory Data Analysis
          ↓
Feature Engineering
          ↓
Machine Learning Model
          ↓
Predicted Wine Quality
```

---

## 📊 Dataset

The dataset contains physicochemical properties of wine.

Typical columns include:

| Feature                | Description               |
| ---------------------- | ------------------------- |
| `fixed acidity`        | Fixed acidity of wine     |
| `volatile acidity`     | Volatile acidity          |
| `citric acid`          | Citric acid concentration |
| `residual sugar`       | Remaining sugar           |
| `chlorides`            | Chloride concentration    |
| `free sulfur dioxide`  | Free sulfur dioxide       |
| `total sulfur dioxide` | Total sulfur dioxide      |
| `density`              | Density of wine           |
| `pH`                   | Acidity level             |
| `sulphates`            | Sulphate concentration    |
| `alcohol`              | Alcohol percentage        |
| `quality`              | Wine quality score        |

### Target Variable

```text
quality
```

---

## 🤖 Machine Learning Problem

Wine quality prediction can be treated as:

```text
Supervised Learning
        ↓
Regression
        ↓
Quality Score Prediction
```

If the quality score is converted into categories such as:

```text
Low Quality
Medium Quality
High Quality
```

then the problem becomes a **Classification** problem.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib

---

## 📁 Project Structure

```text
wine_quality_prediction/
│
├── dataset/
│   └── winequality.csv
│
├── model/
│   ├── wine_quality_model.pkl
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
EDA
     ↓
Data Visualization
     ↓
Feature Selection
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

### Check Missing Values

```python
print(df.isnull().sum())
```

### Check Duplicate Records

```python
print(df.duplicated().sum())
```

### Check Dataset Information

```python
print(df.info())
```

### Statistical Summary

```python
print(df.describe())
```

---

## 📈 Exploratory Data Analysis

EDA can be performed using Matplotlib and Seaborn.

Important visualizations include:

* Histogram
* Box Plot
* Scatter Plot
* Bar Chart
* Correlation Heatmap
* Distribution Plot

Example:

```python
import matplotlib.pyplot as plt

plt.hist(df["quality"])
plt.title("Wine Quality Distribution")
plt.xlabel("Quality")
plt.ylabel("Frequency")
plt.show()
```

---

## 🔥 Correlation Analysis

Correlation can help identify relationships between wine features and quality.

```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)

plt.title("Wine Feature Correlation")
plt.show()
```

---

## ✂️ Train/Test Split

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

---

## 📏 Feature Scaling

Features can have different ranges, so scaling can be applied.

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

The scaler must not be fitted again on test data.

---

## 🧠 Machine Learning Models

For regression, models that can be compared include:

```text
Linear Regression
Ridge Regression
Lasso Regression
Decision Tree Regressor
Random Forest Regressor
Gradient Boosting Regressor
```

For classification, models can include:

```text
Logistic Regression
Decision Tree Classifier
Random Forest Classifier
KNN
SVM
```

---

## 📏 Regression Evaluation Metrics

If wine quality is treated as a regression problem:

### MAE

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)
```

### MSE

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
```

### RMSE

```python
rmse = mean_squared_error(y_test, y_pred) ** 0.5
```

### R² Score

```python
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
```

---

## 📊 Classification Evaluation Metrics

If wine quality is converted into categories, use:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

Example:

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
```

---

## 💾 Save the Model

The trained model can be saved using Joblib.

```python
import joblib

joblib.dump(model, "model/wine_quality_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")
```

---

## 🔮 Sample Prediction

Example input:

```json
{
    "fixed_acidity": 7.4,
    "volatile_acidity": 0.7,
    "citric_acid": 0.0,
    "residual_sugar": 1.9,
    "chlorides": 0.076,
    "free_sulfur_dioxide": 11,
    "total_sulfur_dioxide": 34,
    "density": 0.9978,
    "pH": 3.51,
    "sulphates": 0.56,
    "alcohol": 9.4
}
```

Example output:

```json
{
    "predicted_quality": 5
}
```

The actual prediction depends on the trained model.

---

## ⚠️ Common Issues

### 1. Feature Name Mismatch

The features used during prediction must match the features used during training.

For example:

```text
Training:
alcohol

Prediction:
Alcohol
```

These are different column names.

Keep feature names consistent.

---

### 2. Scaling the Test Data Incorrectly

Incorrect:

```python
X_test = scaler.fit_transform(X_test)
```

Correct:

```python
X_test = scaler.transform(X_test)
```

---

### 3. Target Included in Features

Do not include `quality` inside `X`.

Correct:

```python
X = df.drop("quality", axis=1)
y = df["quality"]
```

---

### 4. Outliers

Some wine features may contain extreme values.

Use a box plot to investigate:

```python
plt.boxplot(df["alcohol"])
plt.show()
```

Do not automatically remove every outlier. First determine whether it is a valid observation.

---

## 🚀 Future Improvements

* Compare multiple Machine Learning models
* Hyperparameter tuning
* Cross-validation
* Feature importance
* Outlier analysis
* Classification version of the project
* Flask API
* Docker deployment
* Web-based prediction interface
* Model monitoring

---

## 📚 Key Learning Outcomes

This project helps practice:

* Data loading
* Data cleaning
* EDA
* Data visualization
* Correlation analysis
* Feature selection
* Train/Test Split
* Feature scaling
* Regression
* Classification
* Model evaluation
* Model serialization
* Prediction API development

---

## 👨‍💻 Author

**Anuj Jain**

Python | Django | Data Science | Machine Learning | AI/ML
