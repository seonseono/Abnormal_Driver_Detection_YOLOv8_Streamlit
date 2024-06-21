# Python In-built packages
from pathlib import Path
from PIL import Image
import io
import requests

import streamlit as st
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="Driver's Behavior Detection using YOLO",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("🚚 운전자 이상 행동 탐지 with YOLOv8")

# Sidebar
st.sidebar.header("Model Config")

# Model Options
model_type = st.sidebar.radio("Select Task", ['Detection'])

confidence = float(st.sidebar.slider("Select Model Confidence", 25, 100, 40)) / 100

# Selecting Detection Or Segmentation
if model_type == 'Detection':
    model_path = settings.DETECTION_MODEL

# Load Pre-trained Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

st.sidebar.header("Image/Video Config")
source_radio = st.sidebar.radio("Select Source", settings.SOURCES_LIST)

source_img = None

# Image is selected
if source_radio == settings.IMAGE:
    source_img = st.sidebar.file_uploader("Choose an image...", type=("jpg", "jpeg", "png"))

    col1, col2 = st.columns(2)

    with col1:
        try:
            if source_img is None:
                default_image_path = settings.DEFAULT_IMAGE
                default_image = Image.open(io.BytesIO(requests.get(default_image_path).content))
                st.image(default_image, caption="Default Image", use_column_width=True)
            else:
                uploaded_image = Image.open(io.BytesIO(source_img.read()))
                st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        except Exception as e:
            st.error(f"Error loading image: {e}")

    with col2:
        if source_img is None:
            default_detected_image_path = settings.DEFAULT_DETECT_IMAGE
            default_detected_image = Image.open(io.BytesIO(requests.get(default_detected_image_path).content))
            st.image(default_detected_image, caption="Detected Image", use_column_width=True)
        else:
            if st.sidebar.button('Detect Objects'):
                res = model.predict(uploaded_image,
                                    conf=confidence
                                    )
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                st.image(res_plotted, caption='Detected Image',
                         use_column_width=True)
                try:
                    with st.expander("Detection Results"):
                        for box in boxes:
                            st.write(box.data)
                except Exception as ex:
                    st.write("No image is uploaded yet!")

# Video is selected
elif source_radio == settings.VIDEO:
    helper.play_stored_video(confidence, model)

# YouTube is selected
elif source_radio == settings.YOUTUBE:
    video_url = st.sidebar.text_input("Enter YouTube video URL:")
    if st.sidebar.button("Load YouTube Video"):
        helper.play_youtube_video(video_url, confidence, model)
