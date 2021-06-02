# 27편 
# 사각형 그리면 hsv 값에 따라 보여짐
# 확률적으로 비슷한 픽셀을 구함
# 구한 픽셀을 흰색에 가깝게 해주고, 동일한 크기의 이미지 생성

import numpy as np
import cv2

ix, iy = -1, -1
mode = False
img1, img2 = None, None

def onMouse(event, x, y, flag, param):
    global ix, iy, mode, img1, img2

    if event == cv2.EVENT_LBUTTONDOWN:
        mode = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if mode:
            img1 = img2.copy()
            cv2.rectangle(img1, (ix, iy), (x, y), (0, 0, 255), 2)
            cv2.imshow('original', img1)

    elif event == cv2.EVENT_LBUTTONUP:
        mode = False
        if ix >= x or iy >= y:
            return

        cv2.rectangle(img1, (ix, iy), (x, y), (0, 0, 255), 2)
        roi = img1[iy: y, ix:x]
        backProjection(img2, roi)

def backProjection(img, roi):
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    hsvt = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    roihist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
    dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)

    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    cv2.filter2D(dst, -1, disc, dst)

    ret, thr = cv2.threshold(dst, 0, 255, 0)
    thr = cv2.merge((thr, thr, thr))
    res = cv2.bitwise_and(img, thr)

    # filter
    kernel = np.ones((1, 1), np.uint8)
    # opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel, iterations=1)

    # cv2.imshow('backprojection', res)
    cv2.imshow('backprojection', closing)


def hist_colorPick():
    global img1, img2

    img1 = cv2.imread('images/12.jpg')
    img2 = img1.copy()

    cv2.namedWindow('original'), cv2.namedWindow('backprojection')
    cv2.setMouseCallback('original', onMouse, param=None)

    cv2.imshow('backprojection', img2)

    while True:
        cv2.imshow('original', img1)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()