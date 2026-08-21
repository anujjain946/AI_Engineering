

# Universal ML Model Identification
                    START
                      │
                      ▼
              Do you have Target y?
                 /          \
               NO            YES
               │              │
               ▼              ▼
          Unsupervised     What is y?
             Learning          │
                    ┌─────────┼─────────┐
                    │         │         │
                 Number     Category   Future
                    │         │         │
                    ▼         ▼         ▼
               Regression Classification Forecasting
                    │         │         │
                    ▼         ▼         ▼
               Linear       Logistic    ARIMA
               Ridge        Tree        SARIMA
               Lasso        RF          XGBoost
               Random       SVM         LSTM
               Forest       KNN
               XGBoost      Naive Bayes

# Linear Regression

```text
Linear Regression
│
├── 1. Data Analysis
│   │
│   ├── Univariate Analysis
│   │   └── Analysis of One Variable
│   │
│   ├── Bivariate Analysis
│   │   └── Relationship Between Two Variables
│   │
│   └── Multivariate Analysis
│       └── Analysis of Multiple Variables
│
├── 2. Correlation Analysis
│   ├── Positive Correlation
│   ├── Negative Correlation
│   ├── Zero Correlation
│   └── Correlation Matrix / Heatmap
│
├── 3. Simple Linear Regression
│   ├── One Independent Feature
│   ├── Linear Equation
│   ├── Intercept
│   ├── Coefficient / Slope
│   └── Prediction
│
├── 4. Multiple Linear Regression
│   ├── Two or More Features
│   ├── Multiple Coefficients
│   ├── Feature Relationships
│   └── Prediction
│
├── 5. Polynomial Regression
│   ├── Non-Linear Relationships
│   ├── Polynomial Features
│   ├── Degree of Polynomial
│   ├── Underfitting
│   └── Overfitting
│
├── 6. Model Evaluation
│   ├── MAE
│   ├── MSE
│   ├── RMSE
│   └── R² Score
│
└── 7. Linear Regression Workflow
    ├── Data Collection
    ├── EDA
    ├── Feature Selection
    ├── Train/Test Split
    ├── Model Training
    ├── Prediction
    ├── Model Evaluation
    └── Model Improvement
```



Linear Regression is a **supervised machine learning algorithm** used to predict a **continuous numerical value** by finding a relationship between input features and a target variable.

### Common Applications

* House Price Prediction
*   
* Sales Prediction
* Revenue Prediction
* Demand Prediction
* Temperature Prediction

---

## 1. Linear Regression Equation

For simple linear regression:

[
y = b_0 + b_1x
]

Where:

* `y` → Predicted/target value
* `x` → Input feature
* `b0` → Intercept
* `b1` → Coefficient/Slope

Example:

```text
Experience → Salary
```

If:

```text
Intercept = 20,000
Coefficient = 5,000
```

Then:

[
Salary = 20000 + 5000(Experience)
]

For 5 years of experience:

[
Salary = 20000 + 5000(5)
]

```text
Predicted Salary = 45,000
```

---

# 2. Univariate Analysis

**Univariate analysis means analyzing one variable at a time.**

Example:

```text
Age
Salary
Experience
```

### Example

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df["Age"].describe())
```

### Visualization

```python
import matplotlib.pyplot as plt

plt.hist(df["Age"], bins=20)

plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")

plt.show()
```

### What to analyze

* Mean
* Median
* Minimum
* Maximum
* Standard deviation
* Distribution
* Skewness
* Outliers

---

# 3. Bivariate Analysis

**Bivariate analysis means analyzing two variables together.**

For Linear Regression:

```text
Experience ↔ Salary
```

### Scatter Plot

```python
import matplotlib.pyplot as plt

plt.scatter(
    df["Experience"],
    df["Salary"]
)

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")

plt.show()
```

A scatter plot helps determine whether the relationship appears approximately linear.

### Positive Relationship

```text
Salary
  |
  |            ●
  |         ●
  |      ●
  |   ●
  | ●
  +---------------- Experience
```

### Negative Relationship

```text
Salary
  |
  | ●
  |    ●
  |       ●
  |          ●
  |             ●
  +---------------- Experience
```

---

# 4. Multivariate Analysis

**Multivariate analysis means analyzing three or more variables together.**

Example:

```text
Area
Bedrooms
Bathrooms
Age
   ↓
House Price
```

A model can use multiple features to predict one target.

```python
X = df[
    [
        "Area",
        "Bedrooms",
        "Bathrooms",
        "Age"
    ]
]

