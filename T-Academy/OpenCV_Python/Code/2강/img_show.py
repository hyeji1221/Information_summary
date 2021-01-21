import cv2
import sys

# 영상 불러오기 -> numpy.ndarray 형태
img = cv2.imread('cat.bmp')
# img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE) # 흑백 사진으로 불러오기

if img is None: # 이미지가 없는 경우
    print('Image load failed!')
    sys.exit()

print(type(img))  # numpy.ndarray
print(img.shape)  # (480, 640, 3) -> 3 이므로 BGR 순서로 컬러정보 저장
print(img.dtype)  # uint8 -> 0~255 까지의 정수 표현 (data type)

# 영상 화면 출력
# cv2.namedWindow('image') # 새로운 창을 만들어준다 -> 없어도 Ok
cv2.imshow('image', img) # image라는 창에 img 출력 , image라는 창이 없으면 새로 만든다
# cv2.waitKey() # 화면이 바로 꺼지는 것을 막는다 -> Key 입력을 기다림 -> 모든 키 입력 가능

while True:
    if cv2.waitKey() == 27:  # ESC
        break

# cv2.destroyAllWindows() # 만들어진 모든 창 닫기 -> 생략해도 OK

