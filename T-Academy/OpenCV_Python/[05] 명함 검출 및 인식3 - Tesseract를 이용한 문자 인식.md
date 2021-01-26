## Tesseract 사용하기

### Tesseract

- 광학 문자 인식 라이브러리 (영상으로 부터 문자를 인식하는 라이브러리)
- 총 116개의 언어가 제공
- 2018년 4.0이 발표되면서 LSTM 기반 OCR 엔진 및 모델이 추가

### Windows Pre-built 설치 파일 다운로드

- [링크](https://github.com/UB-Mannheim/tesseract/wiki)
- 독일 만하임 대학교 도서관에서 오래된 신문에 의해 OCR을 수행하기 위해 Tesseract 사용

### pytesseract 설치하기

```
pip install pytesseract
```

### opdnCV/numpy와 사용하기

```python
img = cv2.imread('digits.png')
# opencv는 BGR 순서이므로 RGB순서로 바꾸기, 그레이스케일은 그냥 줘도 ok
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
print(pytesseract.image_to_string(img_rgb))
```

