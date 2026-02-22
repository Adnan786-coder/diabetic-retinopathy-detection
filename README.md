# 🩺 Diabetic Retinopathy Detection using Deep Learning

An end-to-end Deep Learning project to detect and classify Diabetic Retinopathy severity from retinal fundus images using CNNs and Transfer Learning.

---

## 📌 Problem Statement

Diabetic Retinopathy (DR) is a diabetes complication that affects the eyes and can lead to blindness if not detected early.

The goal of this project is to automatically classify retinal fundus images into 5 severity levels using Deep Learning.

---

## 📊 Dataset

Dataset used: **APTOS 2019 Blindness Detection**

Source: Kaggle  
Images: High-resolution retinal fundus images  
Classes:

| Label | Severity Level |
|-------|----------------|
| 0     | No DR |
| 1     | Mild |
| 2     | Moderate |
| 3     | Severe |
| 4     | Proliferative DR |

---

## 🧠 Approach

### 1️⃣ Data Preprocessing
- Image resizing to 224x224
- Normalization
- Data augmentation
- Train-validation split

### 2️⃣ Model Architecture
- Transfer Learning (ResNet / CNN)
- CrossEntropy Loss
- Adam Optimizer
- GPU Training (if available)

### 3️⃣ Training
- Epoch-wise loss and accuracy tracking
- Model checkpoint saving
- Evaluation on validation data

---

## 📈 Results

- Final Validation Accuracy: ~XX%
- Training Loss Decreased Consistently
- Model Generalizes Well on Validation Set

(Add confusion matrix screenshot here later)

---

## 🛠️ Tech Stack

- Python
- PyTorch
- NumPy
- Pandas
- Matplotlib
- Kaggle API

---

## 📂 Project Structure
