# 📊 Train / Test / Validation

A simple and beginner-friendly guide to:

* Train-Test Split
* Training Data
* Validation Data
* Testing Data
* Cross-Validation
* Overfitting
* Underfitting
* Bias
* Variance
* Bias-Variance Tradeoff

---

# 1. Why Do We Split Data?

Suppose we have a dataset containing **10,000 records**.

If we train and evaluate the model on exactly the same data, the model may simply memorize the training examples.

We want to know:

> **Can the model perform well on data it has never seen before?**

That's why we separate data into different parts.

```text
                    Dataset
                       │
          ┌────────────┴────────────┐
          ↓                         ↓
      Training                    Testing
        Data                       Data
          │                         │
      Learn patterns          Final evaluation
```

---

# 2. Training Data

Training data is the data used to **teach the model**.

Example:

```text
10,000 records

Training = 8,000
Testing  = 2,000
```

The model learns patterns from those 8,000 records.

```text
Training Data
      ↓
ML Algorithm
      ↓
Trained Model
```

---

# 3. Testing Data

Testing data is **unseen data** used to evaluate the final model.

The model should not learn from the test set.

```text
Training Data
     ↓
Train Model
     ↓
Final Model
     ↓
Test Data
     ↓
Final Performance
```

### Important

> The test set should ideally be used only for final evaluation.

---

# 4. Train-Test Split

The most common split is:

```text
80% → Training
20% → Testing
```

Example:

```python id="p3y4w1"
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

Here:

```text
test_size=0.2
```

means 20% of the data is used for testing.

---

# 5. Why `random_state=42`?

`random_state` makes the split **reproducible**.

Without it:

```text
Run 1 → Different split
Run 2 → Different split
Run 3 → Different split
```

With:

```python id="x6t5m4"
random_state=42
```

you generally get the same split when running the same code on the same data.

The number `42` has no special mathematical meaning here. You can use another fixed integer.

---

# 6. Train / Validation / Test Split

Sometimes we need **three datasets**.

```text
Dataset
   │
   ├── Training Data
   ├── Validation Data
   └── Testing Data
```

Example:

```text
70% → Training
15% → Validation
15% → Testing
```

### Purpose

| Dataset    | Purpose               |
| ---------- | --------------------- |
| Training   | Learn patterns        |
| Validation | Select/tune the model |
| Testing    | Final evaluation      |

---

# 7. Why Do We Need Validation Data?

Suppose we have several models:

```text
Model A
Model B
Model C
```

We don't want to choose the best model based on the test set.

Instead:

```text
Training Data
     ↓
Train Models
     ↓
Validation Data
     ↓
Choose Best Model
     ↓
Final Test Data
     ↓
Final Evaluation
```

The validation set acts like a **practice exam**.

The test set is like the **final exam**.

---

# 8. Example of Train / Validation / Test

Suppose we have 10,000 records:

```text
10,000
  │
  ├── 7,000 → Training
  ├── 1,500 → Validation
  └── 1,500 → Testing
```

### Training

Model learns from:

```text
7,000 records
```

### Validation

We compare models/hyperparameters using:

```text
1,500 records
```

### Testing

After everything is finalized:

```text
1,500 records
```

are used for final evaluation.

---

# 9. What is Cross-Validation?

Cross-validation is a technique used to evaluate a model more reliably by training and validating it on different subsets of the available training data.

The most common method is:

> **K-Fold Cross-Validation**

---

# 10. K-Fold Cross-Validation

Suppose:

```text
K = 5
```

The data is divided into 5 folds.

```text
Fold 1
Fold 2
Fold 3
Fold 4
Fold 5
```

The model is trained and validated 5 times.

### Round 1

```text
Validation → Fold 1
Training   → Fold 2 + 3 + 4 + 5
```

### Round 2

```text
Validation → Fold 2
Training   → Fold 1 + 3 + 4 + 5
```

### Round 3

```text
Validation → Fold 3
Training   → Fold 1 + 2 + 4 + 5
```

### Round 4

```text
Validation → Fold 4
Training   → Fold 1 + 2 + 3 + 5
```

### Round 5

```text
Validation → Fold 5
Training   → Fold 1 + 2 + 3 + 4
```

Finally, we usually calculate the average score.

```text
Score 1
Score 2
Score 3
Score 4
Score 5
   ↓
