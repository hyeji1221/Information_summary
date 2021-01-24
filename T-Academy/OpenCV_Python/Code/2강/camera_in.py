import sys
import cv2

cap = cv2.VideoCapture(0)   # 0번 카메라 오픈

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

while True:
    ret, frame = cap.read()  # 무한루프 돌면서 한 프레임씩 카메라에서 가져오기
    
    if not ret:
        break

    edge = cv2.Canny(frame, 50, 150)    
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)    # 외곽선 부분만 검출

    if cv2.waitKey(1) == 27:  # 동영상은 1로 두면 너무 빨리 플레이된다.
        break    

    
    

cap.release()
cv2.destroyAllWindows()