y = df["Price"]
```

Useful visualizations:

* Pair Plot
* Correlation Heatmap
* Multiple feature analysis
* Grouped analysis

---

# 5. Correlation Analysis

Correlation measures the **strength and direction of a linear relationship** between numerical variables.

Correlation ranges from:

```text
-1  →  0  →  +1
```

|  Value | Meaning                      |
| -----: | ---------------------------- |
|   `+1` | Perfect positive correlation |
| `+0.7` | Strong positive correlation  |
| `+0.3` | Weak positive correlation    |
|    `0` | No linear correlation        |
| `-0.3` | Weak negative correlation    |
| `-0.7` | Strong negative correlation  |
|   `-1` | Perfect negative correlation |

### Calculate Correlation

```python
print(
    df[["Experience", "Salary"]].corr()
)
```

Example:

```text
             Experience    Salary
Experience      1.00       0.92
Salary          0.92       1.00
```

`0.92` indicates a strong positive linear relationship.

### Correlation Heatmap

```python
import seaborn as sns
import matplotlib.pyplot as plt

correlation = df.corr(numeric_only=True)

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()
```

> **Important:** Correlation does not imply causation.

---

# 6. Simple Linear Regression

**Simple Linear Regression uses one independent feature to predict one continuous target.**

Example:

```text
Experience → Salary
```

Equation:

[
y = b0 + b1x
]

### Implementation

```python
from sklearn.linear_model import LinearRegression

X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()

model.fit(X, y)
```

### Prediction

```python
prediction = model.predict(
    [[6]]
)

print(prediction)
```

---

# 7. Understanding Coefficients

After training:

```python
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)
```

Suppose:

```text
Intercept = 20,000
Coefficient = 5,000
```

The model becomes:

[
Salary = 20000 + 5000(Experience)
]

The coefficient means:

> For every one-unit increase in Experience, the predicted Salary increases by approximately 5,000, assuming the linear model applies.

---

# 8. Multiple Linear Regression

**Multiple Linear Regression uses two or more independent features to predict a continuous target.**

Example:

```text
Area
Bedrooms
Bathrooms
Age
   ↓
House Price
```

Equation:

[
y = b0 + b1x1 + b2x2 + b3x3 + ... + bnxn
]

### Implementation

```python
from sklearn.linear_model import LinearRegression

X = df[
    [
        "Area",
        "Bedrooms",
        "Bathrooms"
    ]
]

y = df["Price"]

model = LinearRegression()

model.fit(X, y)
```

### Prediction

```python
prediction = model.predict([
    [1500, 3, 2]
])

print(prediction)
```

---

# 9. Simple vs Multiple Linear Regression

| Simple Linear Regression | Multiple Linear Regression      |
| ------------------------ | ------------------------------- |
| One feature              | Two or more features            |
| `y = b0 + b1x`           | `y = b0 + b1x1 + b2x2...`       |
| Easy to visualize        | Difficult to visualize directly |
| Experience → Salary      | Area + Rooms + Age → Price      |

---

# 10. Polynomial Regression

Polynomial Regression is used when the relationship between the feature and target is **non-linear**.

A degree-2 polynomial:

[
y = b0 + b1x + b2x^2
]

A degree-3 polynomial:

[
y = b0 + b1x + b2x^2 + b3x^3
]

### Example

```text
Linear:

      /
     /
    /
   /
  /

Polynomial:

    ●
  ●   ●
 ●     ●
```

---

## Polynomial Regression Implementation

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

X = df[["Experience"]]
y = df["Salary"]

poly = PolynomialFeatures(
    degree=2,
    include_bias=False
)

X_poly = poly.fit_transform(X)

model = LinearRegression()

model.fit(X_poly, y)
```

### Prediction

```python
new_data = [[6]]

new_data_poly = poly.transform(
    new_data
)

prediction = model.predict(
    new_data_poly
)

print(prediction)
```

---

# 11. Polynomial Regression Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

X = df[["Experience"]]
y = df["Salary"]

poly = PolynomialFeatures(
    degree=2,
    include_bias=False
)

X_poly = poly.fit_transform(X)

model = LinearRegression()

model.fit(X_poly, y)

x_range = np.linspace(
    X.min(),
    X.max(),
    100
).reshape(-1, 1)

x_range_poly = poly.transform(
    x_range
)

y_pred = model.predict(
    x_range_poly
)

plt.scatter(X, y)

plt.plot(
    x_range,
    y_pred
)

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Polynomial Regression")

plt.show()
```

---

# 12. Train-Test Split

Never evaluate the model on the same data used for training.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

Train:

```python
model.fit(
    X_train,
    y_train
)
```

Predict:

```python
y_pred = model.predict(
    X_test
)
```

---

# 13. Regression Evaluation Metrics

## MAE — Mean Absolute Error

[
MAE = \frac{1}{n}\sum |y-y_{pred}|
]

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(
    y_test,
    y_pred
)

print("MAE:", mae)
```

