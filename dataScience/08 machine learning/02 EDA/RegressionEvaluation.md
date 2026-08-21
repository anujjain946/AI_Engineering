# 📊 Regression Evaluation

A simple and beginner-friendly guide to **Regression Evaluation**, including:

* MAE
* MSE
* RMSE
* R²
* Adjusted R²
* Residuals
* Regression assumptions
* ML pipelines

---

# 1. What is Regression Evaluation?

After training a regression model, we need to know:

> **How good is my model's prediction?**

For example, suppose the actual house prices are:

```text
Actual:
[100, 200, 300, 400]
```

And our model predicts:

```text
Predicted:
[110, 190, 280, 420]
```

We need metrics to measure the difference between **actual values** and **predicted values**.

The most common regression metrics are:

```text
MAE
MSE
RMSE
R²
Adjusted R²
```

---

# 2. Actual vs Predicted

Let's understand the basic concept first.

```text
Actual Value
     ↓
    100
     │
     │ Error = 10
     ↓
Predicted Value
    110
```

The difference is called the **error**.

```text
Error = Actual - Predicted
```

Example:

```text
Actual     = 100
Predicted  = 110

Error = 100 - 110
      = -10
```

---

# 3. MAE — Mean Absolute Error

## What is MAE?

MAE measures the **average absolute difference** between actual and predicted values.

### Formula

```text
MAE = Average(|Actual - Predicted|)
```

Example:

```text
Actual:     100   200   300
Predicted:  110   190   280
```

Errors:

```text
100 - 110 = -10
200 - 190 =  10
300 - 280 =  20
```

Absolute errors:

```text
10
10
20
```

Therefore:

```text
MAE = (10 + 10 + 20) / 3
    = 13.33
```

### Meaning

> On average, the prediction is approximately **13.33 units away from the actual value**.

### Python

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)

print("MAE:", mae)
```

### Important

**Lower MAE = Better model**

---

# 4. MSE — Mean Squared Error

## What is MSE?

MSE calculates the average of the **squared errors**.

### Formula

```text
MSE = Average((Actual - Predicted)²)
```

Using the previous example:

```text
Errors:

-10
 10
 20
```

Square them:

```text
100
100
400
```

Therefore:

```text
MSE = (100 + 100 + 400) / 3
    = 200
```

### Python

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)

print("MSE:", mse)
```

### Important

**Lower MSE = Better model**

MSE gives more importance to large errors because errors are squared.

---

# 5. RMSE — Root Mean Squared Error

## What is RMSE?

RMSE is the square root of MSE.

### Formula

```text
RMSE = √MSE
```

From the previous example:

```text
MSE = 200

RMSE = √200
     ≈ 14.14
```

### Python

```python
import numpy as np
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

print("RMSE:", rmse)
```

### Why is RMSE useful?

RMSE is in the **same unit as the target**.

For example:

```text
Target = House Price

RMSE = ₹50,000
```

This is easier to understand than an MSE expressed in squared currency units.

### Important

**Lower RMSE = Better model**

---

# 6. MAE vs MSE vs RMSE

| Metric | Meaning                | Large Errors     | Better |
| ------ | ---------------------- | ---------------- | ------ |
| MAE    | Average absolute error | Less sensitive   | Lower  |
| MSE    | Average squared error  | Highly sensitive | Lower  |
| RMSE   | Square root of MSE     | Sensitive        | Lower  |

### Easy Trick

```text
MAE  → Average error
MSE  → Squared error
RMSE → Square root of MSE
```

---

# 7. R² — R-Squared

## What is R²?

R² tells us how much of the variation in the target variable is explained by the model.

It is also called the **coefficient of determination**.

### Simple Example

Suppose:

```text
R² = 0.80
```

This means the model explains approximately **80% of the variance** in the target for that evaluation dataset.

### General interpretation

```text
R² = 1
→ Perfect fit

R² = 0
→ Model performs like predicting the mean, in the standard interpretation

R² < 0
→ Model can perform worse than that baseline
```

### Python

```python
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)

print("R²:", r2)
```

### Important

For R²:

> **Higher is generally better.**

But don't judge a regression model using R² alone. Always look at error metrics and the business context.

---

# 8. Adjusted R²

## What is Adjusted R²?

Adjusted R² is a modified version of R² that takes the **number of features/predictors** into account.

Normal R² can increase when additional features are added, even if those features are not useful.

Adjusted R² applies a penalty for unnecessary predictors.

### Formula

```text
Adjusted R² =
1 - [(1 - R²) × (n - 1) / (n - p - 1)]
```

Where:

```text
n = Number of observations
p = Number of predictors/features
```

### Example

Suppose:

```text
R² = 0.85
Features = 10
```

You add several unnecessary features.

R² might increase:

```text
0.85 → 0.87
```

But Adjusted R² may:

```text
0.82 → 0.81
```

