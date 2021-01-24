# OpenCV 

 [**OpenCV API 최신 도움말 찾기**](http://docs.opencv.org/master/)

## API

### 영상 파일 불러오기

```python
cv2.imread(filename, flags = None)
```

|      flags 옵션      |                             설명                             |
| :------------------: | :----------------------------------------------------------: |
|   cv2.IMREAD_COLOR   | BGR 컬러 영상으로 읽기 (기본값)<br />shpae = (rows, cols, 3) |
| cv2.IMREAD_GRAYSCALE |     그레이스케일 영상으로 읽기<br />shpe = (rows, cols)      |
| cv2.IMREAD_UNCHANGED | 영상 파일 속성 그대로 읽기<br />투명한 PNG 파일 : shape = (rows, cols, 4) |

### 영상 파일 저장하기

````python
cv2.imwrite(filename, img, params = None) -> retval
````

- params : 파일 저장 옵션 지정 (속성 & 값의 정수 쌍
  + JPG 파일 압축률 90% -> [cv2.IMWRITE_JPEG_QUALITY, 90]
- retval : 정상적으로 저장하면 True, 실패하면 False

### 창 위치 & 크기 지정

```
cv2.moveWindow(winname, x, y) -> None
cv2.resizeWindow(winname, width, height) -> None
```

## matplotlib을 이용한 영상 출력

#### 컬러 영상 출력

색상 정보가 RGB 순서여야 함

그러나 cv2.imread() 함수로 불러온 영상의 색상 정보는 BGR 순서이므로 **cv2.cvtColor()** 함수를 이용하여 순서를 변경한다

#### 그레이스케일 영상 출력

plt.imshow() 함수에서 컬러맵을 `cmap='gray'`로 지정

## 카메라 & 영상 처리

#### cv2.VideoCapture 클래스

- openCV에서는 카메라와 동영상으로부터 프레임을 받아오는 작업을 cv2.VidioCapture 클래스 하나로 처리함

#### 동영상, 정지 영상 시퀀스, 비디오 스트림 열기

```
cv2.VideoCapture(filename, apiPreference=None) -> retval
```

- filename : avi or jpg or 비디오 스트림 url
- apiPreference : 선호하는 동영상 처리 방법 지정
- retval : cv2.VideoCapture 객체

```
cv2.VideoCapture.open(filename, apiPreference=None) -> retval
```

- retval : 성공하면 True, 실패하면 False

#### 카메라 열기

```
cv2.VideoCapture(index, apiPreference=None) -> retval
```

- index : camera_id + domain_offset (CAP_*) id
  + camera_id == 0 이면 시스템 기본 카메라
  + domain_offset == 0 이면 auto detect.
  + 기본 카메라를 기본 방법으로 열려면 index에 0을 전달
- apiPreference : 선호하는 동영상 처리 방법 지정
- retval : cv2.VideoCapture 객체

```
cv2.VideoCapture.open(index, apiPreference=None) -> retval
```

- retval : 성공하면 True, 실패하면 False

:white_check_mark: **filename(문자열)이 들어가면 동영상 파일 open, 정수 값이 들어가면 카메라 디바이스 오픈**

