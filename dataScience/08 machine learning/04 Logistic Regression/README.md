## Logistic Regression

Logistic Regression is a **supervised machine learning classification algorithm** used to predict categorical outcomes. Although its name contains "Regression", it is primarily used for **classification problems**.

### 1. Sigmoid Function

Logistic Regression first calculates a linear combination of input features:

```python
z = β0 + β1X1 + β2X2 + ... + βnXn
```

The result is passed through the **Sigmoid function**:

```text
σ(z) = 1 / (1 + e⁻ᶻ)
```

The sigmoid function converts any value into a probability between **0 and 1**.

```text
z → Linear Equation
        ↓
     Sigmoid
        ↓
 Probability (0 → 1)
```

Example:

```text
z = -5 → Probability ≈ 0.007
z =  0 → Probability = 0.500
z =  2 → Probability ≈ 0.881
z =  5 → Probability ≈ 0.993
```

---

### 2. Probability

`predict_proba()` returns the probability of each class.

```python
model.predict_proba(X_test)
```

Example:

```text
[[0.18, 0.82]]
```

This means:

```text
Class 0 → 18%
Class 1 → 82%
```

Therefore, the model predicts **Class 1** with an 82% probability.

---

### 3. Decision Boundary

The probability is converted into a class using a threshold.

The default threshold is usually:

```text
0.5
```

Rule:

```text
Probability >= 0.5 → Class 1
Probability <  0.5 → Class 0
```

Example:

```text
0.20 → Class 0
0.40 → Class 0
0.51 → Class 1
0.90 → Class 1
```

The boundary that separates different classes is called the **Decision Boundary**.

---

### 4. Binary Classification

Binary classification contains exactly **two classes**.

Examples:

```text
Yes / No
0 / 1
Spam / Not Spam
Churn / Not Churn
Approved / Rejected
```

Example:

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

---

### 5. Multiclass Classification

Logistic Regression can also be used when there are more than two classes.

Examples:

```text
Low
Medium
High
```

or:

```text
Cat
Dog
Horse
```

The model calculates probabilities for each class and selects the class with the highest probability.

Example:

```text
Cat   → 0.10
Dog   → 0.75
Horse → 0.15
```

Prediction:

```text
Dog
```

---

### 6. Log Loss

Log Loss measures how well the predicted probabilities match the actual classes.

For binary classification:

```text
Log Loss = -[y log(p) + (1-y) log(1-p)]
```

A lower Log Loss means better probability predictions.

Example when actual class is `1`:

```text
Prediction = 0.99 → Very Low Loss
Prediction = 0.90 → Low Loss
Prediction = 0.60 → Moderate Loss
Prediction = 0.10 → High Loss
Prediction = 0.01 → Extremely High Loss
```

Therefore:

```text
Lower Log Loss = Better
```

---

### 7. L1 Regularization

L1 regularization adds a penalty based on the absolute value of coefficients:

```text
Loss + λ Σ|β|
```

L1 can make some coefficients exactly zero.

Therefore, L1 can perform **feature selection**.

```python
model = LogisticRegression(
    penalty="l1",
    solver="liblinear"
)
```

Example:

```text
Feature       Coefficient

Age              0.82
Income           0.00
Balance         -0.54
Visits           0.00
CreditScore      0.31
```

Features with coefficients equal to zero have effectively been removed from the model.

---

### 8. L2 Regularization

L2 regularization adds a penalty based on the squared coefficients:

```text
Loss + λ Σβ²
```

It reduces large coefficients and helps control overfitting.

```python
model = LogisticRegression(
    penalty="l2"
)
```

L2 generally makes coefficients smaller rather than forcing them exactly to zero.

---

### 9. L1 vs L2

| Feature                  | L1                                 | L2                         |   |      |
| ------------------------ | ---------------------------------- | -------------------------- | - | ---- |
| Penalty                  | `                                  | β                          | ` | `β²` |
| Coefficients become zero | Yes, some                          | Usually no                 |   |      |
| Feature Selection        | Yes                                | Not directly               |   |      |
| Sparse Model             | Yes                                | Usually no                 |   |      |
| Main Purpose             | Feature selection + regularization | Regularization + stability |   |      |

### Remember

```text
L1 → Zero coefficients → Feature Selection
L2 → Small coefficients → Stabilization
```

---

### 10. C Parameter

In Scikit-Learn, `C` controls the inverse strength of regularization.

```python
LogisticRegression(C=1.0)
```

Relationship:

```text
Small C
    ↓
Strong Regularization

Large C
    ↓
Weak Regularization
```

Example:

```python
LogisticRegression(C=0.1)
```

means stronger regularization.

```python
LogisticRegression(C=10)
```

means weaker regularization.

---

### 11. Logistic Regression Pipeline

For datasets containing both numerical and categorical features:

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression


numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])


categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])


preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])


model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(
        penalty="l2",
        C=1.0,
        max_iter=1000
    ))
])


model.fit(X_train, y_train)
```

---

### 12. Logistic Regression — Complete Flow

```text
Input Features
      ↓
Linear Equation
z = β0 + β1X1 + β2X2 + ...
      ↓
Sigmoid Function
      ↓
Probability (0 → 1)
      ↓
Decision Threshold
      ↓
Class Prediction
```

### Key Interview Points

* **Logistic Regression → Classification**
* **Sigmoid → Converts linear output into probability**
* **Probability → Value between 0 and 1**
* **Decision Boundary → Separates classes**
* **Binary Classification → 2 classes**
* **Multiclass Classification → 3 or more classes**
* **Log Loss → Measures probability prediction error**
* **L1 → Can perform feature selection**
* **L2 → Shrinks coefficients and controls overfitting**
* **C → Inverse of regularization strength**
