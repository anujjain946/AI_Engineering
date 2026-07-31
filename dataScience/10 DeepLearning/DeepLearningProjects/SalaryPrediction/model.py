import tensorflow as tf

def create_model():

    model = tf.keras.Sequential([

        # tf.keras.layers.Dense(64, activation="relu", input_shape=(5,)),
        # tf.keras.layers.Dense(32, activation="relu"),
        # tf.keras.layers.Dense(16, activation="relu"),
        # tf.keras.layers.Dense(1)
        tf.keras.layers.Dense(8, activation="relu", input_shape=(1,)),
        tf.keras.layers.Dense(4, activation="relu"),
        tf.keras.layers.Dense(1)

    ])

    model.compile(
        optimizer="adam",
        loss="mse",
        metrics=["mae"]
    )

    return model