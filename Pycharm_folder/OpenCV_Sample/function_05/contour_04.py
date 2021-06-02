# 21편 Convexity Defects

import numpy as np
import cv2

def contour_04():
    img = cv2.imread('images/star.png')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 경계
    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cnt = contours[1]
    
    # 볼록체
    hull = cv2.convexHull(cnt)
    cv2.drawContours(img, [hull], 0, (0, 0, 255), 2)

    # hull_index = hull[0:2]
    # cv2.drawContours(img, [hull_index], 0, (0, 0, 255), 5)

    # contour와 hull이 만나는 꼭지점의 contour 인덱스 리턴
    hull = cv2.convexHull(cnt, returnPoints=False)
    # 시작 인덱스, 그 다음으로 연결되는 인덱스, 가장 멀리 있는 contour 인덱스, 가장 먼점까지 거리 근사치
    defects = cv2.convexityDefects(cnt, hull)

    for i in range(defects.shape[0]):
        sp, ep, fp, dist = defects[i, 0]
        start = tuple(cnt[sp][0])
        end = tuple(cnt[ep][0])
        farthest = tuple(cnt[fp][0])

        cv2.circle(img, farthest, 5, (0, 255, 0), -1)
        cv2.circle(img, start, 5, (255, 0, 0), -1)
        cv2.circle(img, end, 3, (255, 0, 255), -1)
        cv2.imshow(f'defect{i+1}', img)

    cv2.imshow('defects', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()