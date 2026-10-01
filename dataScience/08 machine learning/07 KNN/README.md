# KNN + Stacking — Machine Learning

## 1. What is KNN?

**KNN (K-Nearest Neighbors)** is a supervised machine learning algorithm used for:

* Classification
* Regression

KNN does not build a traditional mathematical model during training.

Instead, it stores the training data and makes predictions by looking at the **nearest data points**.

### Simple Example

Suppose we want to predict whether a person will buy a product.

| Age | Income | Bought |
| --: | -----: | ------ |
|  22 |  25000 | No     |
|  25 |  30000 | No     |
|  35 |  60000 | Yes    |
|  40 |  70000 | Yes    |
|  38 |  65000 | Yes    |

For a new customer:

```text
Age = 36
Income = 62000
```

KNN finds the closest customers.

If most of the nearest customers bought the product:

```text
Prediction = Yes
```

---

# 2. How KNN Works

KNN follows these basic steps:

```text
Step 1 → Choose K
Step 2 → Calculate distance
Step 3 → Find K nearest points
Step 4 → Classification → Majority voting
          Regression     → Average
Step 5 → Return prediction
```

---

# 3. What is K?

`K` represents the number of nearest neighbors considered for prediction.

Example:

```python
K = 3
```

means:

> Look at the 3 closest training examples.

### K = 1

Only the nearest point is considered.

```text
Very sensitive to noise
Low bias
High variance
```

### Large K

More points participate.

```text
Less sensitive to noise
Higher bias
Lower variance
```

---

# 4. KNN Classification

In classification, KNN uses **majority voting**.

Example:

```text
K = 5

Neighbor 1 → Cat
Neighbor 2 → Dog
Neighbor 3 → Cat
Neighbor 4 → Cat
Neighbor 5 → Dog
```

Votes:

```text
Cat = 3
Dog = 2
```

Prediction:

```text
Cat
```

### Python Example

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# Load dataset
data = load_iris()

X = data.data
y = data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create KNN model
model = KNeighborsClassifier(n_neighbors=5)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
```

---

# 5. Why Scaling is Important in KNN

KNN calculates distances.

Suppose we have:

```text
Age       = 25
Salary    = 80000
```

Without scaling, salary has a much larger numerical range.

Therefore salary can dominate the distance calculation.

### Bad

```text
Age       → 25
Salary    → 80000
```

### Better

After StandardScaler:

```text
Age       → -0.45
Salary    → 0.72
```

Therefore, scaling is generally important for KNN.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

---

# 6. Distance Metrics

KNN needs a method to calculate the distance between data points.

Common distance metrics include:

1. Euclidean
2. Manhattan
3. Minkowski
4. Cosine distance

---

## 6.1 Euclidean Distance

The most common distance metric.

For two points:

```text
A = (x1, y1)
B = (x2, y2)
```

Euclidean distance measures straight-line distance.

Example:

```text
A = (1, 2)
B = (4, 6)
```

Python:

```python
from math import sqrt

distance = sqrt(
    (4 - 1) ** 2 +
    (6 - 2) ** 2
)

print(distance)
```

Output:

```text
5.0
```

In sklearn:

```python
model = KNeighborsClassifier(
    n_neighbors=5,
    metric="euclidean"
)
```

---

# 7. Manhattan Distance

Manhattan distance measures distance along each dimension.

Example:

```text
A = (1, 2)
B = (4, 6)
```

```python
distance = abs(4 - 1) + abs(6 - 2)

print(distance)
```

Output:

```text
7
```

Using sklearn:

```python
model = KNeighborsClassifier(
    n_neighbors=5,
    metric="manhattan"
)
```

---

# 8. Minkowski Distance

Minkowski is a generalized distance metric.

```python
model = KNeighborsClassifier(
    n_neighbors=5,
    metric="minkowski"
)
```

For:

```text
p = 2
```

Minkowski behaves like Euclidean distance.

For:

```text
p = 1
```

Minkowski behaves like Manhattan distance.

Example:

```python
model = KNeighborsClassifier(
    n_neighbors=5,
    metric="minkowski",
    p=2
)
```

---

# 9. Cosine Distance

Cosine distance focuses on the **direction/angle** between vectors rather than their magnitude.

It is commonly useful for:

* Text
* Document similarity
* High-dimensional vectors

Example:

```python
model = KNeighborsClassifier(
    n_neighbors=5,
    metric="cosine"
)
```

---

# 10. Choosing the Value of K

Choosing K is important.

### Small K

Example:

```text
K = 1
K = 3
```

Advantages:

* Captures local patterns
* Flexible

Disadvantages:

* Sensitive to noise
* Can overfit

### Large K

Example:

```text
K = 50
K = 100
```

Advantages:

* More stable
* Less affected by individual noisy points

Disadvantages:

* Can underfit
* May ignore local patterns

---

# 11. Finding the Best K

We can test multiple values of K.

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

for k in range(1, 16):

    model = KNeighborsClassifier(
        n_neighbors=k
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print(
        f"K={k}, Accuracy={accuracy:.4f}"
    )
```

