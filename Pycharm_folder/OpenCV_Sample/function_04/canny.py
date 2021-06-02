# 15편
# Canny Edge Detection
# 1 노이즈 제거
# 2 Gradient(변화도) 높은 부분 찾기
# 3 Gradient 방향에 따른 픽셀을 두고 최대값이 아닌 픽셀 값 0 만들기
# 3-2 (edge에 기여하지 않은 픽셀 제거)
# 4 문턱값 2개(max, min) 사이 값을 판단, max보다 높으면 edge

import numpy as np
import cv2
import matplotlib.pyplot as plt

def canny():
    img = cv2.imread('images/2.jpg', cv2.IMREAD_GRAYSCALE)

    edge1 = cv2.Canny(img, 50, 200)     # min thresholding val, max thresholding val
    edge2 = cv2.Canny(img, 100, 200)
    edge3 = cv2.Canny(img, 170, 200)

    cv2.imshow('original', img)
    cv2.imshow('Canny Edge1', edge1)
    cv2.imshow('Canny Edge2', edge2)
    cv2.imshow('Canny Edge3', edge3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()