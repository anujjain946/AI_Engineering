import joblib
import pandas as pd

from config import MODEL_PATH


# Load trained pipeline
model = joblib.load(MODEL_PATH)


def predictStudenPerformence(
    ExtracurricularActivities,  
    HoursStudied,
    PreviousScores,
    SleepHours,
    SampleQuestionPapersPracticed
):

    data = pd.DataFrame({
        "Extracurricular Activities": [ExtracurricularActivities],
        "Hours Studied": [HoursStudied],
        "Previous Scores": [PreviousScores],
        "Sleep Hours": [SleepHours],
        "Sample Question Papers Practiced": [SampleQuestionPapersPracticed],
    })


    prediction = model.predict(data)

    return float(prediction[0])


# Test prediction
predict_studen_performence = predictStudenPerformence('yes',7,85,8,6)

print(f"Predicted Performence: {predict_studen_performence:.2f}")