Average Score
```

---

# 11. K-Fold Cross-Validation in Python

```python id="6g4j4r"
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()

scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="r2"
)

print("Scores:", scores)
print("Mean R²:", scores.mean())
```

Example:

```text
Scores:
[0.81, 0.84, 0.79, 0.83, 0.82]

Mean:
0.818
```

This gives us a more stable estimate than relying on one particular split.

---

# 12. Why Use Cross-Validation?

Cross-validation helps us:

* Use the training data more effectively
* Reduce dependence on one validation split
* Compare models
* Tune hyperparameters
* Detect unstable model performance

---

# 13. What is Overfitting?

Overfitting occurs when a model learns the training data **too closely**, including noise and random patterns.

Example:

```text
Training Accuracy → 99%
Validation Accuracy → 70%
```

The model performs extremely well on training data but poorly on unseen data.

### Simple Example

Imagine a student who memorizes every answer from the practice paper but doesn't understand the concepts.

Practice exam:

```text
99%
```

New exam:

```text
60%
```

That's similar to overfitting.

---

# 14. Signs of Overfitting

```text
Training Score → Very High
Validation Score → Much Lower
```

Example:

```text
Training R²   = 0.99
Validation R² = 0.65
```

Possible solutions:

* Use more training data
* Reduce model complexity
* Regularization
* Feature selection
* Early stopping for suitable models
* Cross-validation
* Pruning for decision trees
* Dropout for neural networks

---

# 15. What is Underfitting?

Underfitting happens when the model is **too simple** to learn the important patterns in the data.

Example:

```text
Training Accuracy   → 60%
Validation Accuracy → 58%
```

The model performs poorly on both training and unseen data.

### Student Example

The student studies too little:

```text
Practice → 60%
Final    → 58%
```

The student hasn't learned enough.

---

# 16. Signs of Underfitting

```text
Training Score → Low
Validation Score → Low
```

Possible solutions:

* Use a more complex model
* Add useful features
* Reduce excessive regularization
* Train for longer where appropriate
* Improve feature engineering

---

# 17. Overfitting vs Underfitting

| Overfitting                 | Underfitting              |
| --------------------------- | ------------------------- |
| Model too complex           | Model too simple          |
| Training score very high    | Training score low        |
| Validation score much lower | Validation score also low |
| Learns noise                | Doesn't learn enough      |
| High variance               | High bias                 |

### Easy Trick

```text
Overfitting
→ Too much learning

Underfitting
→ Too little learning
```

---

# 18. What is Bias?

In ML, **bias** refers to error caused by overly restrictive assumptions or an overly simple model.

A high-bias model tends to:

```text
Oversimplify the problem
        ↓
Miss important patterns
        ↓
Underfit
```

Example:

Trying to model a highly curved relationship using an overly simple straight-line model.

---

# 19. What is Variance?

Variance refers to how much a model's predictions can change when trained on different samples of the training data.

A high-variance model is very sensitive to the particular training data.

```text
Small change in training data
          ↓
Large change in model
          ↓
Overfitting
```

---

# 20. Bias vs Variance

| Bias                                          | Variance                                                 |
| --------------------------------------------- | -------------------------------------------------------- |
| Error from overly simple assumptions          | Sensitivity to training data                             |
| Usually associated with underfitting          | Usually associated with overfitting                      |
| Model too simple                              | Model too complex                                        |
| Training and validation performance both poor | Training performance high, validation performance poorer |

### Easy Trick

```text
High Bias
→ Underfitting

