import numpy as np
import cv2

# Gaussian filter : 가우스 노이즈 제거
# Median filter : 소금 후추 노이즈 제거
# bilateral filter : 성능은 느리나 edge 놔두고, 표면 질감 등을 제거

def onMouse(x):
    pass

def bluring():
    img = cv2.imread('images/7.jpg')

    cv2.namedWindow('BlurPane')
    cv2.createTrackbar('BLUR_MODE', 'BlurPane', 0, 3, onMouse)  # 0,1,2,3
    cv2.createTrackbar('BLUR', 'BlurPane', 0, 8, onMouse)   # 0~8

    mode = cv2.getTrackbarPos('BLUR_MODE', 'BlurPane')
    val = cv2.getTrackbarPos('BLUR', 'BlurPane')

    while True:
        val = val*2 + 1     # 홀수로 만듬

        try:
            if mode == 0:
                blur = cv2.blur(img, (val, val), 0)  # val 필터 커널 사이즈, 둘 달라도됨
            elif mode == 1:
                blur = cv2.GaussianBlur(img, (val, val), 0)  # val 양의 홀수, 둘 달라도됨
            elif mode == 2:
                blur = cv2.medianBlur(img, val)  # val 커널 사이즈
            elif mode == 3:
                blur = cv2.bilateralFilter(img, 9, val, val)
            else:
                break

            cv2.imshow('BlurPane', blur)

        except:
            break

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        mode = cv2.getTrackbarPos('BLUR_MODE', 'BlurPane')
        val = cv2.getTrackbarPos('BLUR', 'BlurPane')

    cv2.destroyAllWindows()