# Logistic Regression — Complete Guide + Project

A simple, practical guide to Logistic Regression covering:

- Sigmoid function
- Probability
- Decision boundary
- Binary classification
- Multiclass classification
- Log Loss / Cross Entropy
- L1 and L2 regularization
- Complete end-to-end project

---

## 1. What is Logistic Regression?

Logistic Regression is a **supervised machine learning classification algorithm**.

Despite the word "Regression", it is mainly used for predicting classes.

### Examples

| Problem | Output |
|---|---|
| Email → Spam / Not Spam | Binary |
| Customer → Buy / Not Buy | Binary |
| Student → Pass / Fail | Binary |
| Image → Cat / Dog / Horse | Multiclass |
| Customer → Low / Medium / High risk | Multiclass |

The model first calculates a score and then converts that score into a probability between `0` and `1`.

---

# 2. Why Logistic Regression?

Linear Regression predicts continuous values:

```text
House price = 250000
Temperature = 32.5
Salary = 75000
```

But classification needs class probabilities:

```text
Spam probability = 0.91
Not Spam probability = 0.09
```

Logistic Regression solves this by using the **Sigmoid function**.

---

# 3. How Logistic Regression Works

The basic flow is:

```text
Input Features
      ↓
Linear Equation
      ↓
Weighted Score (z)
      ↓
Sigmoid Function
      ↓
Probability
      ↓
Threshold
      ↓
Class Prediction
```

The linear equation is:

```text
z = b0 + b1*x1 + b2*x2 + ... + bn*xn
```

Where:

- `x` = input feature
- `b` = model weight
- `b0` = bias/intercept
- `z` = model score

Then:

```text
probability = sigmoid(z)
```

---

# 4. Sigmoid Function

The sigmoid function converts any number into a value between `0` and `1`.

Formula:

```text
σ(z) = 1 / (1 + e^(-z))
```

### Example

If:

```text
z = 0
```

then:

```text
sigmoid(0) = 0.5
```

If:

```text
z = 2
```

then:

```text
sigmoid(2) ≈ 0.88
```

If:

```text
z = -2
```

then:

```text
sigmoid(-2) ≈ 0.12
```

So:

```text
z → -∞     probability → 0
z = 0      probability = 0.5
z → +∞     probability → 1
```

### Python

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

print(sigmoid(-2))
print(sigmoid(0))
print(sigmoid(2))
```

---

# 5. Probability

Logistic Regression produces a probability.

Suppose:

```text
P(Spam) = 0.90
```

This means the model estimates a 90% probability that the email is spam.

Usually we select a threshold:

```text
probability >= 0.5 → class 1
probability < 0.5  → class 0
```

Example:

```text
0.91 → Spam
0.73 → Spam
0.49 → Not Spam
0.12 → Not Spam
```

The threshold does not have to be `0.5`. In some applications we may use `0.3`, `0.7`, etc., depending on the business requirement.

---

# 6. Decision Boundary

The **decision boundary** is the point where the model changes from one class to another.

For the common threshold `0.5`:

```text
sigmoid(z) = 0.5
```

This happens when:

```text
z = 0
```

Therefore the decision boundary is:

```text
b0 + b1*x1 + b2*x2 + ... + bn*xn = 0
```

### Simple example

Suppose:

```text
z = -4 + 2*x
```

Decision boundary:

```text
-4 + 2*x = 0
2*x = 4
x = 2
```

So:

```text
x < 2  → Class 0
x >= 2 → Class 1
```

---

# 7. Binary Classification

Binary classification has exactly two classes.

Example:

```text
0 = Not Purchased
1 = Purchased
```

Suppose the model predicts:

```text
P(Purchased) = 0.82
```

With threshold `0.5`:

```text
0.82 >= 0.5
```

Prediction:

```text
1 = Purchased
```

### Python

```python
probability = 0.82

if probability >= 0.5:
    prediction = 1
else:
    prediction = 0

print(prediction)
```

---

# 8. Multiclass Classification

Multiclass classification has more than two classes.

Example:

```text
0 = Cat
1 = Dog
2 = Horse
```

Logistic Regression can handle multiclass classification.

Two common approaches are:

### One-vs-Rest (OvR)

Train one classifier for each class.

```text
Classifier 1 → Cat vs Not Cat
Classifier 2 → Dog vs Not Dog
Classifier 3 → Horse vs Not Horse
```

The class with the highest score/probability is selected.

### Multinomial Logistic Regression

The model directly estimates probabilities for all classes.

Example:

```text
Cat   = 0.10
Dog   = 0.75
Horse = 0.15
```

Prediction:

```text
Dog
```

In scikit-learn:

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(
    multi_class="multinomial",
    max_iter=1000
)
```

