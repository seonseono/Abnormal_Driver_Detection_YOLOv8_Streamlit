# 운전자 이상 행동 탐지를 위한 객체 탐지 프로젝트</span>
교통사고 발생 원인 1위는 전방 주시 태만입니다. 졸음 운전은 음주 운전보다도 더 많은 피해자를 발생시키고, 특히 화물차에서 대부분의 졸음 운전 사고가 발생합니다. 장거리 운전이 불가피한 화물 운전자들의 안전과 물류 회사의 운영 효율을 위해 이상 행동 감지 카메라를 개발하고자 합니다. 


## YOLOv8을 사용한 실시간 객체 탐지 및 추적</span>
YOLO 모델 학습을 위해 AI 허브의 [운전자 및 탑승자 상태 및 이상행동 모니터링](<https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=651>) 데이터를 사용했습니다. 30,000장의 운전자 이미지를 정상, 졸음, 물건 찾기, 핸드폰 사용 4개 class로 직접 라벨링해 학습을 진행했습니다. YOLOv5, 7, 8, 9 모델을 학습시킨 후 비교했고 P, R, mAP50, mAP50-95 성능이 가장 우수한 YOLOv8 모델을 채택했습니다. 


|    Box(P)   |      R      |    mAP50    |   mAP50-95  |
|-------------|-------------|-------------|-------------|
|     0.90    |    0.912    |    0.951    |    0.595    |


## Streamlit 서버의 WebApp Demo</span>
이 링크 [webapp](https://codingmantras-yolov8-streamlit-detection-tracking-app-njcqjg.streamlit.app/) 에서 Streamlit Web Application을 사용할 수 있습니다. 


## 페이지 설명</span>
- Image
- Video
- Youtube
세 가지 소스의 탐지가 가능합니다. 페이지에 첨부된 이미지, 동영상뿐만 아니라 사용자가 직접 파일 혹은 링크를 업로드하여 학습된 YOLOv8 모델을 사용해볼 수 있습니다. 

## 개선 방안</span>
운전석이 좌측에 있는 40대 남성의 이미지로 학습을 진행해 운전석이 우측에 있는 경우, 촬영 카메라의 위치가 학습에 사용한 데이터와 크게 다른 경우 Detection이 제대로 이뤄지지 않는 한계가 있습니다. 한국의 화물, 물류 차량 대부분이 좌측 운전석인 점을 감안하면 큰 문제는 아니라고 생각하나, 모델의 정확도 개선을 위해 더 많은 데이터를 사용해 모델을 학습시킬 계획입니다. 


## Acknowledgements
부산 SW 전문인재양성과정 4기 최종 팀 프로젝트입니다. 
이 모델은 객체 탐지 알고리즘 [YOLOv8](<https://github.com/ultralytics/ultralytics>) 을 사용하고, [Streamlit](<https://github.com/streamlit/streamlit>) 으로 WepApp을 구현했습니다. 
Streamlit 구현은 아래 레파지토리를 참고했습니다. 
(https://github.com/CodingMantras/yolov8-streamlit-detection-tracking)

