import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        self.model = load_model("artifacts/training/model.h5")

        self.class_labels = {0: "Normal", 1: "Tumor"}

    def predict(self):
        # load image
        test_image = load_img(self.filename, target_size=(224, 224))
        test_image = img_to_array(test_image)

        # convert to batch format
        test_image = np.expand_dims(test_image, axis=0)

        # ✅ FIX: correct preprocessing for VGG16
        test_image = preprocess_input(test_image)

        # prediction
        predictions = self.model.predict(test_image)

        # softmax output → argmax works correctly
        result = np.argmax(predictions, axis=1)[0]

        prediction = self.class_labels[result]

        return [{"image": prediction}]