High Variance
→ Overfitting
```

---

# 21. Bias-Variance Tradeoff

The goal is to find a good balance between **bias and variance**.

```text
Too Simple
    ↓
High Bias
    ↓
Underfitting

       ↓

Balanced Model
       ↓
Good Generalization

       ↓

Too Complex
    ↓
High Variance
    ↓
Overfitting
```

We don't want:

```text
Very High Bias ❌
Very High Variance ❌
```

We want:

```text
Balanced Bias + Variance ✅
```

---

# 22. Example of Model Complexity

Imagine predicting house prices.

### Model 1 — Too Simple

```text
Price = Area × coefficient
```

It may miss important factors such as:

* Location
* Bedrooms
* Age
* Amenities

This can cause **underfitting**.

---

### Model 2 — Balanced

Uses relevant features and suitable complexity.

```text
Area
Bedrooms
Location
Age
Amenities
```

This may generalize well.

---

### Model 3 — Too Complex

A highly flexible model may memorize noise in the training data.

```text
Training Performance → Excellent
New Data Performance → Poor
```

This is **overfitting**.

---

# 23. Train vs Validation Performance

A useful way to diagnose models:

| Training | Validation | Possible Problem            |
| -------- | ---------- | --------------------------- |
| Low      | Low        | Underfitting / high bias    |
| High     | Low        | Overfitting / high variance |
| High     | High       | Good fit                    |
| Similar  | Similar    | Usually good generalization |

The exact interpretation depends on the metric and problem.

---

# 24. Cross-Validation vs Train-Test Split

| Train-Test Split        | Cross-Validation                   |
| ----------------------- | ---------------------------------- |
| Usually one split       | Multiple train/validation splits   |
| Faster                  | More computationally expensive     |
| Simple                  | More robust estimate               |
| Good for large datasets | Useful for model comparison/tuning |
| Example: 80/20          | Example: 5-Fold CV                 |

---

# 25. Train-Test Split + Cross-Validation

A strong practical workflow is:

```text
Complete Dataset
      ↓
Train / Test Split
      │
      ├── Training Data
      │       ↓
      │   K-Fold CV
      │       ↓
      │   Model Selection
      │       ↓
      │   Final Training
      │
      └── Test Data
              ↓
        Final Evaluation
```

The test set stays untouched until the final evaluation.

---

# 26. Cross-Validation for Hyperparameter Tuning

Suppose we have a Random Forest.

We want to find the best:

```text
n_estimators
max_depth
min_samples_split
```

We can use:

```python id="1a3v8h"
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(
    random_state=42
)

params = {
    "n_estimators": [50, 100],
    "max_depth": [5, 10, None]
}

grid = GridSearchCV(
    model,
    params,
    cv=5,
    scoring="r2"
)

grid.fit(X_train, y_train)

print(grid.best_params_)
print(grid.best_score_)
```

Here, cross-validation helps select hyperparameters without using the final test set.

---

# 27. Important: Data Leakage

Data leakage happens when information from outside the training process improperly influences model training.

### Wrong

```text
Full Dataset
     ↓
Scale Entire Dataset
     ↓
Train/Test Split
```

The test information has influenced the scaling step.

### Correct

```text
Dataset
   ↓
Train/Test Split
   ↓
Training Data → Fit Scaler
                  ↓
              Transform Train
                  ↓
              Transform Test
```

Using a pipeline is a good way to manage this safely.

---

# 28. Pipeline + Cross-Validation

Example:

```python id="jv7q5s"
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

scores = cross_val_score(
    pipeline,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)

print("CV Scores:", scores)
print("Mean Score:", scores.mean())
```

The scaler is fitted separately within each training fold, helping avoid leakage during cross-validation.

---

# 29. Complete ML Workflow

```text
                Dataset
                   ↓
             Data Cleaning
                   ↓
            Train/Test Split
              ↙          ↘
       Training Data     Test Data
             ↓               │
       Cross-Validation      │
             ↓               │
       Model Selection       │
             ↓               │
      Hyperparameter Tuning  │
             ↓               │
       Train Final Model     │
             ↓               │
             └───────┐       │
                     ↓       ↓
                  Test Model
                     ↓
               Final Evaluation
