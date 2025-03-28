import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import sys

# Choisir le dataset (color, grayscale, segmented)
dataset_type = "color"

# Chargement du modèle
model_path = f"../models/mobilenetv2_{dataset_type}.h5"
model = load_model(model_path)

# Chargement des classes
class_names = ["Apple___Black_rot", "Apple___healthy", "Tomato___Leaf_Mold"]  # Modifier selon tes classes

# Charger une image en argument
if len(sys.argv) < 2:
    print("Usage: python predict.py <chemin_de_l_image>")
    sys.exit()

img_path = sys.argv[1]
img = cv2.imread(img_path)
img = cv2.resize(img, (224, 224))
img = img / 255.0  # Normalisation
img = np.expand_dims(img, axis=0)

# Prédiction
pred = model.predict(img)
predicted_class = class_names[np.argmax(pred)]

print(f"Classe prédite : {predicted_class}")
