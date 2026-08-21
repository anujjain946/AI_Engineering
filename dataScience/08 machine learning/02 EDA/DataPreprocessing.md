# 🧹 Data Preprocessing

A simple and beginner-friendly guide to **Data Preprocessing** in Machine Learning.

Topics covered:

* Missing Values
* Duplicates
* Outliers
* IQR
* Z-Score
* Imbalanced Data
* SMOTE
* Complete preprocessing workflow

---

# 1. What is Data Preprocessing?

Data preprocessing means **cleaning and preparing raw data before giving it to a Machine Learning model**.

Real-world data is usually not perfect.

It can contain:

```text id="v4ps2j"
Missing Values
Duplicates
Outliers
Wrong Data Types
Categorical Values
Imbalanced Classes
```

### Basic workflow

```text id="a8o9j4"
Raw Data
   ↓
Data Cleaning
   ↓
Handle Missing Values
   ↓
Remove Duplicates
   ↓
Handle Outliers
   ↓
Handle Imbalanced Data
   ↓
Feature Transformation
   ↓
Clean Data
   ↓
ML Model
```

---

# 2. Missing Values

## What are Missing Values?

A missing value means some data is not available.

Example:

|     Age |  Salary | Experience |
| ------: | ------: | ---------: |
|      25 |   30000 |          2 |
|      30 | **NaN** |          5 |
| **NaN** |   70000 |          8 |

Here `NaN` means the value is missing.

---

# 3. How to Find Missing Values?

Using Pandas:

```python id="b7ny4g"
df.isnull().sum()
```

Example output:

```text
Age           1
Salary        1
Experience    0
```

This tells us how many missing values each column contains.

---

# 4. How to Handle Missing Values?

There are several methods.

## Method 1 — Remove Rows

```python id="u2d4kz"
df = df.dropna()
```

This removes rows containing missing values.

### Use when:

* Very few values are missing
* Removing rows will not significantly reduce the dataset

---

# 5. Fill Missing Values with Mean

For numerical columns:

```python id="f4rqw7"
df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)
```

Example:

```text id="a3t5q6"
Age:

20
25
30
NaN
35
```

Mean:

```text id="x1r9hm"
(20 + 25 + 30 + 35) / 4
= 27.5
```

Missing value becomes:

```text id="b9x6op"
NaN → 27.5
```

---

# 6. Fill Missing Values with Median

```python id="x2c7qa"
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)
```

Median is often preferred when the column contains **outliers or is strongly skewed**.

Example:

```text id="nyc9q4"
10
20
25
30
500
```

The value `500` is an outlier.

Mean can be strongly affected by it, while median is more robust.

---

# 7. Fill Missing Categorical Values

For categorical columns, we can use the most frequent value:

```python id="k0y4pg"
df["City"] = df["City"].fillna(
    df["City"].mode()[0]
)
```

Example:

```text id="4k0l0a"
City

Ahmedabad
Delhi
Ahmedabad
NaN
Ahmedabad
```

Mode:

```text id="1fqf7q"
Ahmedabad
```

So:

```text id="l5yqz4"
NaN → Ahmedabad
```

---

# 8. Duplicates

## What are Duplicates?

Duplicates are repeated rows in the dataset.

Example:

| Name | Age | Salary |
| ---- | --: | -----: |
| Anuj |  30 |  50000 |
| Ravi |  28 |  40000 |
| Anuj |  30 |  50000 |

The first and third rows are duplicates.

---

# 9. Find Duplicates

```python id="4ijy9v"
df.duplicated().sum()
```

This returns the number of duplicate rows.

---

# 10. Remove Duplicates

```python id="iux8wm"
df = df.drop_duplicates()
```

Now repeated rows are removed.

### Important

Before removing duplicates, make sure they are truly duplicate records and not legitimate repeated observations.

---

# 11. What are Outliers?

An outlier is a data point that is **unusually far from most other observations**.

Example:

```text id="3q3jfd"
Age:

20
22
24
25
27
29
90
```

`90` may be an outlier depending on the context.

Another example:

```text id="g0q5r8"
Salary:

30000
35000
40000
45000
5000000
```

`5000000` is extremely different from the other values.

---

# 12. Why are Outliers a Problem?

Outliers can:

* Distort the mean
* Affect standard deviation
* Influence Linear Regression
* Affect some ML algorithms
* Make statistical analysis misleading

However:

