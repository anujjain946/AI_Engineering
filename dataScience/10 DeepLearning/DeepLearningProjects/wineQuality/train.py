import tensorflow as tf
from preprocess import load_data

from model import create_model

from config import *

X_train, X_test, y_train, y_test = load_data()

model = create_model()

early_stop = tf.keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=7,
    restore_best_weights=True
)

checkpoint = tf.keras.callbacks.ModelCheckpoint(
    "models/best_wine_model.keras",
    monitor="val_loss",
    save_best_only=True,
    mode="min",
    verbose=1
)
history = model.fit(

    X_train,

    y_train,

    validation_data=(X_test,y_test),

    epochs=EPOCHS,

    batch_size=BATCH_SIZE,
    callbacks=[
        early_stop,
        checkpoint
    ]

)
model.save(MODEL_PATH)
print("Model Saved Successfully")