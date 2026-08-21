from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
import joblib
from config import  MODEL_PATH
from preprocess import loadDataset
from sklearn.linear_model import LinearRegression


# Airline	Date_of_Journey	Source	Destination	Route	Dep_Time	Arrival_Time	Duration	Total_Stops	Additional_Info
# Split data
X_train, X_test, y_train, y_test = loadDataset()




# Categorical Pipeline
categorical_features = [
        "Airline",
        "Source",
        "Destination",
        "Route",
        "Dep_Time",
        "Arrival_Time",
        "Duration",
        "Total_Stops",
        "Additional_Info"
]


categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("cat", categorical_pipeline, categorical_features)
])


# model = Pipeline([
#     ("preprocessor", preprocessor),
#     ("regressor", RandomForestRegressor(
#         n_estimators=200,
#         random_state=42,
#         n_jobs=-1
#     ))
# ])



model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])



# X_train = pipeline.fit_transform(X_train)
# X_test = pipeline.transform(X_test)

# Train model
model.fit(X_train, y_train)

# Save model
joblib.dump(model, MODEL_PATH)

print("Model Saved Successfully")