> **An outlier is not automatically a bad value.**

For example, a genuine millionaire's salary is not an error just because it is unusually high.

Always understand the business/domain context first.

---

# 13. IQR Method

IQR stands for:

> **Interquartile Range**

It is commonly used to detect potential outliers.

### Formula

```text id="a8ph9c"
IQR = Q3 - Q1
```

Where:

```text id="g8f8kv"
Q1 = 25th percentile
Q3 = 75th percentile
```

Lower boundary:

```text id="mx1q0k"
Q1 - 1.5 × IQR
```

Upper boundary:

```text id="2f6k3x"
Q3 + 1.5 × IQR
```

Values outside these boundaries are commonly flagged as potential outliers.

---

# 14. IQR Example

Suppose:

```text id="g0q0sn"
Q1 = 20
Q3 = 40
```

Then:

```text id="7qv4vr"
IQR = 40 - 20
    = 20
```

Lower boundary:

```text id="3x0y2u"
20 - (1.5 × 20)
= -10
```

Upper boundary:

```text id="y1xjhy"
40 + (1.5 × 20)
= 70
```

Therefore values:

```text id="e9uwj6"
< -10
or
> 70
```

are flagged as potential outliers.

---

# 15. Find Outliers Using IQR

```python id="6z9r3k"
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["Salary"] < lower) |
    (df["Salary"] > upper)
]

print(outliers)
```

---

# 16. Remove IQR Outliers

```python id="0b3guk"
df = df[
    (df["Salary"] >= lower) &
    (df["Salary"] <= upper)
]
```

### But be careful!

Don't blindly remove every IQR outlier.

First ask:

> Is it a data-entry error or a genuine observation?

---

# 17. Z-Score

Z-score tells us how many standard deviations a value is away from the mean.

### Formula

```text id="8nq2vr"
Z = (X - Mean) / Standard Deviation
```

Example:

```text id="j4g2a9"
Mean = 50
Standard Deviation = 10
Value = 80
```

Then:

```text id="s5h7xk"
Z = (80 - 50) / 10
Z = 3
```

So the value is **3 standard deviations above the mean**.

---

# 18. Detect Outliers Using Z-Score

A common rule is:

```text id="v0k4pu"
Z < -3
or
Z > +3
```

may be treated as a potential outlier.

But the appropriate threshold depends on the application and assumptions.

Python:

```python id="9i7vkj"
from scipy.stats import zscore

z_scores = zscore(df["Salary"])

outliers = df[
    abs(z_scores) > 3
]

print(outliers)
```

---

# 19. IQR vs Z-Score

| IQR                       | Z-Score                                            |
| ------------------------- | -------------------------------------------------- |
| Based on quartiles        | Based on mean and standard deviation               |
| More robust to outliers   | More sensitive to outliers                         |
| Doesn't require normality | Often most interpretable under roughly normal data |
| Good for skewed data      | Common for approximately normal distributions      |

### Easy Trick

```text id="0yqv1a"
IQR
→ Quartiles

Z-Score
→ Mean + Standard Deviation
```

---

# 20. Imbalanced Data

## What is Imbalanced Data?

Imbalanced data occurs when one class has **many more observations than another class**.

Example:

```text id="7m1nwy"
Customer Churn

Not Churn → 9500
Churn     → 500
```

Total:

```text id="x6e3d4"
10000 customers
```

Distribution:

```text id="nyf3y9"
Not Churn → 95%
Churn     → 5%
```

This is an imbalanced dataset.

---

# 21. Why is Imbalanced Data a Problem?

Suppose a model predicts:

```text id="h5x2js"
Every customer → Not Churn
```

Accuracy:

```text id="kq7r5d"
9500 / 10000
= 95%
```

It looks like a very good model.

But the model completely fails to identify churn customers.

Therefore:

> **Accuracy alone can be misleading for imbalanced classification problems.**

We should also consider:

* Precision
* Recall
* F1-score
* Confusion Matrix
* PR-AUC / ROC-AUC, depending on the problem

---

# 22. How to Check Class Distribution?

```python id="r4x9df"
df["Churn"].value_counts()
```

Percentage:

```python id="b6p3qv"
df["Churn"].value_counts(normalize=True) * 100
```

Example:

```text
Not Churn    95%
Churn         5%
```

---

# 23. What is SMOTE?

SMOTE stands for:

> **Synthetic Minority Over-sampling Technique**

