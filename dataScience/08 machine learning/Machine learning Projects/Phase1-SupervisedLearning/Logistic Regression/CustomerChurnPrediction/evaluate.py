import joblib
import pandas as pd
import numpy as np

# Changed to classification metrics
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from preprocess import loadDataset
from config import MODEL_PATH

def evaluate_model():
    # 1. Load data splits (Assumes stratify=y was handled inside loadDataset)
    X_train, X_test, y_train, y_test = loadDataset()

    # 2. Load the trained Logistic Regression Pipeline/Model
    model = joblib.load(MODEL_PATH)

    # 3. Generate Predictions on test data
    y_pred = model.predict(X_test)

    # 4. Compute Classification Metrics
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)

    # 5. Print Results
    print("=" * 50)
    print("       LOGISTIC REGRESSION MODEL")
    print("             EVALUATION")
    print("=" * 50)
    
    print(f"Overall Accuracy: {accuracy:.4f}\n")
    
    print("Classification Report:")
    print(report)
    
    print("Confusion Matrix:")
    print(matrix)
    print("=" * 50)

if __name__ == "__main__":
    evaluate_model()
