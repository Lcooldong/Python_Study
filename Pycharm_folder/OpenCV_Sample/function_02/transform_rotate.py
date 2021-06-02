import numpy as np
import cv2

def transform_rotate():
    img = cv2.imread('images/2.jpg')
    h, w = img.shape[:2]

    M1 = cv2.getRotationMatrix2D((w/2, h/2), 45, 1)
    M2 = cv2.getRotationMatrix2D((w/2, h/2), 90, 1)

    img2 = cv2.warpAffine(img, M1, (w, h))
    img3 = cv2.warpAffine(img, M2, (w, h))

    cv2.imshow('45-Rotated', img2)
    cv2.imshow('90-Ratated', img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()