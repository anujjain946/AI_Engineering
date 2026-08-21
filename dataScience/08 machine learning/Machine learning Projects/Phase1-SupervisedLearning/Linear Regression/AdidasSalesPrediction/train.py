from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
import joblib
from config import  MODEL_PATH
from preprocess import loadDataset



# Split data
X_train, X_test, y_train, y_test = loadDataset()

# Numerical Pipeline
numeric_features = [
    "Price per Unit",
    "Units Sold",
    "Year",
    "Month",
    "Day",
    "DayOfWeek"
]


# Categorical Pipeline
categorical_features = [
    "Retailer",
    "Region",
    "State",
    "City",
    "Product",
    "Sales Method"
]

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
    ("regressor", RandomForestRegressor(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    ))
])



# X_train = pipeline.fit_transform(X_train)
# X_test = pipeline.transform(X_test)

# Train model
model.fit(X_train, y_train)

# Save model
joblib.dump(model, MODEL_PATH)

print("Model Saved Successfully")