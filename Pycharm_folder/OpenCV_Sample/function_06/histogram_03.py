# 이미지 강조 히스토그램

import numpy as np
import cv2

def histogram_03():
    img = cv2.imread('images/11.jpg', cv2.IMREAD_GRAYSCALE)

    equ = cv2.equalizeHist(img)
    res = np.hstack((img, equ))
    cv2.imshow('equalizer', res)

    cv2.waitKey(0)
    cv2.destroyAllWindows()