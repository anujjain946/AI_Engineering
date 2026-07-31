import tensorflow as tf

def create_model():

    model = tf.keras.Sequential([

        tf.keras.layers.Dense(
            32,
            input_shape=(3,)
        ),

        tf.keras.layers.Dense(
            16,
            activation="relu"
        ),
        tf.keras.layers.Dropout(0.2), 

         tf.keras.layers.Dense(
            8,
            activation="relu"
        ),
        tf.keras.layers.Dropout(0.2), 

        tf.keras.layers.Dense(
            1,
            activation="sigmoid"
        )

    ])

    model.compile(

        optimizer="adam",

        loss="binary_crossentropy",

        metrics=["accuracy"]

    )

    

    return model