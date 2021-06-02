# opening : erosion-> dilation  원래 크기   erosion(배경화) 배경근처 삭제
# closing : dilation-> erosion 원래 크기    dilation(사물화) 사물 근처 삭제


import numpy as np
import cv2

def morph_02():
    img1 = cv2.imread('images/A.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('images/B.jpg', cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((5, 5), np.uint8)

    opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()