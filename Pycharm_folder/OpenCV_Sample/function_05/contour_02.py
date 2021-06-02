import numpy as np
import cv2

def contour_02():
    img = cv2.imread('images/goldenship.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[121]  # index
    area = cv2.contourArea(cnt)  # contour 면적
    perimeter = cv2.arcLength(cnt, True)    # contour 길이

    cv2.drawContours(img, [cnt], 0, (0, 0, 255), 2)

    print('contour 면적', area)
    print('contour 길이', perimeter)

    cv2.imshow('contour', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()