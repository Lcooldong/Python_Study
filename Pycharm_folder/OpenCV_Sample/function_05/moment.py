import numpy as np
import cv2

def moment():
    img = cv2.imread('images/5.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour = contours[0]
    mmt = cv2.moments(contour)

    for key, val in mmt.items():
        print('%s:\t%.5f' %(key, val))
    
    # 공간모멘트 m00, 중심모멘트 mu02, 평준화됨 중심모멘트 nu11 등등
    # 무게 중심 구하기
    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01']/mmt['m00'])

    print(cx, cy)