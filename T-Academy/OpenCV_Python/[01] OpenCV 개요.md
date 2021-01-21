# 컴퓨터 비전

- 영상 또는 이미지를 보고 무엇인지 검출 또는 인식햐는 등의 high-level understanding
- 사람의 시각 시스템을 컴퓨터가 똑같이 묘사할 수 있게 하는 작업

## 관련 분야

<img src = "https://user-images.githubusercontent.com/59350891/105370395-e38bfb00-5c46-11eb-98a0-d9f364ce7ba8.png" width = 60%>

## 연구 분야

- 영샹의 화질 개선
  + Filtering App
  + HDR
  + Image Noise Remove
  + Super Resolution - TV에 많이 적용
- 객체 검출
- 분할
- 인식
- 움직임 정보 추출 및 추적

## 응용 분야

- 머신 비전
  + 공장 자동화: 제품 불량 검사, 위치 확인, 측정 등
  + 높은 정확도와 빠른 처리 시간 요구
  + 조명, 렌즈, 필터, 실시간 처리
- 인공지능(AI) 서비스
  + 인공지능 로봇과 자율 주행 자동차
  + 입력 영사을 객체와 배경으로 분할 -> 객체와 배경 인식 -> 상황 인식 -> 로봇과 자동차의 행동 지시
  + Computer Vision + Sensor Fusion + Deep Learning
  + Amazon Go / 구글, 테슬라의 자율 주행 자동차

# 영상

## 영상의 획득

### 디지털 카메라에서 영상의 획득 과정

<img src = "https://user-images.githubusercontent.com/59350891/105373624-387d4080-5c4a-11eb-9ec6-d052ddb0a7f5.png" width = 55%>

- 센서 
  + 광학적 신호를 전기적 신호로 변환
  + <img src = "https://user-images.githubusercontent.com/59350891/105374032-9ad64100-5c4a-11eb-934c-52dfd8276269.png" width = 60%>
  + ISP : 영상처리 모듈(noise를 제거 or 밝기 조정 or 색감 조정 등)

## 영상의 표현 방법

- ### **그레이스케일 영상**

  + 하나의 픽셀이 색상 정보 없이 밝기 정보로만 구성된 영상

  + 밝기 정보를 256 단계로 표현 -> 가장 어두우면 0(검정색), 가장 밝으면 255(흰색)

  + C/C++ 에서 unsigned char로 표현 (1 byte)

    ```c
    typedef unsigned char Byte; // Windows
    typedef unsigned char uchar; // OpenCV
    ```

  + Python에서는? -> **numpy.uint8**

- ### **트루컬러 영상**

  + 컬러 사진처럼 색상 정보를 가짐 -> 다양한 색상 표현 가능
  + RGB 성분을 256 단계로 표현 -> 256^3 = 16,777,216 색상 표현 가능
  + 한 픽셀이 3개의 값을 가짐(C) or 3개의 프레임을 만들어 표현, 3차원 행렬  (Python)

  <img src="https://user-images.githubusercontent.com/59350891/105376260-e689ea00-5c4c-11eb-8ad0-f7416c5fcd86.png" width = 50%>

- ###  **픽셀**

  + 영상의 기본 단위, 화소

###  영상이란?

- 픽셀이 바둑판 모양의 격자에 나열되어 있는 형태 (2차원 행렬)
- 각각의 점이 RGB에 대한 강도를 가진다

<img src = "https://user-images.githubusercontent.com/59350891/105374350-f274ac80-5c4a-11eb-9e38-7323b700316a.png" width = 60%>

### 영상에서 사용되는 자표계

- 2차원으로 구성
- OpenCV는 행렬로 구성
- 영상을 표현할 때는 가로 X 세로 형태로 표시하지만 행렬을 다룰 때는 세로 X 가로로 표현 (해상도)

<img src="https://user-images.githubusercontent.com/59350891/105374736-5dbe7e80-5c4b-11eb-863c-5629d7c1b405.png" width = 50%>

### 영상 데이터 크기 분석

- 그레이스케일 영상 : (가로 크기) X (세로 크기) Bytes
- 트루컬러 영상 : (가로 크기) X (세로 크기) X 3 Bytes
  + 보통 1초에 30프레임 -> 1초 플레이하는데 180MB 필요 (1920X1080) -> 용량이 매우 크다 -> 시간이 많이 걸린다

## 영상 파일 형식 특징

| 종류 | 특징                                                         |
| :--: | :----------------------------------------------------------- |
| BMP  | - 픽셀 데이터 압축 X 그대로 사용 -> 용량 큼<br />- 파일 구조 단순 -> 별도의 라이브러리 없이 직접 파일 입출력 프로그래밍 가능 |
| JPG  | - 주로 사진 같은 컬러 영상 저장을 위해 사용<br />- 손실 압축 -> 픽셀 값이 미세하기 바뀜 -> 영상 처리에서 선호 X<br />- 압축률이 좋음 -> 파일 용량 크게 감소 -> 디지털 카메라 사진 포맷으로 주로 사용 |
| GIF  | - 256 색상 이하의 영상 저장 -> 일반 사진 저장 시 화질 열화 심함<br />- 무손실 압축<br />- 움직이는 GIF 지원 |
| PNG  | - Portable Network Graphics<br />- 무손실 압축<br />- 알파 채널(투명도) 지원 |

영상처리에서는 **TIF 또는 PNG**를 주로 사용

# OpenCV

## What is OpenCV?

- Open source
- Computer vision & machine learning
- Software library

## Why OpenCV?

- BSD license -> Free for academic & commercial use
- Multiple interface -> C, C++, Python, Java, JavaScript, MATLAB, etc.

## OpenCV 구성

- 모든 소스코드가 병렬 처리 형태로 구성 -> CPU의 모든 코어 사용

<img src="https://user-images.githubusercontent.com/59350891/105379146-e50df100-5c4f-11eb-851f-42c85cdbb9bf.png" alt="image" style="zoom:70%;" />

