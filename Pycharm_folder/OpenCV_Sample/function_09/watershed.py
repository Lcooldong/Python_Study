import numpy as np
import cv2
from scipy.ndimage import label

def watershed():
    img = cv2.imread('images/coin2.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # thresholding
    ret, thr = cv2.threshold(imgray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cv2.imshow('threshold', thr)

    # 커널, opening 노이즈 제거
    kernel = np.ones((5, 5), np.uint8)
    #opening = cv2.morphologyEx(thr, cv2.MORPH_OPEN, kernel, iterations=2)
    opening = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, kernel, iterations=1)
    cv2.imshow('kernel', opening)

    # 경계만 표시
    border = cv2.dilate(opening, kernel, iterations=2)
    border = border - cv2.erode(border, None)
    cv2.imshow('border', border)

    # 거리 변환
    dt = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    dt = ((dt-dt.min())/(dt.max()-dt.min())*255).astype(np.uint8)
    cv2.imshow('dt1', dt)
    # thresholding
    ret, dt = cv2.threshold(dt, 100, 255, cv2.THRESH_BINARY)
    # ret, dt = cv2.threshold(dt, 180, 255, cv2.THRESH_BINARY)
    cv2.imshow('dt2', dt)

    # 마커 생성 
    marker, ncc = label(dt)  # ncc 개수
    marker = marker*(255/ncc)

    marker[border == 255] = 255
    marker = marker.astype(np.int32)
    cv2.watershed(img, marker)

    marker[marker == -1] = 0
    marker = marker.astype(np.uint8)
    marker = 255 - marker

    marker[marker != 255] = 0
    marker = cv2.dilate(marker, None)
    # 색칠
    img[marker == 255] = (0, 0, 255)

    cv2.imshow('watershed', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
