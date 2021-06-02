# 31 편
# template 찾아내기 
# 0~1 사이의 thr 경계값을 줘서 같은 것을 찾아냄
# thr 값이 높을수록 보다 유사하게 찾아냄

import numpy as np
import cv2

def tmpMatching_02(thr):
    img = cv2.imread('images/wind.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/rabbit3.jpg', cv2.IMREAD_GRAYSCALE)
    # template = cv2.imread('images/squirrel.jpg', cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]  # [시작인덱스:끝인덱스:인덱스증가폭] 역순

    res = cv2.matchTemplate(imgray, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= thr)

    # zip 같은 위치끼리 묶어줌  zip([0,1], [4,5]) -> [(0,4), (1,5)]
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 2)

    cv2.imshow('res', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()