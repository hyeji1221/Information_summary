import sys
import numpy as np
import cv2

src = cv2.imread('namecard1.jpg')

if src is None:
    print('image load failed')
    sys.exit()

#src = cv2.resize(src, (640, 480))
# src = cv2.resize(src, (0, 0), fx = 0.4, fy = 0.4)

# src -> 그레이스케일로 변환
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# src_gray -> 이진화
th, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print(th)   # threshold 값

contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(contours)) # 키보드 자판의 countours 까지도 포함한 외곽선

for pts in contours:
    if cv2.contourArea(pts) < 1000:
        continue

    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)

    if len(approx) != 4: # 4각형으로 근사화가 되지 않으면
        continue

    w, h = 900, 500
    srcQuad = np.array([[approx[0, 0, :]], [approx[1, 0, :]], [approx[2, 0, :]], [approx[3, 0, :]]]).astype(np.float32)
    dstQuad = np.array    ([[0,0], [0,h], [w, h], [w,0]]).astype(np.float32) # 직접 넣기
    pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
    dst = cv2.warpPerspective(src, pers, (w, h))


    cv2.polylines(src, pts, True, (0, 0, 255)) # 빨간 색으로 외곽선을 그림 (B,G,R)

cv2.imshow('src', src)
cv2.imshow('src_gray', src_gray)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()    