Lower MAE is generally better.

---

## MSE — Mean Squared Error

[
MSE = \frac{1}{n}\sum(y-y_{pred})^2
]

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(
    y_test,
    y_pred
)

print("MSE:", mse)
```

MSE penalizes larger errors more heavily.

---

## RMSE — Root Mean Squared Error

```python
import numpy as np

rmse = np.sqrt(mse)

print("RMSE:", rmse)
```

RMSE is expressed in the **same units as the target**.

---

## R² Score

```python
from sklearn.metrics import r2_score

r2 = r2_score(
    y_test,
    y_pred
)

print("R²:", r2)
```

R² measures the proportion of variance in the target explained by the model.

Example:

```text
R² = 0.85
```

means the model explains approximately **85% of the variance** in the target under the usual interpretation of R².

---

# 14. Complete Linear Regression Workflow

```text
Dataset
   ↓
Understand Dataset
   ↓
EDA
   ↓
Univariate Analysis
   ↓
Bivariate Analysis
   ↓
Multivariate Analysis
   ↓
Correlation Analysis
   ↓
Feature Engineering
   ↓
Train/Test Split
   ↓
Simple Linear Regression
   ↓
Multiple Linear Regression
   ↓
Polynomial Regression
   ↓
Prediction
   ↓
MAE
   ↓
MSE
   ↓
RMSE
   ↓
R² Score
   ↓
Residual Analysis
   ↓
Model Improvement
```

---

# 15. Key Differences

### Simple Linear Regression

```text
1 Feature
   ↓
Target
```

### Multiple Linear Regression

```text
Feature 1 ─┐
Feature 2 ─┤
Feature 3 ─┤
Feature 4 ─┘
     ↓
   Target
```

### Polynomial Regression

```text
X
↓
X²
X³
...
↓
Target
```

---

# 16. Important Interview Questions

1. What is Linear Regression?
2. What is the difference between simple and multiple linear regression?
3. What is the equation of Linear Regression?
4. What is the meaning of slope/coefficient?
5. What is an intercept?
6. What is correlation?
7. What is the difference between correlation and regression?
8. What is Polynomial Regression?
9. Why do we use Polynomial Regression?
10. What happens if polynomial degree is too high?
11. What is overfitting in Polynomial Regression?
12. What is MAE?
13. What is MSE?
14. What is RMSE?
15. What is R²?
16. Why do we split data into train and test sets?
17. What are the assumptions of Linear Regression?
18. What is multicollinearity?
19. What are residuals?
20. How do you evaluate a Linear Regression model?

---

# 17. Key Takeaways

```text
Linear Regression
        ↓
Continuous Target
        ↓
Relationship Between Features & Target
        ↓
Simple Regression
        ↓
Multiple Regression
        ↓
Polynomial Regression
        ↓
Prediction
        ↓
MAE / MSE / RMSE / R²
```

### Interview Definition

> **Linear Regression is a supervised machine learning algorithm that models the relationship between one or more independent variables and a continuous dependent variable by fitting a linear equation to the data.**


#####
# Machine Learning Pipeline

## What is a Pipeline?

A **Pipeline** in Machine Learning is a sequence of preprocessing and modeling steps connected together into a single workflow.

Instead of performing every step manually, Pipeline automatically executes the steps in the correct order.

```text
Raw Data
   ↓
Missing Value Handling
   ↓
Feature Scaling
   ↓
Feature Transformation
   ↓
ML Model
   ↓
Prediction
```

---

## Why Do We Use Pipeline?

Without Pipeline, we may need to perform each step separately:

```python
X_train = imputer.fit_transform(X_train)

X_train = scaler.fit_transform(X_train)

model.fit(X_train, y_train)
```

This can make the code:

* Longer
* Difficult to manage
* Easy to make mistakes
* More prone to data leakage

With Pipeline:

```python
pipeline.fit(X_train, y_train)
```

All steps are executed automatically.

---

# Simple Pipeline Example

Suppose we want to predict **Employee Salary using Experience**.

```text
Experience
     ↓
Preprocessing
     ↓
Linear Regression
     ↓
Salary Prediction
```

### Import Libraries

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
```

### Create Pipeline

```python
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])
```

### Train Model

```python
pipeline.fit(
    X_train,
    y_train
)
```

### Make Predictions

```python
y_pred = pipeline.predict(
    X_test
)
```

The Pipeline automatically performs:

```text
X_train
   ↓
StandardScaler
   ↓
LinearRegression
   ↓
Trained Model
```

---

# Pipeline with Missing Values

If the dataset contains missing values, we can add an imputer.

