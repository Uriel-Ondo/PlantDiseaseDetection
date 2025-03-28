import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Choisir le dataset (color, grayscale, segmented)
dataset_type = "color"

# Chargement du modèle
model_path = f"../models/mobilenetv2_{dataset_type}.h5"
model = load_model(model_path)

# Chargement des données de test
test_dir = f"../dataset/{dataset_type}/test"
img_size = (224, 224)
batch_size = 32

test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
    test_dir, target_size=img_size, batch_size=batch_size, class_mode="categorical"
)

# Évaluation du modèle
test_loss, test_acc = model.evaluate(test_generator)
print(f"Test Accuracy: {test_acc*100:.2f}%")
