import mlflow
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

## set Experiment
mlflow.set_experiment("Iris Classification Experiment")
print("⚠️: Experiment is all set")

#load the iris dataset
X, y = load_iris(return_X_y=True)

# split the data into train and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state = 42
)

# display the len of train and test set
print("⚠️ Training Samples: ", len(X_train))
print("⚠️ Testing Samples: ", len(X_test))


# mlflow workflow
params = {
    'solver': 'lbfgs',
    'max_iter': 100,
    'random_state': 42
}               

with mlflow.start_run(run_name="base_line"):

   # log parameters
    mlflow.log_params(params)

    # train model
    logistic_model = LogisticRegression(**params)
    logistic_model.fit(X_train, y_train)

    # prediction of the model
    y_pred = logistic_model.predict(X_test)

    # evalaution of the model
    accuracy = accuracy_score(y_test, y_pred)

    # log evaluation metric
    mlflow.log_metric("accuracy", accuracy)

     # save the model and register it
    mlflow.sklearn.log_model(logistic_model, artifact_path="logistic_model", registered_model_name="Iris_Classifier")

    print("Baseline Accuracy: ", accuracy)
    print("Run ID: ", mlflow.active_run().info.run_id)




    
    # #log confusion matrix
    # cm = confusion_matrix(y_test, cles)
    # plt.figure(figsize=(5,5))
    # plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    # plt.title('Confusion Matrix')
    # plt.colorbar()
    # tick_marks = np.arange(len(set(y)))
    # plt.xticks(tick_marks, set(y))
    # plt.yticks(tick_marks, set(y))
    # plt.ylabel('True label')
    # plt.xlabel('Predicted label')
    
    # #save the confusion matrix plot
    # cm_plot_path = "confusion_matrix.png"
    # plt.savefig(cm_plot_path)
    
    # #log the confusion matrix plot to mlflow
    # mlflow.log_artifact(cm_plot_path)
