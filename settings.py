from pathlib import Path
import sys

# Absolute Path ROOT
ROOT = Path(__file__).resolve().parent

# sys.path ROOT
if ROOT not in sys.path:
    sys.path.append(str(ROOT))

# Source Type
IMAGE = 'Image'
VIDEO = 'Video'
YOUTUBE = 'YouTube'

SOURCES_LIST = [IMAGE, VIDEO, YOUTUBE]

# Image
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = 'https://github.com/seonseono/Abnormal_Driver_Detection_YOLOv8_Streamlit/blob/main/images/01.jpg?raw=true'
DEFAULT_DETECT_IMAGE = 'https://github.com/seonseono/Abnormal_Driver_Detection_YOLOv8_Streamlit/blob/main/images/02.jpg?raw=true'

# Video
# VIDEO_DIR = ROOT / 'videos'
# VIDEOS_DICT = {
#     'video_1': 'https://www.youtube.com/watch?v=BZjaStb53so',
#     'video_2': 'https://www.youtube.com/watch?v=3LhJsKadwhw',
#     'video_3': 'https://www.youtube.com/watch?v=cvBF0WCU5BM',
# }

VIDEO_DIR = ROOT / 'videos'
VIDEOS_DICT = {
    'video_1': VIDEO_DIR / 'video_1.mp4',
    'video_2': VIDEO_DIR / 'video_2.mp4',
    'video_3': VIDEO_DIR / 'video_3.mp4',
}

# Model
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = 'weights/yolov8n.pt'

# # Debugging
# print(f"ROOT: {ROOT}")
# print(f"IMAGES_DIR: {IMAGES_DIR}")
# print(f"NORAML_DETECT_IMAGE: {DEFAULT_IMAGE}")
# print(f"DROWSY_DETECT_IMAGE: {DEFAULT_DETECT_IMAGE}")
# print(f"VIDEO_DIR: {VIDEO_DIR}")
# print(f"VIDEOS_DICT: {VIDEOS_DICT}")
# print(f"MODEL_DIR: {MODEL_DIR}")
# print(f"DETECTION_MODEL: {DETECTION_MODEL}")

# # URL Validity Check
# for key, url in VIDEOS_DICT.items():
#     if not url.startswith('http'):
#         print(f"Warning: {key} does not appear to be a valid URL: {url}")