Note: newer scikit-learn versions may handle multinomial behavior automatically depending on the solver and configuration, so check the version-specific API when writing production code.

---

# 9. Log Loss

Log Loss measures how good the predicted probabilities are.

For binary classification:

```text
Log Loss =
-y*log(p) - (1-y)*log(1-p)
```

Where:

- `y` = actual class
- `p` = predicted probability

The important idea:

> Correct and confident predictions get low loss. Wrong and confident predictions get very high loss.

### Example

Actual:

```text
y = 1
```

Prediction:

```text
p = 0.90
```

This is a good prediction → low loss.

But:

```text
p = 0.01
```

This is a very confident wrong prediction → very high loss.

Therefore, Log Loss encourages the model to produce good probabilities, not only correct class labels.

### Why not only use Accuracy?

Consider:

```text
Actual = 1
Prediction probability = 0.51
```

and:

```text
Actual = 1
Prediction probability = 0.99
```

Both may be classified correctly using a 0.5 threshold, but the second prediction is much more confident.

Log Loss captures this difference.

---

# 10. L1 Regularization

L1 regularization adds a penalty based on the absolute values of model weights.

Conceptually:

```text
Loss + λ * Σ|weights|
```

`λ` controls the regularization strength.

### Main effect

L1 can push some weights exactly to zero.

Example:

```text
Before:

age       = 1.2
salary    = 0.8
city      = 0.03
browser   = 0.01

After L1:

age       = 1.1
salary    = 0.7
city      = 0
browser   = 0
```

This can make L1 useful for:

- Feature selection
- High-dimensional datasets
- Sparse models

In scikit-learn:

```python
model = LogisticRegression(
    penalty="l1",
    solver="liblinear"
)
```

---

# 11. L2 Regularization

L2 regularization penalizes squared weights.

Conceptually:

```text
Loss + λ * Σ(weight²)
```

L2 usually makes weights smaller rather than forcing many of them exactly to zero.

Example:

```text
Before:

age       = 2.5
salary    = 1.8
experience = 1.2

After L2:

age       = 1.8
salary    = 1.3
experience = 0.9
```

L2 is commonly used because it helps reduce overfitting while keeping the model stable.

In scikit-learn:

```python
model = LogisticRegression(
    penalty="l2",
    solver="lbfgs"
)
```

---

# 12. L1 vs L2

| Feature | L1 | L2 |
|---|---|---|
| Penalty | `|w|` | `w²` |
| Can make weights zero | Yes | Usually no |
| Feature selection | Good | Not the main purpose |
| Sparse model | Yes | Usually no |
| Common use | High-dimensional data | General regularization |

Easy memory trick:

```text
L1 → Some weights become 0
L2 → Weights become smaller
```

---

# 13. C Parameter in Scikit-Learn

Scikit-learn's `LogisticRegression` commonly uses `C`.

Important:

```text
C = inverse of regularization strength
```

Therefore:

```text
Small C → stronger regularization
Large C → weaker regularization
```

Example:

```python
LogisticRegression(C=0.1)
```

has stronger regularization than:

```python
LogisticRegression(C=10)
```

---

# 14. Complete Machine Learning Workflow

A practical Logistic Regression project follows:

```text
1. Load Dataset
       ↓
2. Understand Data
       ↓
3. Clean Data
       ↓
4. EDA
       ↓
5. Split X and y
       ↓
6. Train/Test Split
       ↓
7. Preprocess Features
       ↓
8. Train Logistic Regression
       ↓
9. Predict Probability
       ↓
10. Predict Class
       ↓
11. Evaluate Model
       ↓
12. Tune Hyperparameters
       ↓
13. Save Model
       ↓
14. Build API
```

---

# 15. Project: Customer Purchase Prediction

## Project Goal

Build a machine learning model that predicts:

> Will a customer purchase a product?

Target:

```text
0 = No Purchase
1 = Purchase
```

Features:

```text
Age
Salary
WebsiteVisits
PreviousPurchases
```

---

# 16. Project Structure

```text
customer_purchase_prediction/
│
├── data/
│   └── customers.csv
│
├── models/
│   └── logistic_model.pkl
│
├── src/
│   ├── train.py
│   ├── predict.py
│   └── evaluate.py
│
├── requirements.txt
└── README.md
```

