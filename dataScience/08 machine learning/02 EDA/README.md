# Machine Learning

## 1. Data Visualization

* Matplotlib
* Seaborn
* Plotly
* Line Chart
* Bar Chart
* Histogram
* Box Plot
* Scatter Plot
* Heatmap
* Pair Plot
* Pie Chart
* Distribution Plot
* Correlation Visualization

## 2. Exploratory Data Analysis (EDA)

* Understand Dataset
* Dataset Shape 
* Data Types
* Missing Values
* Duplicate Values
* Statistical Summary
* Unique Values
* Outlier Detection
* Univariate Analysis
* Bivariate Analysis
* Multivariate Analysis
* Correlation Analysis
* Distribution Analysis
* Target Variable Analysis
* Data Visualization
* Finding Data Patterns
* Finding Data Quality Issues

## 3. Feature Engineering

* Feature Creation
* Feature Selection
* Feature Transformation
* Feature Scaling
* Normalization
* Standardization
* Encoding Categorical Variables

  * Label Encoding
  * One-Hot Encoding
  * Ordinal Encoding
* Handling Missing Values
* Handling Outliers
* Binning / Discretization
* Log Transformation
* Polynomial Features
* Date/Time Feature Extraction
* Text Feature Extraction
* Interaction Features
* Removing Irrelevant Features
* Dimensionality Reduction
  * PCA
* Preventing Data Leakage


# Machine Learning Preprocessing & Pipeline Architecture

This repository contains a comprehensive, production-grade guide to data preprocessing, feature engineering, and leak-proof pipeline design using **scikit-learn**. It serves as an architectural blueprint for converting raw datasets into clean, robust features for predictive modeling.

---

## 📌 ML Workflow Pipeline

```text
                     RAW DATA
                        │
                 Data Cleaning
                        │
              Feature Extraction
                        │
               Feature Selection
                        │
                Train/Test Split
                        │
           ┌────────────┴────────────┐
           ▼                         ▼
     Numerical                  Categorical
           │                         │
       Imputation                Imputation
           │                         │
        Scaling                   Encoding
           └────────────┬────────────┘
                        ▼
                ColumnTransformer
                        │
                     Pipeline
                        │
                      Model
                        │
                   Evaluation
```

---

## 1. Categorical Encoding

Machine Learning models cannot process raw text directly. Categorical text data must be transformed into a numerical format.

### OneHotEncoder
Creates a binary column for each unique category in a feature.

*   **Example:**
    ```text
    Raw Feature: [Product]
    - Shoe
    - Bag
    - T-Shirt
    ```
*   **Transformation:**
    ```text
    Product_Bag  Product_Shoe  Product_T-Shirt
         0            1               0
         1            0               0
         0            0               1
    ```

### Production Implementation
```python
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])
```

---

## 2. Feature Scaling

Numerical features often span wildly different mathematical ranges. Scaling prevents features with larger magnitudes from dominating the learning process.

### Feature Scaler Comparison

| Scaler | Formula / Core Logic | Best Used For | Vulnerability |
| :--- | :--- | :--- | :--- |
| **StandardScaler** | `z = (x - mean) / std` | Linear Models, SVMs, KNN, Neural Networks | Sensitive to extreme outliers. |
| **MinMaxScaler** | `z = (x - min) / (max - min)` | Algorithms needing bounded ranges (0 to 1) | Heavily distorted by outliers. |
| **RobustScaler** | `z = (x - median) / IQR` | Datasets with high outlier variance | Not ideal if data is perfectly normal. |

> 💡 **Rule of Thumb:** **Tree-based models** (e.g., Random Forest, XGBoost) do not require feature scaling because they split data using thresholds rather than distance or magnitude.

### Production Implementation
```python
from sklearn.preprocessing import StandardScaler

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
```

---

## 3. Feature Engineering

Optimising your feature space is critical for reducing model noise, reducing training time, and preventing overfitting.

### Feature Extraction
Deriving clean, actionable features from raw, unstructured fields (like Timestamps).
*   **Example:** Converting `Invoice Date (2026-08-13)` into distinct numerical fields:
    ```python
    df["Year"] = df["Invoice Date"].dt.year        # 2026
    df["Month"] = df["Invoice Date"].dt.month      # 8
    df["DayOfWeek"] = df["Invoice Date"].dt.dayofweek  # 3
    ```

### Feature Selection
Removing redundant, uninformative, or identifier-only columns that add noise to the model.
*   **Example:** Dropping internal database keys like `Retailer ID` or `UUID` before training:
    ```python
    df = df.drop(columns=["Retailer ID"])
    ```

---

## 4. Preventing Data Leakage

**Data Leakage** occurs when information from the holdout test set accidentally leaks into the training process, causing overly optimistic validation metrics but poor real-world performance.

### ❌ The Incorrect Way (Causes Leakage)
Fitting a transformer on the entire dataset calculates global metrics (like global mean or max value), meaning your training set learns properties of your test set.
```python
# BAD: Test data properties leak into the scaler calculations
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X) 
```

### ✅ The Correct Way (Leak-Proof)
Always split your data **before** applying any transformations. Fit parameters *only* on the training set.
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit metrics calculated ONLY from X_train
scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

## 5. End-to-End Unified Pipeline

Using `ColumnTransformer` combined with a scikit-learn `Pipeline` automatically enforces clean data separation, prevents leakage, and provides a single deployment asset.

```python
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor

# Define feature boundaries
numeric_features = ["Price per Unit", "Units Sold", "Year", "Month", "DayOfWeek"]
categorical_features = ["Retailer", "Region", "State", "City", "Product"]

# Combine processing steps
preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])

# Create full deployment pipeline
final_model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=200, random_state=42))
])

# Fit safely without risk of data leakage
final_model.fit(X_train, y_train)

# Predict seamlessly on raw inference data
predictions = final_model.predict(X_test)
```