SMOTE is used to help address class imbalance by generating **synthetic minority-class samples**.

Instead of simply duplicating existing minority examples, SMOTE creates new synthetic points based on nearby minority samples.

---

# 24. Simple SMOTE Example

Suppose:

```text id="b0rj6n"
Class 0 → 900 samples
Class 1 → 100 samples
```

SMOTE can generate synthetic Class 1 samples.

After resampling, for example:

```text id="kq8c0e"
Class 0 → 900
Class 1 → 900
```

The exact target ratio is configurable.

---

# 25. Install imbalanced-learn

```bash id="5p5c98"
pip install imbalanced-learn
```

---

# 26. Apply SMOTE

```python id="x4k2ts"
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)

X_resampled, y_resampled = smote.fit_resample(
    X_train,
    y_train
)
```

Check distribution:

```python id="m2kr1b"
print(y_train.value_counts())

print(y_resampled.value_counts())
```

---

# 27. Very Important: SMOTE Only on Training Data

❌ Don't do this:

```python id="4s8w3z"
X_resampled, y_resampled = smote.fit_resample(
    X,
    y
)

X_train, X_test, y_train, y_test = train_test_split(
    X_resampled,
    y_resampled
)
```

This can cause **data leakage** because information from the full dataset can influence the test set.

### Correct approach

```text id="b5x6dj"
Original Data
     ↓
Train / Test Split
     ↓
Training Data
     ↓
SMOTE
     ↓
Train Model
     ↓
Original Test Data
     ↓
Evaluation
```

The test set should remain untouched.

---

# 28. SMOTE with Pipeline

For a robust workflow, use `imblearn.pipeline.Pipeline`.

```python id="q6a4w8"
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("smote", SMOTE(random_state=42)),
    ("model", LogisticRegression())
])
```

Train:

```python id="q8s2e1"
pipeline.fit(X_train, y_train)
```

Predict:

```python id="0j8f8m"
y_pred = pipeline.predict(X_test)
```

This is especially useful with cross-validation because SMOTE is applied separately inside each training fold rather than to validation/test data.

---

# 29. Complete Preprocessing Workflow

A typical workflow looks like:

```text id="g9s2w0"
Raw Dataset
     ↓
Check Data Types
     ↓
Missing Values
     ↓
Duplicates
     ↓
Outliers
     ↓
Categorical Encoding
     ↓
Feature Scaling
     ↓
Train/Test Split
     ↓
Handle Class Imbalance
     ↓
Train Model
     ↓
Evaluate
```

For SMOTE specifically:

```text id="x5g8p1"
Raw Data
    ↓
Clean Data
    ↓
Train/Test Split
    ↓
Training Data ──→ SMOTE
    ↓
Train Model
    ↓
Original Test Data
    ↓
Evaluation
```

---

# 30. Complete Example

Suppose we have a **Customer Churn Prediction** dataset.

Columns:

```text id="h7m1o2"
Age
MonthlyCharges
Tenure
Contract
Churn
```

### Step 1 — Check missing values

```python id="q4m1gz"
print(df.isnull().sum())
```

### Step 2 — Remove duplicates

```python id="1q7k7n"
df = df.drop_duplicates()
```

### Step 3 — Separate features and target

```python id="w5b7d1"
X = df.drop("Churn", axis=1)

y = df["Churn"]
```

### Step 4 — Split data

```python id="x2s5v9"
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

`stratify=y` helps preserve the class distribution between train and test sets.

### Step 5 — Apply SMOTE to training data

```python id="m4f0as"
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)

X_train_resampled, y_train_resampled = (
    smote.fit_resample(X_train, y_train)
)
```

### Step 6 — Train model

```python id="n3t2vj"
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(
    X_train_resampled,
    y_train_resampled
)
```

### Step 7 — Predict on original test data

```python id="1n4d6c"
y_pred = model.predict(X_test)
```

### Step 8 — Evaluate

```python id="0u7d1s"
from sklearn.metrics import (
    classification_report,
    confusion_matrix
)

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))
```

---

# 31. Important Difference: Outlier vs Imbalanced Data

These two concepts are different.

### Outlier

An unusual **data point**.

Example:

```text id="y7b0q6"
Salary:

30000
35000
40000
45000
5000000 ← Outlier
```

### Imbalanced Data

Unequal **class distribution**.

Example:

```text id="0gj4dn"
Class 0 → 9500
Class 1 → 500
```

### Easy Trick

```text id="1m8v4y"
Outlier
→ Unusual value

