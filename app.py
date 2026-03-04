import streamlit as st
import torch
from PIL import Image

from src.model import load_model, class_names
from src.preprocess import get_transform

st.set_page_config(page_title="DR Detection")

st.title("🩺 Diabetic Retinopathy Detection")
st.warning("⚠ Prototype model — Not for medical use.")

@st.cache_resource
def get_model():
    return load_model("model/best_dr_model.pth")

model = get_model()
transform = get_transform()

uploaded_file = st.file_uploader("Upload retinal image", type=["jpg","png","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image)

    image_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image_tensor)
        probs = torch.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probs, 1)

    st.success(class_names[predicted.item()])
    st.progress(float(confidence.item()))
    st.write(f"Confidence: {confidence.item()*100:.2f}%")
