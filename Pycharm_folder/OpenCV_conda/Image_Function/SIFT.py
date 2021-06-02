# TODO

import numpy as np
import cv2

def SIFT():
    img = cv2.imread('images/butterfly.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2, img3 = None, None

    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(imgray, None)

    img2 = cv2.drawKeypoints(imgray, kp, img2)
    img3 = cv2.drawKeypoints(imgray, kp, img3, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow('SIFT1', img2)
    cv2.imshow('SIFT2', img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
