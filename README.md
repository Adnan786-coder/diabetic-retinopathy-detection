# 🩺 Diabetic Retinopathy Detection — End-to-End ML Deployment

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/Framework-PyTorch-orange)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Docker](https://img.shields.io/badge/Container-Docker-blue)

---

## 📖 Executive Summary

This repository contains an **end-to-end Deep Learning system** for **Diabetic Retinopathy detection** from retinal fundus images.

The project demonstrates a **complete Machine Learning deployment pipeline**, transforming a trained model into an interactive medical screening application using **Streamlit and Docker**.

The system analyzes retinal images and classifies them into **five stages of diabetic retinopathy**, assisting in **early detection and medical screening**.

Unlike typical notebook-based projects, this repository demonstrates a **production-style ML workflow**, including:

- Data preprocessing  
- Model training  
- Model inference  
- Web interface  
- Containerized deployment with Docker  

---

## 🧠 Problem Statement

**Diabetic Retinopathy (DR)** is one of the leading causes of **preventable blindness worldwide**.

Early detection can significantly reduce vision loss, but manual screening requires **expert ophthalmologists and significant time**.

This project leverages **Deep Learning and Computer Vision** to automatically detect the severity of diabetic retinopathy from retinal fundus images.

---

## 🧠 Model Overview

The model classifies retinal images into the following **five categories**:

| Class | Condition |
|------|-----------|
| 0 | No DR |
| 1 | Mild |
| 2 | Moderate |
| 3 | Severe |
| 4 | Proliferative DR |

### Example Output

```
Prediction: Moderate DR
Confidence: 0.56
```


---

## 🏗️ Technical Architecture

The project is built using a **modern ML deployment stack**.

### Core Components

- **Deep Learning Framework:** PyTorch  
- **Computer Vision:** Torchvision transforms  
- **User Interface:** Streamlit  
- **Containerization:** Docker  
- **Programming Language:** Python  

---

## ⚙️ Workflow
```
User Uploads Retina Image
        ↓
Image Preprocessing (Resize + Normalize)
        ↓
PyTorch Model (.pth)
        ↓
Softmax Probabilities
        ↓
Predicted DR Severity
        ↓
Streamlit UI Displays Result
```


---

## 📂 Project Structure

```
diabetic-retinopathy-app/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   └── best_dr_model.pth
│
├── src/
│   ├── __init__.py
│   ├── model.py
│   └── preprocess.py
│
└── notebooks/
    └── diabetic-retinopathy.ipynb
```
## 3️⃣ Create Virtual Environment (Recommended)

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```
## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
## 🖥️ Running the Application

### Option A — Run Locally

1. **Launch the Streamlit application:**

   ```bash
   streamlit run app.py
   ```
2. **Open in your browser:**
 ```bash
   http://localhost:8501
   ```

### 🐳 Option B — Run Using Docker

Docker ensures the application runs identically on any machine.

**Build Docker Image**
 ```bash
   docker build -t dr-streamlit .
   ```
**Run Container**
```bash
   docker run -p 8501:8501 dr-streamlit
   ```
**Open the application:**
```bash
   http://localhost:8501
   ```
### 🧠 Model Details

The model is trained using deep convolutional neural networks to learn features from retinal fundus images.
 ```
Image size: 224 × 224
Channels: RGB
   ```
**Preprocessing Steps**

* Image resizing
* Tensor conversion
* Normalization

**Output**
```
  Softmax probabilities across 5 DR classes
   ```
### 📊 Dataset

The model is trained using the APTOS 2019 Blindness Detection Dataset.

The dataset contains retinal fundus images labeled with diabetic retinopathy severity.

**Classes**
```
0 — No DR
1 — Mild
2 — Moderate
3 — Severe
4 — Proliferative DR
   ```
## 🎯 Key Features

✔ **Deep Learning model** for retinal disease detection  
✔ **Interactive Streamlit dashboard**  
✔ **Docker containerization** for reproducibility  
✔ **Clean modular project structure**  
✔ **End-to-end ML deployment workflow**  

---

## 🔬 Future Improvements

Possible enhancements include:

• **Grad-CAM visualization** for model explainability  
• **Model performance monitoring**  
• **Cloud deployment** (AWS / GCP)  
• **API interface** with FastAPI  
• **Larger dataset training**  
