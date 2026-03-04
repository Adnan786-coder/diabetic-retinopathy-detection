🩺 Diabetic Retinopathy Detection — End-to-End ML Deployment










📖 Executive Summary

This repository contains an end-to-end Deep Learning system for Diabetic Retinopathy detection from retinal fundus images.

The project demonstrates a complete Machine Learning deployment pipeline, transforming a trained model into an interactive medical screening application using Streamlit and Docker.

The system analyzes retinal images and classifies them into five stages of diabetic retinopathy, assisting in early detection and medical screening.

Unlike typical notebook-based projects, this repository shows a production-ready ML workflow, including:

Data preprocessing

Model training

Model inference

Web interface

Containerized deployment with Docker

🧠 Problem Statement

Diabetic Retinopathy (DR) is one of the leading causes of preventable blindness worldwide.

Early detection can significantly reduce vision loss, but manual screening requires expert ophthalmologists and significant time.

This project leverages Deep Learning and Computer Vision to automatically detect the severity of diabetic retinopathy from retinal fundus images.

🧠 Model Overview

The model classifies retinal images into the following five categories:

Class	Condition
0	No DR
1	Mild
2	Moderate
3	Severe
4	Proliferative DR

The system outputs:

Prediction: Moderate DR
Confidence: 0.56
🏗️ Technical Architecture

The project is built using a modern ML deployment stack.

Core Components

Deep Learning Framework: PyTorch

Computer Vision: Torchvision transforms

User Interface: Streamlit

Containerization: Docker

Programming Language: Python

Workflow
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
📂 Project Structure
diabetic-retinopathy-app/
│
├── app.py                 # Streamlit Web Application
├── Dockerfile             # Docker container instructions
├── requirements.txt       # Python dependencies
│
├── model/
│   └── best_dr_model.pth  # Trained PyTorch model
│
├── src/                   # Helper scripts (preprocessing / utilities)
│
└── README.md              # Project documentation
🚀 Installation & Setup
1️⃣ Prerequisites

Ensure the following are installed:

Python 3.10+

Git

Docker (optional but recommended)

2️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/diabetic-retinopathy-detection.git

cd diabetic-retinopathy-detection
3️⃣ Create Virtual Environment (Recommended)

Linux / macOS:

python3 -m venv venv
source venv/bin/activate

Windows:

python -m venv venv
venv\Scripts\activate
4️⃣ Install Dependencies
pip install -r requirements.txt
🖥️ Running the Application
Option A — Run Locally

Launch the Streamlit application:

streamlit run app.py

Then open:

http://localhost:8501

Upload a retinal image and receive a model prediction instantly.

🐳 Option B — Run Using Docker

Docker ensures the application runs identically on any machine.

Build Docker Image
docker build -t dr-streamlit .
Run Container
docker run -p 8501:8501 dr-streamlit

Open the application:

http://localhost:8501
🧠 Model Details

The model is trained using deep convolutional neural networks to learn features from retinal fundus images.

Input
Image size: 224 × 224
Channels: RGB
Preprocessing Steps

Image resizing

Tensor conversion

Normalization

Output
Softmax probabilities across 5 DR classes
📊 Dataset

The model is trained using the APTOS 2019 Blindness Detection Dataset.

Dataset contains retinal fundus images labeled with diabetic retinopathy severity.

Classes:

0 — No DR
1 — Mild
2 — Moderate
3 — Severe
4 — Proliferative DR
🎯 Key Features

✔ Deep Learning model for retinal disease detection
✔ Interactive Streamlit dashboard
✔ Docker containerization for reproducibility
✔ Clean modular project structure
✔ End-to-end ML deployment workflow

🔬 Future Improvements

Possible enhancements include:

Grad-CAM visualization for model explainability

Model performance monitoring

Cloud deployment (AWS / GCP)

API interface with FastAPI

Larger dataset training
