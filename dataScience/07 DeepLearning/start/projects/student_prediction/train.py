from preprocess import load_data

from model import create_model

from config import *

X_train, X_test, y_train, y_test = load_data()

model = create_model()

history = model.fit(

    X_train,

    y_train,

    validation_data=(X_test,y_test),

    epochs=EPOCHS,

    batch_size=BATCH_SIZE

)

model.save(MODEL_PATH)

print("Model Saved Successfully")