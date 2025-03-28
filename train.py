import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
import os

# Choisir le type d'images (color, grayscale, segmented)
dataset_type = "color"

# Définition des chemins
train_dir = f"../dataset/{dataset_type}/train"
test_dir = f"../dataset/{dataset_type}/test"

# Prétraitement des images
img_size = (224, 224)
batch_size = 32

train_datagen = ImageDataGenerator(
    rescale=1./255, rotation_range=20, width_shift_range=0.2, height_shift_range=0.2,
    horizontal_flip=True, validation_split=0.2
)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir, target_size=img_size, batch_size=batch_size,
    class_mode="categorical", subset="training"
)

val_generator = train_datagen.flow_from_directory(
    train_dir, target_size=img_size, batch_size=batch_size,
    class_mode="categorical", subset="validation"
)

# Chargement de MobileNetV2
base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights="imagenet")
base_model.trainable = False

# Ajout de la couche de classification
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation="relu")(x)
x = Dropout(0.3)(x)
output_layer = Dense(len(train_generator.class_indices), activation="softmax")(x)  # Correction ici !

# Définition du modèle
model = Model(inputs=base_model.input, outputs=output_layer)


# Compilation et entraînement
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
              loss="categorical_crossentropy",
              metrics=["accuracy"])

model.fit(train_generator, validation_data=val_generator, epochs=10, batch_size=batch_size)

# Sauvegarde du modèle
model.save(f"../models/mobilenetv2_{dataset_type}.h5")
print(f"Modèle sauvegardé sous models/mobilenetv2_{dataset_type}.h5")
