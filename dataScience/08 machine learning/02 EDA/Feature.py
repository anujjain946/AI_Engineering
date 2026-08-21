'''

Feature Engineering — Complete Roadmap

**Feature Engineering** means converting raw data into useful features that help a Machine Learning model learn better.

A good sequence is:

```text
Raw Dataset
     ↓
Understand Features
     ↓
Feature Creation
     ↓
Feature Selection
     ↓
Handle Missing Values
     ↓
Handle Outliers
     ↓
Encoding
     ↓
Transformation
     ↓
Scaling
     ↓
Feature Interaction
     ↓
Dimensionality Reduction
     ↓
Final ML Dataset
```

## 1. Feature Creation

Create new features from existing columns.

Example:

```python
df["TotalAmount"] = df["Quantity"] * df["Price"]
```

Another example:

```python
df["AgeGroup"] = df["Age"].apply(
    lambda x: "Young" if x < 30 else "Adult"
)
```

**Goal:** extract more useful information from existing data.

---

## 2. Feature Selection

Select only the features that are useful for the model.

```python
features = [
    "Age",
    "Income",
    "Experience"
]

X = df[features]
```

Common techniques:

* Correlation
* Mutual Information
* Chi-Square
* ANOVA
* Recursive Feature Elimination
* L1 Regularization
* Feature Importance

Why?

```text
Too many features
       ↓
More complexity
       ↓
Higher chance of overfitting
       ↓
Slower training
```

---

## 3. Feature Transformation

Transform features into a more useful representation.

Examples:

```text
Log Transformation
Square Root
Polynomial Transformation
Power Transformation
```

Example:

```python
import numpy as np

df["LogIncome"] = np.log1p(df["Income"])
```

Useful when data is highly skewed.

---

## 4. Feature Scaling

Features can have very different ranges.

Example:

```text
Age       → 18–80
Salary    → 20,000–2,000,000
```

Salary can dominate distance/gradient-based algorithms.

Common scaling methods:

```text
Normalization
Standardization
Robust Scaling
Min-Max Scaling
```

---

# 5. Normalization

Usually means scaling values to a fixed range, commonly **0 to 1**.

Formula:

```text
x' = (x - min) / (max - min)
```

Using Scikit-Learn:

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)
```

Example:

```text
10 → 0.0
20 → 0.5
30 → 1.0
```

Useful for algorithms such as:

* KNN
* Neural Networks
* Gradient-based models

---

# 6. Standardization

Standardization transforms data so that it generally has:

```text
Mean ≈ 0
Standard deviation ≈ 1
```

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

The transformation is based on the z-score:

genui{"descriptive_statistics_sampling":{"type_id":"STANDARD_SCORE_Z"}}

Commonly useful for:

* Logistic Regression
* Linear Regression
* SVM
* KNN
* PCA
* Neural Networks

---

# 7. Encoding Categorical Variables

ML models generally require numerical inputs, so categorical data must be encoded.

Example:

```text
Gender

Male
Female
Male
Female
```

---

### 7.1 Label Encoding

Converts categories into integer labels.

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

df["Gender"] = encoder.fit_transform(df["Gender"])
```

Example:

```text
Female → 0
Male   → 1
```

⚠️ Be careful using Label Encoding for **nominal categories** because numbers can incorrectly imply an order.

---

### 7.2 One-Hot Encoding

Creates separate binary columns.

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(
    handle_unknown="ignore"
)

X_encoded = encoder.fit_transform(
    df[["City"]]
)
```

Example:

```text
City

Delhi
Mumbai
Pune
```

becomes conceptually:

```text
City_Delhi  City_Mumbai  City_Pune
    1           0           0
    0           1           0
    0           0           1
```

Best for **nominal categories** without natural ordering.

---

### 7.3 Ordinal Encoding

Use when categories have a meaningful order.

Example:

```text
Education

School < Bachelor < Master < PhD
```

```python
from sklearn.preprocessing import OrdinalEncoder

encoder = OrdinalEncoder(
    categories=[
        ["School", "Bachelor", "Master", "PhD"]
    ]
)

df["Education"] = encoder.fit_transform(
    df[["Education"]]
)
```

Conceptually:

```text
School   → 0
Bachelor → 1
Master   → 2
PhD      → 3
```

---

# 8. Handling Missing Values

### Numerical

```python
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)
```

### Categorical

```python
df["City"] = df["City"].fillna(
    df["City"].mode()[0]
)
```

Better approach for ML pipelines:

```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")

X = imputer.fit_transform(X)
```

Common strategies:

```text
Mean
Median
Mode
Constant
KNN Imputation
Iterative Imputation
```

---

# 9. Handling Outliers

First identify them:

```python
import seaborn as sns

sns.boxplot(x=df["Salary"])
```

Then choose an appropriate strategy:

```text
Remove
Cap/Winsorize
Transform
Replace
Keep
```

**Don't automatically remove every outlier.**

An outlier could be a legitimate observation.

---

# 10. Binning / Discretization

Convert continuous values into groups.

Example:

```python
bins = [0, 18, 30, 50, 100]

labels = [
    "Child",
    "Young",
    "Adult",
    "Senior"
]

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)
```

Example:

```text
Age = 25
      ↓
Young
```

Useful when ranges/categories are more meaningful than exact values.

---

# 11. Log Transformation

Useful for **right-skewed data**.

```python
import numpy as np

df["LogSalary"] = np.log1p(
    df["Salary"]
)
```

Conceptually:

```text
Original:

1
10
100
1000
10000

        ↓ log transformation

0
2.4
4.6
6.9
9.2
```

It compresses very large values.

---

# 12. Polynomial Features

Create higher-order features.

Suppose:

```text
X
```

Polynomial transformation can create:

```text
X
X²
X³
```

Using Scikit-Learn:

```python
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(
    degree=2,
    include_bias=False
)

X_poly = poly.fit_transform(X)
```

For:

```text
X1, X2
```

you can get:

```text
X1
X2
X1²
X1 × X2
X2²
```

Useful when the relationship between features and target is **non-linear**.

---

# 13. Date/Time Feature Extraction

A date contains much more information than a single string.

```python
df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["DayOfWeek"] = df["Date"].dt.dayofweek
df["Quarter"] = df["Date"].dt.quarter
```

You can also create:

```text
Weekend
Month
Quarter
Hour
Minute
Day of year
Week of year
```

Example:

```python
df["IsWeekend"] = (
    df["DayOfWeek"] >= 5
).astype(int)
```

---

# 14. Text Feature Extraction

Convert text into numerical features.

Common approaches:

```text
Bag of Words
TF-IDF
N-grams
Word Embeddings
```

Example using TF-IDF:

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

X_text = vectorizer.fit_transform(
    df["Review"]
)
```

Example:

```text
"I love this product"
        ↓
TF-IDF
        ↓
[0.12, 0.00, 0.45, ...]
```

---

# 15. Interaction Features

Create features by combining existing features.

Example:

```python
df["IncomePerPerson"] = (
    df["Income"] / df["FamilySize"]
)
```

Or:

```python
df["Age_Income"] = (
    df["Age"] * df["Income"]
)
```

PolynomialFeatures can also automatically generate interaction terms.

---

# 16. Removing Irrelevant Features

Remove columns that don't provide useful predictive information.

Example:

```python
df = df.drop(
    columns=["CustomerID"]
)
```

Potentially irrelevant:

```text
Customer ID
Transaction ID
Random identifiers
Constant columns
Duplicate information
```

But be careful: an apparently useless column can sometimes contain useful information.

---

# 17. Dimensionality Reduction — PCA

**PCA (Principal Component Analysis)** reduces the number of features while trying to preserve as much variance/information as possible.

Example:

```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)
```

Original:

```text
Feature 1
Feature 2
Feature 3
Feature 4
Feature 5
Feature 6
Feature 7
Feature 8
```

After PCA:

```text
PC1
PC2
```

Useful for:

* High-dimensional datasets
* Visualization
* Reducing model complexity
* Removing correlated dimensions

⚠️ **Scale features before PCA** in most cases.

---

# 18. Preventing Data Leakage

This is one of the **most important Feature Engineering concepts**.

### Wrong ❌

```python
scaler.fit_transform(X)
```

before splitting the data.

Or:

```python
imputer.fit_transform(all_data)
```

before train/test split.

The transformation learns information from the test set.

### Correct ✅

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)
```

Remember:

```text
TRAIN DATA
    ↓
fit()
    ↓
Transformation rules
    ↓
TEST DATA
    ↓
transform()
```

**Never learn preprocessing parameters from the test set.**

---

# 🔥 Complete Feature Engineering Checklist

```text
FEATURE ENGINEERING
│
├── Feature Creation
│
├── Feature Selection
│
├── Feature Transformation
│
├── Feature Scaling
│   ├── Normalization
│   └── Standardization
│
├── Categorical Encoding
│   ├── Label Encoding
│   ├── One-Hot Encoding
│   └── Ordinal Encoding
│
├── Missing Value Handling
│
├── Outlier Handling
│
├── Binning / Discretization
│
├── Log Transformation
│
├── Polynomial Features
│
├── Date/Time Features
│
├── Text Features
│
├── Interaction Features
│
├── Remove Irrelevant Features
│
├── Dimensionality Reduction
│   └── PCA
│
└── Prevent Data Leakage
```

### ⭐ Most important for ML interviews

Focus especially on these differences:

```text
Normalization vs Standardization
Label vs One-Hot vs Ordinal Encoding
Feature Selection vs Feature Extraction
Handling Missing Values
Handling Outliers
Polynomial vs Interaction Features
PCA
Data Leakage
fit() vs transform() vs fit_transform()
```

And for real ML projects, learn to combine these using **`Pipeline` and `ColumnTransformer`**. This is the next major step after understanding individual Feature Engineering techniques.
'''