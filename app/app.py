import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load model
model = load_model("../model/fruit_model.h5")

# Classes
classes = ['overripe', 'ripe', 'unripe']

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Resize and preprocess
    img = cv2.resize(frame, (128,128))
    img = img / 255.0
    img = np.reshape(img, (1,128,128,3))

    # Predict
    prediction = model.predict(img)
    label = classes[np.argmax(prediction)]

    # Display result
    cv2.putText(frame, f"Prediction: {label}", (10,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Fruit Ripeness Detection", frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()