```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

pipeline = Pipeline([
    (
        "imputer",
        SimpleImputer(strategy="median")
    ),
    (
        "scaler",
        StandardScaler()
    ),
    (
        "model",
        LinearRegression()
    )
])
```

Training:

```python
pipeline.fit(
    X_train,
    y_train
)
```

Prediction:

```python
y_pred = pipeline.predict(
    X_test
)
```

### Workflow

```text
Training Data
     ↓
Missing Values
     ↓
SimpleImputer
     ↓
StandardScaler
     ↓
LinearRegression
     ↓
Prediction
```

---

# Pipeline with Polynomial Regression

Pipeline is especially useful for Polynomial Regression.

Without Pipeline:

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

poly = PolynomialFeatures(
    degree=2,
    include_bias=False
)

X_poly = poly.fit_transform(X_train)

model = LinearRegression()

model.fit(
    X_poly,
    y_train
)
```

With Pipeline:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

pipeline = Pipeline([
    (
        "poly",
        PolynomialFeatures(
            degree=2,
            include_bias=False
        )
    ),
    (
        "model",
        LinearRegression()
    )
])
```

Train:

```python
pipeline.fit(
    X_train,
    y_train
)
```

Predict:

```python
y_pred = pipeline.predict(
    X_test
)
```

### Workflow

```text
Experience
     ↓
PolynomialFeatures
     ↓
Experience
Experience²
     ↓
LinearRegression
     ↓
Salary Prediction
```

---

# Pipeline and Data Leakage

One of the biggest advantages of Pipeline is helping prevent **data leakage** during preprocessing.

Correct workflow:

```text
Training Data
     ↓
fit()
     ↓
Learn preprocessing parameters
     ↓
Transform Training Data
     ↓
Train Model
```

For test data:

```text
Test Data
     ↓
transform()
     ↓
Use already learned parameters
     ↓
Prediction
```

The test data should not be used to learn preprocessing parameters.

Pipeline helps keep these operations together and ensures the same preprocessing workflow is applied during training and prediction.

---

# Pipeline vs Manual Processing

### Without Pipeline

```text
Data
 ↓
Imputer
 ↓
Scaler
 ↓
PolynomialFeatures
 ↓
Model
```

Each step is handled manually.

### With Pipeline

```text
Data
 ↓
┌────────────────────────────┐
│         Pipeline           │
│                            │
│  Imputer                   │
│      ↓                     │
│  Scaler                    │
│      ↓                     │
│  PolynomialFeatures        │
│      ↓                     │
│  Model                     │
└────────────────────────────┘
 ↓
Prediction
```

---

# Important Pipeline Methods

## `fit()`

Used to train the complete pipeline.

```python
pipeline.fit(
    X_train,
    y_train
)
```

---

## `predict()`

Used to make predictions.

```python
y_pred = pipeline.predict(
    X_test
)
```

---

## `fit_transform()`

Usually used by preprocessing transformers.

```python
X_train = scaler.fit_transform(
    X_train
)
```

Pipeline handles the appropriate fitting and transformation internally.

---

# Pipeline with Model Evaluation

```python
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

pipeline.fit(
    X_train,
    y_train
)

y_pred = pipeline.predict(
    X_test
)

mae = mean_absolute_error(
    y_test,
    y_pred
)

mse = mean_squared_error(
    y_test,
    y_pred
)

rmse = mse ** 0.5

r2 = r2_score(
    y_test,
    y_pred
)

print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R²  :", r2)
```

---

# Complete Pipeline Workflow

```text
Machine Learning Pipeline
│
├── Dataset
│
├── Train/Test Split
│
├── Preprocessing
│   ├── Missing Value Handling
│   ├── Encoding
│   ├── Scaling
│   └── Feature Transformation
│
├── Feature Engineering
│
├── Machine Learning Model
│
├── Prediction
│
└── Model Evaluation
    ├── MAE
    ├── MSE
    ├── RMSE
    └── R²
```

---

# Key Benefits

* **Simplifies ML workflow**
* **Reduces repetitive code**
* **Keeps preprocessing and model together**
* **Helps prevent data leakage**
* **Ensures consistent preprocessing**
* **Makes model training and prediction easier**
* **Works with GridSearchCV and cross-validation**
* **Useful for production deployment**

---

# Pipeline — Easy Definition

> **Pipeline is a sequence of preprocessing and machine learning steps combined into a single workflow.**

### Easy Example

```text
Pipeline
   │
   ├── Missing Values
   │
   ├── Scaling
   │
   ├── Feature Transformation
   │
   └── ML Model
```

### Remember

```text
Pipeline = Multiple ML Steps → One Workflow
```

   