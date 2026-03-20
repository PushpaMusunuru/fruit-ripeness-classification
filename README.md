
# 🍌 Fruit Ripeness Classification using CNN

## 📌 Project Overview
This project is a deep learning-based image classification system that identifies the ripeness stage of fruits (banana) into:
- Unripe
- Ripe
- Overripe

The model is built using Convolutional Neural Networks (CNN) and allows users to upload an image through a web interface to get predictions.

---

## 🚀 Features
- Image classification using CNN
- Data augmentation for improved accuracy
- Web interface for image upload (Flask)
- Real-time prediction output
- Clean and modular project structure

---

## 🛠️ Tech Stack
- Python
- TensorFlow / Keras
- OpenCV
- Flask
- NumPy

---

## 📂 Project Structure
fruit-ripeness-classification/
│── dataset/ # (ignored in GitHub)
│── model/
│ ├── train.py
│ ├── test.py
│── app/
│ ├── app.py
│ ├── templates/
│ │ └── index.html
│ ├── static/
│ └── uploads/
│── requirements.txt
│── README.md
│── .gitignore

---

## 📊 Dataset
- Dataset sourced from Kaggle
- Contains images categorized into:
  - Unripe
  - Ripe
  - Overripe

⚠️ Note: Dataset is not included due to size limitations.

---

## Model Details
- CNN with multiple convolution + pooling layers
- Input size: 128x128
- Optimizer: Adam
- Loss: Categorical Crossentropy

---

## How to Run

### 1️ Install dependencies
pip install -r requirements.txt

### 2️ Train the model
python model/train.py

### 3 Run the Flask app
python app/app.py

### 4️ Open browser
http://127.0.0.1:5000/

---

##  Output
- Upload an image
- Get prediction:
  - Unripe / Ripe / Overripe

---

##  Notes
- Model file is not uploaded due to size limitations
- You can train the model locally using the provided script

---

## Future Improvements
- Support multiple fruits (apple, mango)
- Improve accuracy using transfer learning
- Deploy as a web application
- Add confidence score to predictions

---

## Author
Rama Pushpa Latha Musunuru
