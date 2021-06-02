import numpy as np
import cv2

def BRIEF():
    img = cv2.imread('images/corner.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = None

    star = cv2.xfeatures2d.StarDetector_create()

    brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

    kp1 = star.detect(imgray, None)
    kp2, des = brief.compute(img, kp1)

    # input image, keypoint, output image, color, flags=
    img2 = cv2.drawKeypoints(img, kp1, img2, (255, 0, 0))

    cv2.imshow('BRIEF', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()