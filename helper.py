from ultralytics import YOLO
import streamlit as st
import cv2
from pytube import YouTube
import requests
import settings
import numpy as np

def load_model(model_path):
    """
    Loads a YOLO object detection model from the specified model_path.

    Parameters:
        model_path (str): The path to the YOLO model file.

    Returns:
        A YOLO object detection model.
    """
    model = YOLO(model_path)
    return model

def display_tracker_options():
    display_tracker = st.radio("Display Tracker", ('Yes', 'No'))
    is_display_tracker = True if display_tracker == 'Yes' else False
    if is_display_tracker:
        tracker_type = st.radio("Tracker", ("bytetrack.yaml", "botsort.yaml"))
        return is_display_tracker, tracker_type
    return is_display_tracker, None

def _display_detected_frames(conf, model, st_frame, image, is_display_tracking=None, tracker=None):
    """
    Display the detected objects on a video frame using the YOLOv8 model.

    Args:
    - conf (float): Confidence threshold for object detection.
    - model (YoloV8): A YOLOv8 object detection model.
    - st_frame (Streamlit object): A Streamlit object to display the detected video.
    - image (numpy array): A numpy array representing the video frame.
    - is_display_tracking (bool): A flag indicating whether to display object tracking (default=None).

    Returns:
    None
    """
    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720*(9/16))))

    # Display object tracking, if specified
    if is_display_tracking:
        res = model.track(image, conf=conf, persist=True, tracker=tracker)
    else:
        # Predict the objects in the image using the YOLOv8 model
        res = model.predict(image, conf=conf)

    # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted, caption='Detected Video', channels="BGR", use_column_width=True)

def stream_video_from_youtube(video_url):
    """
    Streams video from a given YouTube URL using OpenCV and processes it with YOLOv8.

    Parameters:
        video_url (str): URL of the YouTube video to stream.

    Returns:
        Generator yielding video frames.
    """
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_url = stream.url
        cap = cv2.VideoCapture(video_url)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            yield frame
        cap.release()
    except Exception as e:
        st.error(f"Failed to stream video from YouTube: {e}")

def play_youtube_video(video_url, conf, model):
    """
    Plays a YouTube video. Tracks and detects objects in real-time using the YOLOv8 object detection model.

    Parameters:
        video_url (str): URL of the YouTube video.
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.

    Returns:
        None
    """
    try:
        st_frame = st.empty()
        for frame in stream_video_from_youtube(video_url):
            _display_detected_frames(conf, model, st_frame, frame)
    except Exception as e:
        st.error(f"Error streaming YouTube video: {e}")

def play_stored_video(conf, model):
    """
    Plays a stored video file from a YouTube URL. Tracks and detects objects in real-time using the YOLOv8 object detection model.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.

    Returns:
        None

    Raises:
        None
    """
    source_vid = st.sidebar.selectbox("Choose a video...", settings.VIDEOS_DICT.keys())

    is_display_tracker, tracker = display_tracker_options()

    video_url = settings.VIDEOS_DICT.get(source_vid)
    st.info(f"Original video URL: {video_url}")

    try:
        st_frame = st.empty()
        for frame in stream_video_from_youtube(video_url):
            _display_detected_frames(conf, model, st_frame, frame, is_display_tracker, tracker)
    except Exception as e:
        st.error(f"Error streaming video: {e}")
