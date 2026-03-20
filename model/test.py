import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load model
model = load_model("fruit_model.h5")

# Class labels (VERY IMPORTANT)
classes = ['overripe', 'ripe', 'unripe']

# Load test image
img = cv2.imread("test.jpg")   # <-- put your image name here
img = cv2.resize(img, (128,128))
img = img / 255.0
img = np.reshape(img, (1,128,128,3))

# Predict
prediction = model.predict(img)
label = classes[np.argmax(prediction)]

print("Prediction:", label)