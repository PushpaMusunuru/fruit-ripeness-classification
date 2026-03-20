from flask import Flask, render_template, request
import os
import numpy as np
import cv2
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load model
model = load_model("../model/fruit_model.h5")

# Class labels (UPDATE based on your class_indices)
classes = ['overripe', 'ripe', 'unripe']

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def predict_image(filepath):
    img = cv2.imread(filepath)
    img = cv2.resize(img, (128,128))
    img = img / 255.0
    img = np.reshape(img, (1,128,128,3))

    prediction = model.predict(img)
    label = classes[np.argmax(prediction)]

    return label


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            result = predict_image(filepath)

            return render_template('index.html', prediction=result, img_path=filepath)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)