A better production approach is **cross-validation**.

```python
from sklearn.model_selection import GridSearchCV

params = {
    "n_neighbors": range(1, 21),
    "metric": ["euclidean", "manhattan"]
}

grid = GridSearchCV(
    KNeighborsClassifier(),
    params,
    cv=5,
    scoring="accuracy"
)

grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)
```

---

# 12. Odd K and Ties

For binary classification, an odd K can reduce the chance of a tie.

Example:

```text
K = 5

Class A → 3 votes
Class B → 2 votes
```

Clear prediction:

```text
Class A
```

But:

```text
K = 4

Class A → 2
Class B → 2
```

There is a tie.

However, simply choosing an odd K is **not a replacement for model validation**.

---

# 13. KNN Regression

KNN can also be used for regression.

Instead of majority voting, KNN regression calculates the average of the neighbors' target values.

Example:

```text
Neighbor 1 → ₹50,000
Neighbor 2 → ₹55,000
Neighbor 3 → ₹60,000
```

Prediction:

```text
(50000 + 55000 + 60000) / 3
= ₹55,000
```

### Python Example

```python
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_diabetes

data = load_diabetes()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsRegressor(
    n_neighbors=5
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(
    y_test,
    y_pred
)

print("MSE:", mse)
```

---

# 14. Curse of Dimensionality

The **curse of dimensionality** is an important problem for KNN.

As the number of features increases:

```text
2 dimensions
     ↓
10 dimensions
     ↓
100 dimensions
     ↓
1000 dimensions
```

Data points become increasingly sparse.

Distances between points also become less informative for identifying meaningful neighbors.

### Example

Imagine finding nearby houses.

With:

```text
2 features:
Area
Price
```

Finding similar houses is relatively easy.

Now consider:

```text
100 features
```

including:

```text
Area
Price
Bedrooms
Bathrooms
Age
Location
...
```

The concept of "nearest" can become less useful as dimensionality increases.

### Solutions

Common approaches:

```text
Feature selection
        ↓
Dimensionality reduction
        ↓
PCA
        ↓
Remove irrelevant features
        ↓
Use appropriate distance metric
```

Example:

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=10)

X_train_reduced = pca.fit_transform(X_train)
X_test_reduced = pca.transform(X_test)
```

---

# 15. Weighted KNN

Normal KNN gives equal voting weight to neighbors.

Weighted KNN gives closer neighbors more importance.

```python
model = KNeighborsClassifier(
    n_neighbors=5,
    weights="distance"
)
```

Compare:

```text
weights="uniform"
```

Every neighbor has equal importance.

```text
weights="distance"
```

Closer neighbors have more influence.

---

# 16. Stacking

**Stacking** is an ensemble learning technique.

Instead of relying on only one model, we combine multiple different models.

Example:

```text
                Dataset
                   |
        -------------------------
        |           |           |
       KNN       Logistic     Random
                 Regression    Forest
        |           |           |
        -------------------------
                   |
              Meta Learner
                   |
               Prediction
```

The first-level models are called:

```text
Base Learners
```

The final model is called:

```text
Meta Learner
```

---

# 17. Why Stacking?

Different models can learn different patterns.

For example:

```text
KNN
→ local similarity

Logistic Regression
→ linear relationship

Random Forest
→ non-linear relationships
```

Stacking combines their predictions.

---

# 18. Base Learners

Base learners are the models that make the initial predictions.

Example:

```python
KNN
Random Forest
Logistic Regression
```

Their outputs can look like:

```text
KNN                 → 0.80
Logistic Regression → 0.65
Random Forest       → 0.90
```

These predictions become input for the meta learner.

---

# 19. Meta Learner

The **meta learner** learns how to combine predictions from the base models.

Example:

```text
KNN prediction       → 0.80
Random Forest        → 0.90
Logistic Regression  → 0.65
                         |
                         ↓
                    Meta Learner
                         |
                         ↓
                    Final prediction