This tells us that the new features may not actually improve the model meaningfully.

### When is Adjusted R² useful?

It is especially useful when comparing regression models with **different numbers of predictors**.

---

# 9. R² vs Adjusted R²

| R²                                   | Adjusted R²                                                    |
| ------------------------------------ | -------------------------------------------------------------- |
| Measures explained variance          | Measures explained variance with feature penalty               |
| Does not penalize extra predictors   | Penalizes unnecessary predictors                               |
| Can increase when features are added | Can decrease if added features don't help                      |
| Simpler                              | More useful for comparing models with different feature counts |

### Easy Trick

```text
R²
→ How much variation is explained?

Adjusted R²
→ How much variation is explained after considering the number of features?
```

---

# 10. Residuals

## What is a Residual?

A residual is the difference between the **actual value and predicted value**.

### Formula

```text
Residual = Actual - Predicted
```

Example:

```text
Actual     = 100
Predicted  = 90

Residual = 100 - 90
         = 10
```

Another example:

```text
Actual     = 100
Predicted  = 110

Residual = 100 - 110
         = -10
```

---

# 11. Residual Plot

A residual plot helps us understand whether the regression model is making systematic errors.

Ideally:

```text
Residual
   ↑
 + |   .    .      .
   |      .    .
 0 |------------------------→ Predicted
   |   .      .    .
 - |      .       .
```

We generally want residuals to look **randomly scattered around zero**.

### Good residual pattern

```text
.   .      .
   .  .  .
.      .     .
-------------------- 0
   .    .   .
      .     .
```

### Bad residual pattern

If you see a clear curve, funnel, or other systematic pattern, it may indicate that the model or its assumptions need attention.

---

# 12. How to Calculate Residuals in Python

```python
residuals = y_test - y_pred

print(residuals)
```

Using Pandas:

```python
import pandas as pd

results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

results["Residual"] = (
    results["Actual"] - results["Predicted"]
)

print(results)
```

---

# 13. Regression Assumptions

Classical linear regression relies on several important assumptions.

## 1. Linearity

There should be an approximately linear relationship between predictors and the target, in the context of the linear model.

Example:

```text
X increases
     ↓
Y tends to change approximately linearly
```

If the true relationship is strongly curved, simple linear regression may not fit well.

---

## 2. Independence of Errors

Residuals should generally be independent of each other.

This is particularly important for:

* Time-series data
* Sequential observations
* Repeated measurements

For example, today's prediction error should not systematically depend on yesterday's error.

---

## 3. Homoscedasticity

The variance of residuals should be approximately constant across the range of predictions or fitted values.

### Good

```text
 .   . .   .
. . .  . .  .
 .  . .   . .
```

### Problem

```text
.
 . .
   .   .
      .     .
         .       .
```

A funnel-shaped pattern can indicate **heteroscedasticity**.

---

## 4. Normality of Residuals

For classical statistical inference, residuals are often assumed to be approximately normally distributed.

This assumption is more important for:

* Confidence intervals
* Hypothesis tests
* Statistical inference

It is not required in the same way merely to obtain good predictions.

---

## 5. No Perfect Multicollinearity

Features should not be perfectly linearly dependent on each other.

Example:

```text
Age in years
Age in months
```

These contain essentially the same information.

High multicollinearity can make coefficient estimates unstable and harder to interpret.

---

# 14. Summary of Regression Assumptions

```text
Linear Regression
       │
       ├── Linearity
       │
       ├── Independent Errors
       │
       ├── Constant Variance
       │   (Homoscedasticity)
       │
       ├── Approximately Normal Residuals
       │   (mainly for inference)
       │
       └── No Perfect Multicollinearity
```

---

# 15. What is a Pipeline?

A Pipeline allows us to combine preprocessing and model training into a **single workflow**.

Instead of doing:

```text
Data
 ↓
Missing Value Handling
 ↓
Scaling
 ↓
Model
```

manually, we can create:

```text
Pipeline
   ↓
Imputer
   ↓
Scaler
   ↓
Model
```

---

# 16. Why Use Pipelines?

Pipelines provide several benefits:

### 1. Cleaner Code

All preprocessing and modeling steps are organized together.

### 2. Avoid Data Leakage

Preprocessing is fitted only on the training data when the pipeline is used correctly.

### 3. Easy Training

You can simply call:

```python
pipeline.fit(X_train, y_train)
```

### 4. Easy Prediction

```python
pipeline.predict(X_test)
```

### 5. Easy Deployment

The preprocessing and model can be saved together.

---

# 17. Simple Regression Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])
```

Train:

```python
pipeline.fit(X_train, y_train)
```

Predict:

```python
y_pred = pipeline.predict(X_test)
```

Evaluate:

```python
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = mse ** 0.5

r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)
```

---

# 18. Pipeline with Missing Values

If your dataset contains missing numerical values:

```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])
```

Then:

```python
pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
```

---

# 19. Numerical + Categorical Features

Real-world datasets often contain both numerical and categorical columns.

Example:

```text
Numerical:
Age
Salary
Experience

