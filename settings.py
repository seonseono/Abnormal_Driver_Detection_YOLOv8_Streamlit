from pathlib import Path
import sys

# 절대 경로 ROOT 설정
ROOT = Path(r'C:\Users\seono\Desktop\Abnormal_Driver_Detection_YOLOv8_Streamlit')

# sys.path ROOT 추가
if ROOT not in sys.path:
    sys.path.append(str(ROOT))

# Source Type
IMAGE = 'Image'
VIDEO = 'Video'
YOUTUBE = 'YouTube'

SOURCES_LIST = [IMAGE, VIDEO, YOUTUBE]

# Image
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / '01.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / '02.jpg'

# Video
VIDEO_DIR = ROOT / 'videos'
VIDEOS_DICT = {
    'video_1': VIDEO_DIR / 'video_1.mp4',
    'video_2': VIDEO_DIR / 'video_2.mp4',
    'video_3': VIDEO_DIR / 'video_3.mp4',
}

# Model
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'yolov8n.pt'
# 사용자 지정 모델을 사용할 경우 아래 줄의 주석을 해제하고 파일명을 입력하세요.
# DETECTION_MODEL = MODEL_DIR / 'my_detection_model.pt'


# Debugging
print(f"ROOT: {ROOT}")
print(f"IMAGES_DIR: {IMAGES_DIR}")
print(f"NORAML_DETECT_IMAGE: {DEFAULT_IMAGE}")
print(f"DROWSY_DETECT_IMAGE: {DEFAULT_DETECT_IMAGE}")
print(f"VIDEO_DIR: {VIDEO_DIR}")
print(f"VIDEOS_DICT: {VIDEOS_DICT}")
print(f"MODEL_DIR: {MODEL_DIR}")
print(f"DETECTION_MODEL: {DETECTION_MODEL}")

# File Exist
for key, path in VIDEOS_DICT.items():
    if not path.exists():
        print(f"Warning: {key} does not exist at path: {path}")