```

Common meta learners:

```text
Logistic Regression
Linear Regression
Random Forest
Gradient Boosting
```

---

# 20. Stacking Classification Example

Scikit-learn provides `StackingClassifier`.

```python
from sklearn.ensemble import (
    StackingClassifier,
    RandomForestClassifier
)

from sklearn.neighbors import KNeighborsClassifier

from sklearn.linear_model import LogisticRegression

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.pipeline import make_pipeline

from sklearn.metrics import accuracy_score
```

Load data:

```python
data = load_iris()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

Create base models:

```python
knn = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(
        n_neighbors=5
    )
)

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

Create meta learner:

```python
meta_model = LogisticRegression(
    max_iter=1000
)
```

Create stacking model:

```python
stacking_model = StackingClassifier(
    estimators=[
        ("knn", knn),
        ("random_forest", rf)
    ],
    final_estimator=meta_model
)
```

Train:

```python
stacking_model.fit(
    X_train,
    y_train
)
```

Predict:

```python
y_pred = stacking_model.predict(
    X_test
)
```

Evaluate:

```python
accuracy = accuracy_score(
    y_test,
    y_pred
)

print("Stacking Accuracy:", accuracy)
```

---

# 21. Stacking Regression

For regression, use `StackingRegressor`.

```python
from sklearn.ensemble import (
    StackingRegressor,
    RandomForestRegressor
)

from sklearn.neighbors import KNeighborsRegressor

from sklearn.linear_model import LinearRegression

from sklearn.pipeline import make_pipeline

from sklearn.preprocessing import StandardScaler
```

Create models:

```python
knn = make_pipeline(
    StandardScaler(),
    KNeighborsRegressor(
        n_neighbors=5
    )
)

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
```

Create stacking model:

```python
stacking_model = StackingRegressor(
    estimators=[
        ("knn", knn),
        ("random_forest", rf)
    ],
    final_estimator=LinearRegression()
)
```

Train:

```python
stacking_model.fit(
    X_train,
    y_train
)
```

Predict:

```python
y_pred = stacking_model.predict(
    X_test
)
```

---

# 22. Voting vs Stacking

These two concepts are often confused.

## Voting

Voting combines predictions directly.

```text
Model A → Yes
Model B → Yes
Model C → No

Majority → Yes
```

There is no separate model learning how to combine them.

---

## Stacking

Stacking uses another model to learn how to combine predictions.

```text
Model A → Prediction
Model B → Prediction
Model C → Prediction
             |
             ↓
        Meta Learner
             |
             ↓
      Final Prediction
```

### Main Difference

| Voting                      | Stacking                          |
| --------------------------- | --------------------------------- |
| Combines predictions        | Learns how to combine predictions |
| No meta learner             | Uses meta learner                 |
| Simpler                     | More flexible                     |
| Usually easier to interpret | More complex                      |

---

# 23. Complete KNN + Stacking Example

```python
from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.pipeline import make_pipeline

from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import (
    RandomForestClassifier,
    StackingClassifier
)

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report
)


# --------------------------------
# 1. Load Dataset
# --------------------------------

data = load_iris()

X = data.data
y = data.target


# --------------------------------
# 2. Train/Test Split
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# --------------------------------
# 3. KNN
# --------------------------------

knn = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(
        n_neighbors=5,
        metric="euclidean",
        weights="distance"
    )
)


# --------------------------------
# 4. Random Forest
# --------------------------------

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# --------------------------------
# 5. Meta Learner
# --------------------------------

meta_learner = LogisticRegression(
    max_iter=1000
)


# --------------------------------
# 6. Stacking
# --------------------------------

stacking = StackingClassifier(
    estimators=[
        ("knn", knn),
        ("random_forest", rf)
    ],
    final_estimator=meta_learner
)


# --------------------------------
# 7. Train
# --------------------------------

stacking.fit(
    X_train,
    y_train
)


# --------------------------------
# 8. Predict
# --------------------------------

y_pred = stacking.predict(
    X_test
)


# --------------------------------
# 9. Evaluation
# --------------------------------

print(
    "Accuracy:",
    accuracy_score(y_test, y_pred)
)

