# Comprehensive Machine Learning Pipeline (Classification)

This repository contains a complete, production-ready **End-to-End Machine Learning Pipeline** for tabular classification tasks. The workflow spans from initial raw data loading to final model deployment using standard data science and machine learning libraries (`pandas`, `scikit-learn`, `seaborn`, `joblib`).

---

## 🚀 Pipeline Flow Overview

---

## 🛠️ Step-by-Step Implementation Guide

### Step 1: Dataset Load
Read your data into a DataFrame. This acts as the entry point for your data workflow.
* **Code Example:**
  ```python
  import pandas as pd

  df = pd.read_csv("your_dataset.csv")
  print("Dataset loaded successfully!")
  ```

### Step 2: Data Understanding
Inspect the dimensions, data types, and structural properties of your dataset.
* **Code Example:**
  ```python
  print(df.shape)  # Dimensions
  print(df.info())  # Data types & non-null counts
  print(df.describe(include="all"))  # Statistical overview
  ```

### Step 3: EDA (Exploratory Data Analysis)
Visualize feature distributions, relationships, and the balance of your target class.
* **Code Example:**
  ```python
  import matplotlib.pyplot as plt
  import seaborn as sns

  # Target class distribution
  sns.countplot(x="target", data=df)
  plt.show()

  # Correlation Matrix Heatmap
  sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
  plt.show()
  ```

### Step 4: Missing Values Handling
Identify missing values and apply strategy-based imputation rules.
* **Code Example:**
  ```python
  print(df.isnull().sum())  # Check missing numbers

  # Imputation strategy
  for col in df.columns:
      if df[col].isnull().any():
          if df[col].dtype == "object":
              df[col].fillna(df[col].mode()[0], inplace=True)  # Categorical
          else:
              df[col].fillna(df[col].median(), inplace=True)  # Numerical
  ```

### Step 5: Duplicate Check
Scan your rows to identify and drop identical copies of entries.
* **Code Example:**
  ```python
  print(f"Duplicate rows found: {df.duplicated().sum()}")
  df.drop_duplicates(inplace=True)
  df.reset_index(drop=True, inplace=True)
  ```

### Step 6: Categorical Encoding
Convert non-numeric text classes into numerical matrices using encoding mechanisms.
* **Code Example:**
  ```python
  # One-Hot Encoding for nominal features
  df = pd.get_dummies(df, drop_first=True)
  ```

### Step 7: Feature Selection
Separate features (\(X\)) from the target column (\(y\)) and filter out non-essential predictive items.
* **Code Example:**
  ```python
  X = df.drop(columns=["target"])
  y = df["target"]
  ```

### Step 8: Train / Test Split
Partition datasets safely to avoid data leakage while evaluating final metrics.
* **Code Example:**
  ```python
  from sklearn.model_selection import train_test_split

  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=42, stratify=y
  )
  ```

### Step 9: Feature Scaling
Normalize numerical columns to a unified, relative range scale.
* **Code Example:**
  ```python
  from sklearn.preprocessing import StandardScaler

  scaler = StandardScaler()
  X_train_scaled = scaler.fit_transform(X_train)
  X_test_scaled = scaler.transform(X_test)
  ```

### Step 10: Logistic Regression
Train a foundational parametric linear benchmark classifier.
* **Code Example:**
  ```python
  from sklearn.linear_model import LogisticRegression

  lr_model = LogisticRegression(max_iter=1000)
  lr_model.fit(X_train_scaled, y_train)
  ```

### Step 11: Decision Tree
Train an easily interpretable, non-linear tree rule partition engine.
* **Code Example:**
  ```python
  from sklearn.tree import DecisionTreeClassifier

  dt_model = DecisionTreeClassifier(random_state=42)
  dt_model.fit(X_train_scaled, y_train)
  ```

### Step 12: Random Forest
Train an ensemble system built on robust bootstrapped decision structures.
* **Code Example:**
  ```python
  from sklearn.ensemble import RandomForestClassifier

  rf_model = RandomForestClassifier(random_state=42)
  rf_model.fit(X_train_scaled, y_train)
  ```

### Step 13: Model Comparison
Evaluate overall training and generalization performance metrics across your trained baselines.
* **Code Example:**
  ```python
  models = {"Logistic Regression": lr_model, "Decision Tree": dt_model, "Random Forest": rf_model}

  for name, model in models.items():
      print(f"{name} Test Accuracy: {model.score(X_test_scaled, y_test):.4f}")
  ```

### Step 14: Confusion Matrix
Generate error matrix grids tracking true vs predicted categorical patterns.
* **Code Example:**
  ```python
  from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

  y_pred = rf_model.predict(X_test_scaled)
  cm = confusion_matrix(y_test, y_pred)
  ConfusionMatrixDisplay(cm).plot()
  plt.show()
  ```

### Step 15: Precision / Recall / F1 / ROC-AUC
Generate granular structural classification performance diagnostic sheets.
* **Code Example:**
  ```python
  from sklearn.metrics import classification_report, roc_auc_score

  print(classification_report(y_test, y_pred))

  y_probs = rf_model.predict_proba(X_test_scaled)[:, 1]
  print(f"ROC-AUC Score: {roc_auc_score(y_test, y_probs):.4f}")
  ```

### Step 16: Hyperparameter Tuning
Optimize model architecture layouts using automated broad cross-validated search spaces.
* **Code Example:**
  ```python
  from sklearn.model_selection import GridSearchCV

  param_grid = {"n_estimators":, "max_depth": [None, 10, 20]}

  grid_search = GridSearchCV(
      RandomForestClassifier(random_state=42), param_grid, cv=5, scoring="f1"
  )
  grid_search.fit(X_train_scaled, y_train)
  best_model = grid_search.best_estimator_
  ```

### Step 17: Save Model Using Joblib
Export your optimized pipeline artifacts to binary files for production deployment.
* **Code Example:**
  ```python
  import joblib

  # Save artifact models
  joblib.dump(best_model, "best_random_forest_model.pkl")
  joblib.dump(scaler, "feature_scaler.pkl")
  print("Models saved successfully!")
  ```

### Step 18: Prediction Function / API
Deploy an asset interface block to transform raw dictionary queries into live prediction inference scores.
* **Code Example:**
  ```python
  import numpy as np
  import joblib


  def predict_pipeline(raw_input_data):
      """Loads production weights to score a single raw input dictionary sample."""
      model = joblib.load("best_random_forest_model.pkl")
      scaler = joblib.load("feature_scaler.pkl")

      # Convert sample input to array shape
      input_array = np.array(list(raw_input_data.values())).reshape(1, -1)
      scaled_input = scaler.transform(input_array)

      prediction = model.predict(scaled_input)
      probability = model.predict_proba(scaled_input)[0][1]

      return {"class_prediction": int(prediction[0]), "probability_score": float(probability)}
  ```