Categorical:
Gender
City
Education
```

We can use `ColumnTransformer`.

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import (
    StandardScaler,
    OneHotEncoder
)
from sklearn.linear_model import LinearRegression
```

Define columns:

```python
numeric_features = [
    "Age",
    "Salary",
    "Experience"
]

categorical_features = [
    "Gender",
    "City",
    "Education"
]
```

Numerical pipeline:

```python
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])
```

Categorical pipeline:

```python
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])
```

Combine them:

```python
preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])
```

Final pipeline:

```python
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])
```

Train:

```python
model.fit(X_train, y_train)
```

Predict:

```python
y_pred = model.predict(X_test)
```

---

# 20. Complete Regression Evaluation Example

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import numpy as np
```

### Split data

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### Create pipeline

```python
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])
```

### Train

```python
pipeline.fit(X_train, y_train)
```

### Predict

```python
y_pred = pipeline.predict(X_test)
```

### Evaluate

```python
mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R²  :", r2)
```

---

# 21. How to Interpret Results

Suppose we get:

```text
MAE  = 10
MSE  = 150
RMSE = 12.25
R²   = 0.85
```

Interpretation:

```text
MAE = 10
→ Average absolute prediction error is about 10 target units.

RMSE = 12.25
→ Typical error scale is about 12.25 target units, with larger errors penalized more.

R² = 0.85
→ The model explains about 85% of the variance in the evaluation data.
```

Remember:

```text
MAE  → Lower is better
MSE  → Lower is better
RMSE → Lower is better
R²   → Higher is generally better
```

---

# 22. Which Metric Should I Use?

### Use MAE when:

You want an easy-to-understand average error and don't want large errors to dominate as strongly.

### Use MSE when:

Large errors should be penalized strongly.

### Use RMSE when:

You want the error in the same units as the target while still penalizing large errors.

### Use R² when:

You want to understand how much target variance is explained by the model.

### Use Adjusted R² when:

You are comparing regression models with different numbers of predictors and want to account for model complexity.

---

# 23. Quick Comparison

| Metric      | Meaning                    | Better |
| ----------- | -------------------------- | ------ |
| MAE         | Average absolute error     | Lower  |
| MSE         | Average squared error      | Lower  |
| RMSE        | Square root of MSE         | Lower  |
| R²          | Explained variance         | Higher |
| Adjusted R² | R² adjusted for predictors | Higher |

---

# 24. Interview Quick Questions

### Q1. What is MAE?

> MAE is the average absolute difference between actual and predicted values.

### Q2. What is MSE?

> MSE is the average squared difference between actual and predicted values.

### Q3. Why does MSE penalize large errors?

> Because the errors are squared, larger errors contribute disproportionately more to the metric.

### Q4. What is RMSE?

> RMSE is the square root of MSE and is expressed in the same units as the target.

### Q5. What is R²?

> R² measures the proportion of variance in the target that is explained by the regression model.

### Q6. What is Adjusted R²?

> Adjusted R² modifies R² by accounting for the number of predictors in the model.

### Q7. What is a residual?

> A residual is the difference between the actual value and the predicted value.

```text
Residual = Actual - Predicted
```

### Q8. What is homoscedasticity?

> Homoscedasticity means the residual variance is approximately constant across the range of fitted values.

### Q9. What is multicollinearity?

> Multicollinearity occurs when predictor variables are highly linearly related, making coefficient estimates less stable.

### Q10. Why use a Pipeline?

> A Pipeline combines preprocessing and model training into one workflow, reduces code repetition, and helps prevent data leakage during preprocessing.

---

# 🎯 Easy Memory Trick

```text
MAE
↓
Average Absolute Error

MSE
↓
Squared Error

RMSE
↓
√MSE

R²
↓
Explained Variance

Adjusted R²
↓
R² + Feature Penalty

Residual
↓
Actual - Predicted

Pipeline
↓
Preprocessing + Model
```

---

# 🚀 Final Regression Workflow

```text
Dataset
   ↓
Features + Target
   ↓
Train/Test Split
   ↓
Pipeline
   ├── Imputation
   ├── Encoding
   ├── Scaling
   └── Regression Model
           ↓
        Prediction
           ↓
     ┌──────────────┐
     │ Evaluation   │
     ├──────────────┤
     │ MAE          │
     │ MSE          │
     │ RMSE         │
     │ R²           │
     │ Adjusted R²  │
     └──────────────┘
           ↓
   Residual Analysis
           ↓
   Check Assumptions
           ↓
   Improve / Tune Model
```

## ⭐ One-Line Summary

> **Regression evaluation tells us how accurately our model predicts numerical values, while residual analysis and regression assumptions help us understand whether the model is appropriate and where it may be going wrong.**
