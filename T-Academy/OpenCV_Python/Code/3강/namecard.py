import sys
import numpy as np
import cv2

src = cv2.imread('namecard2.jpg')

if src is None:
    print('image load failed')
    sys.exit()

#src = cv2.resize(src, (640, 480))
src = cv2.resize(src, (0, 0), fx = 0.5, fy = 0.5)

# src -> 그레이스케일로 변환
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# src_gray -> 이진화
th, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print(th)   # threshold 값
cv2.imshow('src', src)
cv2.imshow('src_gray', src_gray)
cv2.imshow('src_bin', src_bin)

cv2.waitKey()
cv2.destroyAllWindows()    