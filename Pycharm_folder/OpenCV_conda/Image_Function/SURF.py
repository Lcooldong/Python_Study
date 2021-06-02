# TODO

import numpy as np
import cv2

def SURF():
    img = cv2.imread('images/butterfly.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2, img3 = None, None

    surf = cv2.xfeatures2d.SURF_create()
    surf.setHessianThreshold(10000)

    kp, des = surf.detectAndCompute(img, None)
    img2 = cv2.drawKeypoints(imgray, kp, img2, (255, 0, 0), 4)

    cv2.imshow('SURF', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()