---

# 17. Install Libraries

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib
```

`requirements.txt`:

```text
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
```

---

# 18. Dataset Example

`customers.csv`

```csv
Age,Salary,WebsiteVisits,PreviousPurchases,Purchased
22,25000,3,0,0
25,30000,5,1,0
28,35000,7,1,1
35,50000,8,3,1
42,70000,10,5,1
21,22000,2,0,0
31,45000,6,2,1
26,28000,4,0,0
45,80000,12,6,1
24,27000,3,0,0
```

For a real project, use a much larger dataset.

---

# 19. Load Dataset

```python
import pandas as pd

df = pd.read_csv("data/customers.csv")

print(df.head())
print(df.info())
print(df.describe())
```

---

# 20. Separate Features and Target

```python
X = df.drop("Purchased", axis=1)
y = df["Purchased"]
```

Here:

```text
X = input features
y = target
```

---

# 21. Train/Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

Meaning:

```text
80% → Training
20% → Testing
```

`stratify=y` helps preserve the class distribution in the train and test sets.

---

# 22. Feature Scaling

Logistic Regression often benefits from scaling, especially when features have very different ranges.

Example:

```text
Age = 25
Salary = 50000
WebsiteVisits = 5
```

Salary is much larger numerically.

Use:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Important:

```text
fit_transform → training data
transform      → test data
```

Never fit the scaler separately on the test set.

---

# 23. Train Logistic Regression

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(
    penalty="l2",
    C=1.0,
    max_iter=1000
)

model.fit(X_train_scaled, y_train)
```

---

# 24. Predict Classes

```python
y_pred = model.predict(X_test_scaled)

print(y_pred)
```

Example:

```text
[0, 1, 1, 0, 1]
```

---

# 25. Predict Probabilities

```python
y_prob = model.predict_proba(X_test_scaled)

print(y_prob)
```

Example:

```text
[
 [0.90, 0.10],
 [0.15, 0.85],
 [0.20, 0.80]
]
```

For class `1`:

```python
probability = model.predict_proba(X_test_scaled)[:, 1]
```

---

# 26. Evaluate Accuracy

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
```

---

# 27. Confusion Matrix

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print(cm)
```

The four important outcomes are:

```text
TP = True Positive
TN = True Negative
FP = False Positive
FN = False Negative
```

---

# 28. Classification Report

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

It provides:

```text
Precision
Recall
F1-score
Support
```

---

# 29. Log Loss Evaluation

```python
from sklearn.metrics import log_loss

loss = log_loss(y_test, probability)

print("Log Loss:", loss)
```

Lower Log Loss is generally better.

---

# 30. ROC-AUC

```python
from sklearn.metrics import roc_auc_score

auc = roc_auc_score(y_test, probability)

print("ROC-AUC:", auc)
```

ROC-AUC evaluates how well the model separates the two classes across thresholds.

---

# 31. Complete Training Code

```python
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    log_loss,
    roc_auc_score
)

# 1. Load data
df = pd.read_csv("data/customers.csv")

# 2. X and y
X = df.drop("Purchased", axis=1)
y = df["Purchased"]

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 4. Scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Model
model = LogisticRegression(
    penalty="l2",
    C=1.0,
    max_iter=1000
)

# 6. Training
model.fit(X_train_scaled, y_train)

# 7. Prediction
y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:, 1]

# 8. Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Log Loss:", log_loss(y_test, y_prob))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 9. Save model and scaler
joblib.dump(model, "models/logistic_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Model saved successfully.")
```

---

# 32. Predict a New Customer

```python
import joblib
import numpy as np

model = joblib.load("models/logistic_model.pkl")
scaler = joblib.load("models/scaler.pkl")

customer = np.array([
    [30, 45000, 7, 2]
])

customer_scaled = scaler.transform(customer)

probability = model.predict_proba(customer_scaled)[0][1]

prediction = 1 if probability >= 0.5 else 0

print("Purchase Probability:", probability)
print("Prediction:", prediction)
```

Example:

```text
Purchase Probability: 0.82
Prediction: 1
```

Meaning:

```text
Customer is likely to purchase.
```

---

# 33. Custom Decision Threshold

The default threshold is commonly:

```text
0.5
```

But you can change it.

```python
threshold = 0.7

prediction = (probability >= threshold).astype(int)
```

Why?

Suppose fraud detection is more important than missing some legitimate transactions. You may choose a lower or higher threshold depending on the business objective.

Always select the threshold using validation data and the cost of FP/FN rather than choosing it arbitrarily.

