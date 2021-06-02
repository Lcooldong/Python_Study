# GRADIENT : Dilation 과 Erosion 이미지 차이를 나타냄
# TOPHAT : 원본 이미지와 opening 이미지 차이
# BLACKHAT : 원본 이미지와 closing 이미지 차이

import numpy as np
import cv2

def morph_03():
    img1 = cv2.imread('images/alphabet.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('images/A.jpg', cv2.IMREAD_GRAYSCALE)
    img3 = cv2.imread('images/B.jpg', cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((3, 3), np.uint8)

    grad = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)
    tophat = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(img3, cv2.MORPH_BLACKHAT, kernel)

    cv2.imshow('function_04', grad)
    cv2.imshow('tophat', tophat)
    cv2.imshow('blackhat', blackhat)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
