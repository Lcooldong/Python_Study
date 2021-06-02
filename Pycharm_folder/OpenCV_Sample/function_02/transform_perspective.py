# 기울여진 사진 바로 세울 수 있음

import numpy as np
import cv2

def transform_perspective():
    img = cv2.imread('images/1.png')
    h, w = img.shape[:2]

    pts1 = np.float32([[0, 0], [300,0], [0, 300], [300, 300]])
    pts2 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])

    M = cv2.getPerspectiveTransform(pts1, pts2)

    img2 = cv2.warpPerspective(img, M, (w, h))

    cv2.imshow('original', img)
    cv2.imshow('Perspective-Transform', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
