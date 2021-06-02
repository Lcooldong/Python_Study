#approxPolyDP(대상곡선, 정확도매개변수, 폐,개곡선유무)

import numpy as np
import cv2

def contour_03():
    img = cv2.imread('images/box_b.jpg')
    img1 = img.copy()
    img2 = img.copy()
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    cv2.drawContours(img, [cnt], 0, (0, 0, 255), 2)

    # 근사 정확도를 위해 contour 에서 근사 contour 까지 최대 거리
    epsilon1 = 0.01*cv2.arcLength(cnt, True)  # 짧으면 근처로 연결
    epsilon2 = 0.1*cv2.arcLength(cnt, True)   # 멀면 먼쪽에 연결
    
    # True 폐곡선, False 개곡선
    approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
    approx2 = cv2.approxPolyDP(cnt, epsilon2, True)

    cv2.drawContours(img1, [approx1], 0, (0, 255, 0), 3)
    cv2.drawContours(img2, [approx2], 0, (0, 255, 0), 3)

    cv2.imshow('contour', img)
    cv2.imshow('Approx1', img1)
    cv2.imshow('Approx2', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


