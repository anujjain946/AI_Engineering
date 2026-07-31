import tensorflow as tf

def create_model():

    model = tf.keras.Sequential([

        tf.keras.layers.Dense(
            128,
            input_shape=(11,)
        ),

        tf.keras.layers.Dense(
            64,
            activation="relu"
        ),
        tf.keras.layers.Dropout(0.3), 

        tf.keras.layers.Dense(
            16,
            activation="relu"
        ),
        tf.keras.layers.Dropout(0.2), 

        tf.keras.layers.Dense(
            16,
            activation="relu"
        ),

        tf.keras.layers.Dense(
            1,
            activation="sigmoid"
        )

    ])

    # model.compile(

    #     optimizer="adam",

    #     loss="binary_crossentropy",

    #     metrics=["accuracy"]

    # )


    model.compile(
    optimizer=tf.keras.optimizers.Adam(
        learning_rate=0.001
    ),

    loss="binary_crossentropy",

    metrics=[
        "accuracy",
        tf.keras.metrics.Precision(name="precision"),
        tf.keras.metrics.Recall(name="recall"),
        tf.keras.metrics.AUC(name="auc")
    ]
)

    

    return model