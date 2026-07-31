from preprocess import load_data

from model import create_model

from config import *
import tensorflow as tf

X_train, X_test, y_train, y_test = load_data()

model = create_model()

early_stop = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        # monitor="val_accuracy",
        patience=4,
        restore_best_weights=True
),


history = model.fit(

    X_train,

    y_train,

    validation_data=(X_test,y_test),

    epochs=EPOCHS,

    batch_size=BATCH_SIZE,
    callbacks = [early_stop]

)

model.save(MODEL_PATH)

print("Model Saved Successfully")