Imbalance
→ Unequal classes
```

---

# 32. Quick Revision

| Topic           | Simple Meaning                            |
| --------------- | ----------------------------------------- |
| Missing Value   | Data is unavailable                       |
| Duplicate       | Repeated record                           |
| Outlier         | Unusually different observation           |
| IQR             | Quartile-based outlier method             |
| Z-Score         | Distance from mean in standard deviations |
| Imbalanced Data | Unequal class distribution                |
| SMOTE           | Generates synthetic minority samples      |

---

# 🎯 Interview Questions

## Q1. What is data preprocessing?

> Data preprocessing is the process of cleaning and transforming raw data into a suitable format for machine learning.

---

## Q2. How do you handle missing values?

> Depending on the situation, I can remove rows or columns, or impute values using mean, median, mode, or a model-based method.

---

## Q3. When would you use median instead of mean?

> Median is often preferred when numerical data is skewed or contains outliers because it is less affected by extreme values.

---

## Q4. What are duplicates?

> Duplicates are repeated records in a dataset. They can be detected using `duplicated()` and removed using `drop_duplicates()` when they are not legitimate observations.

---

## Q5. What is an outlier?

> An outlier is an observation that is unusually far from the rest of the data.

---

## Q6. What is IQR?

> IQR is the Interquartile Range, calculated as Q3 minus Q1. It is commonly used to identify potential outliers.

```text id="v9y3e7"
IQR = Q3 - Q1
```

---

## Q7. What is Z-score?

> Z-score measures how many standard deviations an observation is away from the mean.

```text id="1c5y9k"
Z = (X - Mean) / Standard Deviation
```

---

## Q8. IQR vs Z-score?

> IQR is based on quartiles and is more robust to extreme values. Z-score is based on the mean and standard deviation and is often used when the distribution is approximately normal.

---

## Q9. What is imbalanced data?

> Imbalanced data occurs when one class has significantly more observations than another class.

---

## Q10. Why can accuracy be misleading for imbalanced data?

> Because a model can achieve high accuracy by mostly predicting the majority class while performing poorly on the minority class.

---

## Q11. What is SMOTE?

> SMOTE stands for Synthetic Minority Over-sampling Technique. It creates synthetic minority-class samples to help address class imbalance.

---

## Q12. Should we apply SMOTE before or after train-test split?

> After the train-test split, and only on the training data. The test set should remain untouched.

---

## Q13. Why should SMOTE not be applied to the test set?

> Applying SMOTE to the test set changes its natural distribution and can cause data leakage, resulting in an unrealistic evaluation.

---

## Q14. What is data leakage?

> Data leakage happens when information that should not be available during training influences the model's learning process.

Example:

```text id="a5b4u9"
❌ SMOTE on full dataset
❌ Fit scaler on full dataset before split
❌ Use test information during training
```

Correct:

```text id="4u3r8v"
Split
 ↓
Fit preprocessing on training data
 ↓
Train
 ↓
Transform test data
 ↓
Evaluate
```

---

# ⭐ Most Important Interview Answer

If the interviewer asks:

### "How do you preprocess a real-world dataset?"

You can answer:

> "First, I understand the dataset and check data types, missing values, duplicates, and invalid values. I handle missing values using an appropriate imputation strategy, remove only genuine duplicate records, and investigate outliers using methods such as IQR or Z-score. For classification problems, I check the class distribution and, if the data is significantly imbalanced, I may use techniques such as class weights or SMOTE. I perform preprocessing only using the training data to avoid data leakage, and I use pipelines where appropriate."

---

# 🚀 Final Cheat Sheet

```text id="1v0w4g"
DATA PREPROCESSING
│
├── Missing Values
│   ├── Remove
│   ├── Mean
│   ├── Median
│   └── Mode
│
├── Duplicates
│   ├── Check
│   └── Remove if appropriate
│
├── Outliers
│   ├── IQR
│   └── Z-Score
│
├── Imbalanced Data
│   ├── Check class distribution
│   ├── Class weights
│   └── SMOTE
│
└── Avoid Data Leakage
    └── Fit preprocessing on training data only
```

## ⭐ Remember

> **Clean the data → Split the data → Preprocess using training data → Handle imbalance on training data → Train → Evaluate on untouched test data.**