```

---

# 30. Quick Revision

| Concept                | Simple Meaning                        |
| ---------------------- | ------------------------------------- |
| Training Data          | Used to learn                         |
| Validation Data        | Used for model selection/tuning       |
| Test Data              | Used for final evaluation             |
| Train-Test Split       | Divides data into train/test          |
| Cross-Validation       | Repeated train/validation splits      |
| Overfitting            | Learns training data too much         |
| Underfitting           | Learns too little                     |
| Bias                   | Error from overly simple assumptions  |
| Variance               | Sensitivity to training data          |
| Bias-Variance Tradeoff | Balance complexity and generalization |

---

# 🎯 Interview Questions

## Q1. Why do we split data into train and test?

> We split data so that we can evaluate how well the model generalizes to unseen data.

---

## Q2. What is the difference between training and testing data?

> Training data is used to learn patterns, while testing data is kept unseen during training and used for final evaluation.

---

## Q3. What is validation data?

> Validation data is used during model development to select models, tune hyperparameters, and make decisions before final testing.

---

## Q4. What is cross-validation?

> Cross-validation evaluates a model using multiple train-validation splits, providing a more reliable estimate of its performance.

---

## Q5. What is K-Fold Cross-Validation?

> K-Fold CV divides the data into K folds and trains/evaluates the model K times, using a different fold for validation each time.

---

## Q6. What is overfitting?

> Overfitting occurs when a model learns the training data too closely, including noise, and performs poorly on unseen data.

---

## Q7. What is underfitting?

> Underfitting occurs when a model is too simple to capture important patterns, resulting in poor performance on both training and unseen data.

---

## Q8. What is bias?

> Bias is error caused by overly simple assumptions or a model that is too restrictive, often resulting in underfitting.

---

## Q9. What is variance?

> Variance describes how sensitive a model is to changes in its training data. High variance is commonly associated with overfitting.

---

## Q10. Explain the bias-variance tradeoff.

> The bias-variance tradeoff is the balance between a model being too simple and too complex. High bias can cause underfitting, while high variance can cause overfitting. The goal is to find a model that generalizes well to unseen data.

---

# ⭐ Most Important Interview Question

### "How do you prevent overfitting?"

A good answer:

> "I can use techniques such as cross-validation, regularization, feature selection, reducing model complexity, collecting more training data, and early stopping where applicable. I also monitor the difference between training and validation performance."

---

# ⭐ Another Important Question

### "How would you evaluate an ML model?"

A good answer:

> "First, I split the data into training and test sets. During model development, I can use cross-validation on the training data for model selection and hyperparameter tuning. After finalizing the model, I evaluate it once on the untouched test set using appropriate metrics."

---

# 🔥 Easy Memory Trick

```text
TRAIN
↓
Learn

VALIDATION
↓
Choose / Tune

TEST
↓
Final Check
```

```text
High Bias
↓
Underfitting

High Variance
↓
Overfitting
```

```text
Cross-Validation
↓
Multiple train/validation splits
↓
More reliable model evaluation
```

---

# 🚀 Final Cheat Sheet

```text
DATA
 │
 ├── TRAIN
 │    → Learn patterns
 │
 ├── VALIDATION
 │    → Tune / Select
 │
 └── TEST
      → Final evaluation


MODEL COMPLEXITY

Too Simple
    ↓
High Bias
    ↓
Underfitting

      ↕
Balance
      ↕

Too Complex
    ↓
High Variance
    ↓
Overfitting
```

## ⭐ Remember

> **Train = Learn, Validation = Tune, Test = Final Check**

> **High Bias = Underfitting**

> **High Variance = Overfitting**

> **Cross-Validation = Evaluate across multiple splits**
