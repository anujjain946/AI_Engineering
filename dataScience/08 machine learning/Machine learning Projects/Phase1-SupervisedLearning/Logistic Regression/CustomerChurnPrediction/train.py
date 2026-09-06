from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib
from config import  MODEL_PATH
from preprocess import loadDataset



# Split data
X_train, X_test, y_train, y_test = loadDataset()

# 1. Define the steps in your pipeline (List of tuples: ('name', transformer/estimator))
pipeline = Pipeline([
    ('scaler', StandardScaler()),        # Step 1: Scale the features
    ('classifier', LogisticRegression(random_state=42, class_weight='balanced')) # Step 2: Train the model
])


# 2. Fit the entire pipeline on your training data
pipeline.fit(X_train, y_train)


# Save model
joblib.dump(pipeline, MODEL_PATH)

print("Model Saved Successfully")