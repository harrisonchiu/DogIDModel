import os
import sys
import random

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Check versions of libraries
print(f"Python: {sys.version}")
print(f"numpy: {np.__version__}")
print(f"tensorflow: {tf.__version__}")

print(tf.config.list_physical_devices("GPU"))



CURRENT_DIR = os.getcwd()
TRAINING_SET_DIR = os.path.join(CURRENT_DIR, "images", "training_set")
VALIDATION_SET_DIR = os.path.join(CURRENT_DIR, "images", "validation_set")
NUMBER_OF_TRAINING_IMAGES = 0
NUMBER_OF_VALIDATION_IMAGES = 0

# Must be the same input size as the base model
# Currently using: EfficientNetB5 - (456, 456)
IMAGE_WIDTH = 456
IMAGE_HEIGHT = 456

EPOCHS = 8
BATCH_SIZE = 24
LEARNING_RATE = 0.001



image_generator_train = keras.preprocessing.image.ImageDataGenerator(
    # rescale=1./255,
    brightness_range=[0.4, 1.4],
    channel_shift_range=30,
    rotation_range=30,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.2,
    zoom_range=0.1,
    horizontal_flip=True,
)

data_generator_train = image_generator_train.flow_from_directory(
    batch_size=BATCH_SIZE,
    directory=TRAINING_SET_DIR,
    shuffle=True,
    target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
    class_mode="categorical"
)

image_generator_validation = keras.preprocessing.image.ImageDataGenerator(
    # rescale=1./255
)

data_generator_validation = image_generator_validation.flow_from_directory(
    batch_size=BATCH_SIZE,
    directory=VALIDATION_SET_DIR,
    target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
    class_mode="categorical"
)

NUMBER_OF_TRAINING_IMAGES = data_generator_train.samples
NUMBER_OF_VALIDATION_IMAGES = data_generator_validation.samples


base_model = keras.applications.EfficientNetB5(
    weights="efficientnetb5_noisystudent_notop.h5", include_top=False, input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, 3)
)

inputs = keras.Input(shape=(IMAGE_WIDTH, IMAGE_HEIGHT, 3))
x = tf.cast(inputs, dtype=tf.uint8)
x = base_model(x, training=False)

x = keras.layers.GlobalAveragePooling2D()(x)
# x = keras.layers.Dropout(0.2)(x)

outputs = keras.layers.Dense(130, activation="softmax")(x)
model = keras.models.Model(inputs=inputs, outputs=outputs)

for layer in base_model.layers:
    layer.trainable = False

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()



history = model.fit(
    data_generator_train,
    epochs=EPOCHS,
    steps_per_epoch=NUMBER_OF_TRAINING_IMAGES // BATCH_SIZE,
    validation_data=data_generator_validation,
    validation_steps=NUMBER_OF_VALIDATION_IMAGES // BATCH_SIZE
)


model.save("efficientnetb5-noisystudent-8epochs")


accuracy = history.history["accuracy"]
validation_accuracy = history.history["val_accuracy"]

loss = history.history["loss"]
validation_loss = history.history["val_loss"]

"""Plot accuracy of model by epochs"""
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(range(EPOCHS), accuracy, label="Training Accuracy")
plt.plot(range(EPOCHS), validation_accuracy, label="Validation Accuracy")
plt.legend(loc="lower right")
plt.title("Training and Validation Accuracy")

"""Plot loss of model by epochs"""
plt.subplot(1, 2, 2)
plt.plot(range(EPOCHS), loss, label="Training Loss")
plt.plot(range(EPOCHS), validation_loss, label="Validation Loss")
plt.legend(loc="upper right")
plt.title("Training and Validation Loss")
plt.show()
