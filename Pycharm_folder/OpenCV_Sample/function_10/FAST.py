# 40 편

import numpy as np
import cv2

def FAST():
    img = cv2.imread('images/corner.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2, img3 = None, None

    # threshold 값 30  클수록 키포인트 개수 감소
    fast = cv2.FastFeatureDetector_create(30)
    # Non-maximal Suppression True
    kp = fast.detect(img, None)  # kp 코너이면 True
    img2 = cv2.drawKeypoints(img, kp, img2, (255, 0, 0))
    cv2.imshow('FAST', img2)

    # Non-maximal Suppression False
    fast.setNonmaxSuppression(0)
    kp = fast.detect(img, None)
    img3 = cv2.drawKeypoints(img, kp, img3, (255, 0, 0))
    cv2.imshow('FAST2', img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
