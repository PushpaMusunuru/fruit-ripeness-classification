
# 🍌 Fruit Ripeness Classification using CNN

## 📌 Project Overview
This project is a deep learning-based image classification system that identifies the ripeness stage of fruits (banana) into:
- Unripe
- Ripe
- Overripe

The model is built using Convolutional Neural Networks (CNN) and allows users to upload an image through a web interface to get predictions.

---
<img width="901" height="927" alt="Screenshot 2026-03-22 174042" src="https://github.com/user-attachments/assets/73632a11-b879-4cbb-a444-beac28c4107f" />


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
