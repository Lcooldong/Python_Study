# 37편
# Shi-Tomasi 코너 검출

import numpy as np
import cv2

def shito():
    img = cv2.imread('images/corner2.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # grayscale, 검출할 코더 개수, 코너로 판단할 문턱값(코너 검출품질), 검출할 코너 사이 최소거리(이 거리 이내 무시)
    corners = cv2.goodFeaturesToTrack(imgray, 200, 0.1, 25)
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 5, (255, 0, 255), -1)

    cv2.imshow('shito', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()