print(
    classification_report(
        y_test,
        y_pred
    )
)
```

---

# 24. Important KNN Hyperparameters

```python
KNeighborsClassifier(
    n_neighbors=5,
    weights="uniform",
    algorithm="auto",
    leaf_size=30,
    p=2,
    metric="minkowski"
)
```

### `n_neighbors`

Controls K.

```python
n_neighbors=5
```

### `weights`

```python
weights="uniform"
```

Equal weight.

```python
weights="distance"
```

Closer points get greater influence.

### `metric`

```python
metric="euclidean"
```

or:

```python
metric="manhattan"
```

or:

```python
metric="cosine"
```

---

# 25. KNN Advantages

### Advantages

* Simple to understand
* Easy to implement
* No complex training phase
* Useful for classification and regression
* Can model non-linear decision boundaries

### Disadvantages

* Prediction can be expensive for large datasets
* Sensitive to feature scaling
* Sensitive to irrelevant features
* Can suffer from curse of dimensionality
* Choosing K is important
* Requires storing training data

---

# 26. Stacking Advantages

### Advantages

* Combines different algorithms
* Can capture different types of patterns
* Can improve predictive performance in some datasets
* Flexible choice of base learners and meta learner

### Disadvantages

* More complex than a single model
* More computationally expensive
* Can overfit if designed poorly
* Requires careful validation
* Harder to interpret

---

# 27. Real-Life Example

Imagine an e-commerce company wants to predict:

```text
Will customer buy a product?
```

We use:

### Model 1 — KNN

Looks at similar customers.

```text
Similar customers mostly bought
→ Buy
```

### Model 2 — Random Forest

Looks at non-linear relationships.

```text
Income + visits + age + previous purchases
→ Buy probability
```

### Model 3 — Logistic Regression

Looks at linear relationships.

```text
Features
→ Buy probability
```

Stacking combines these:

```text
                 Customer Data
                      |
          -------------------------
          |           |           |
         KNN      Random Forest   LR
          |           |           |
          -------- Predictions ----
                      |
                      ↓
                 Meta Learner
                      |
                      ↓
                Final Prediction
```

---

# 28. Interview Questions

### Q1. What is KNN?

KNN is a supervised learning algorithm that predicts a sample using its nearest training examples.

### Q2. What does K represent?

K represents the number of nearest neighbors used for prediction.

### Q3. Why is feature scaling important in KNN?

Because KNN uses distance calculations, features with larger numerical ranges can dominate the distance.

### Q4. What happens when K is too small?

The model can become sensitive to noise and may overfit.

### Q5. What happens when K is too large?

The model can become overly smooth and may underfit.

### Q6. What is the curse of dimensionality?

As the number of dimensions/features increases, data becomes sparse and distance-based methods such as KNN can become less effective.

### Q7. How does KNN regression work?

It predicts using the target values of neighboring samples, commonly their average.

### Q8. What is stacking?

Stacking is an ensemble technique where predictions from multiple base models are provided to a meta learner.

### Q9. What is a meta learner?

The model that learns how to combine the predictions of the base learners.

### Q10. Voting vs stacking?

Voting combines predictions directly, while stacking uses a meta learner to learn how to combine them.

---

# 29. Quick Revision

```text
KNN
│
├── Classification
│   └── Majority Voting
│
├── Regression
│   └── Average / Weighted Average
│
├── Distance
│   ├── Euclidean
│   ├── Manhattan
│   ├── Minkowski
│   └── Cosine
│
├── K
│   ├── Small K → High variance
│   └── Large K → High bias
│
├── Scaling
│   └── Important for distance-based algorithms
│
├── Curse of Dimensionality
│   └── More dimensions → less useful distances
│
└── Stacking
    │
    ├── Base Learner 1
    ├── Base Learner 2
    ├── Base Learner 3
    │
    └── Meta Learner
          ↓
      Final Prediction
```

---

# 30. One-Line Memory Trick

```text
KNN = Find Neighbors → Vote/Average → Predict

Voting = Models Vote

Stacking = Models Predict → Meta Model Learns → Final Prediction

Small K = Sensitive
Large K = Smooth

More Features = Curse of Dimensionality
```

---

## Recommended Practice Project

Build:

**Customer Purchase Prediction using KNN + Stacking**

Features:

```text
Age
AnnualIncome
WebsiteVisits
AppUsageHours
PreviousPurchases
```

Target:

```text
Purchased
```

Pipeline:

```text
CSV
 ↓
Data Cleaning
 ↓
Train/Test Split
 ↓
Feature Scaling
 ↓
KNN
 ↓
Random Forest
 ↓
Logistic Regression
 ↓
Stacking
 ↓
Evaluation
 ↓
Flask/FastAPI API
```

Suggested evaluation:

```text
Accuracy
Precision
Recall
F1-Score
Confusion Matrix
ROC-AUC
```