---

# 34. L1 Model

```python
l1_model = LogisticRegression(
    penalty="l1",
    solver="liblinear",
    C=1.0,
    max_iter=1000
)

l1_model.fit(X_train_scaled, y_train)
```

Check coefficients:

```python
print(l1_model.coef_)
```

Some coefficients may become:

```text
0
```

---

# 35. L2 Model

```python
l2_model = LogisticRegression(
    penalty="l2",
    C=1.0,
    solver="lbfgs",
    max_iter=1000
)

l2_model.fit(X_train_scaled, y_train)
```

Compare:

```python
print("L1:", l1_model.coef_)
print("L2:", l2_model.coef_)
```

---

# 36. Hyperparameter Tuning

Use GridSearchCV:

```python
from sklearn.model_selection import GridSearchCV

params = {
    "C": [0.01, 0.1, 1, 10, 100],
    "penalty": ["l2"]
}

grid = GridSearchCV(
    LogisticRegression(max_iter=1000),
    params,
    cv=5,
    scoring="accuracy"
)

grid.fit(X_train_scaled, y_train)

print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)
```

---

# 37. Better Production Approach: Pipeline

Instead of manually scaling and training separately:

```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
y_prob = pipeline.predict_proba(X_test)[:, 1]
```

This is safer and cleaner because preprocessing and model training are packaged together.

---

# 38. Important Concepts to Remember

### Sigmoid

```text
Converts score → probability
```

### Probability

```text
Value between 0 and 1
```

### Threshold

```text
Probability → Class
```

### Decision Boundary

```text
Where the predicted class changes
```

### Binary Classification

```text
Two classes
```

### Multiclass Classification

```text
More than two classes
```

### Log Loss

```text
Measures quality of predicted probabilities
```

### L1

```text
Can make coefficients zero
```

### L2

```text
Shrinks coefficients
```

### C

```text
Smaller C → stronger regularization
Larger C  → weaker regularization
```

---

# 39. Interview Questions

### Q1. Why is Logistic Regression called regression?

Because it models a linear relationship in the log-odds space, even though its final use is classification.

### Q2. Why do we use sigmoid?

To convert the model score into a value between `0` and `1`, which can be interpreted as a probability for binary classification.

### Q3. What is the default threshold?

Commonly `0.5`, although the threshold can be changed.

### Q4. What happens when probability = 0.5?

For a threshold of `0.5`, it is typically assigned to class `1` by a `>= 0.5` rule. Exact behavior can depend on implementation.

### Q5. What is decision boundary?

The boundary where the model changes its predicted class.

### Q6. Why use Log Loss?

Because it evaluates predicted probabilities and heavily penalizes confident wrong predictions.

### Q7. L1 vs L2?

```text
L1 → sparse coefficients / feature selection
L2 → coefficient shrinkage
```

### Q8. What does C mean?

`C` is the inverse of regularization strength in scikit-learn's Logistic Regression.

### Q9. Can Logistic Regression handle multiclass?

Yes. It can use approaches such as One-vs-Rest or multinomial logistic regression depending on configuration.

### Q10. Why scale features?

Scaling puts features on comparable numerical ranges and can make optimization more stable, especially when feature magnitudes differ significantly.

---

# 40. Final Mental Model

Remember Logistic Regression like this:

```text
                FEATURES
                   ↓
             Linear Equation
                   ↓
            z = wX + b
                   ↓
              SIGMOID
                   ↓
          Probability 0 → 1
                   ↓
              Threshold
                   ↓
          Class 0 / Class 1
```

Training:

```text
Prediction
    ↓
Compare with actual value
    ↓
Log Loss
    ↓
Regularization
    ↓
Update weights
    ↓
Repeat
```

Final project:

```text
Customer Data
     ↓
Preprocessing
     ↓
Train/Test Split
     ↓
Scaling
     ↓
Logistic Regression
     ↓
Probability
     ↓
Threshold
     ↓
Purchase Prediction
     ↓
Accuracy + Precision + Recall + F1 + ROC-AUC + Log Loss
     ↓
Save Model
     ↓
API / Django / Flask Deployment
```

---

## What to Practice Next

1. Implement the customer purchase project from scratch.
2. Plot the sigmoid function.
3. Change the classification threshold from `0.5` to `0.3`, `0.7`.
4. Compare L1 and L2 coefficients.
5. Compare Logistic Regression with Decision Tree and Random Forest.
6. Build a Flask/Django prediction API.
7. Deploy the trained model.
