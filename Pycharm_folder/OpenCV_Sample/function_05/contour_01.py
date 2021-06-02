# 같은 값을 가진 곳을 연결한 선(등고선, 등압선) -> 색의 강도
# 대상 흰색, 배경 검은색과 비슷 (바이너리 이미지)
# cv2.CHAIN_APPROX_SIMPLE : 직선 contour 구할 때 양쪽 끝만 구함
# cv2.CHAIN_APPROX_NONE : 모든 점을 구해서 메모리 소모 심함


import numpy as np
import cv2

def contour_01():
    img = cv2.imread('images/goldenship.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 흑백이미지로 변경

    ret, thr = cv2.threshold(imgray, 127, 255, 0)   # 문턱으로 바이너리화
    contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 경계

    # img 대상, 그릴 contour, -1은 모든 contour (index임),  색 ,1은 선의 두께
    cv2.drawContours(img, contours, -1, (0, 0, 255), 1)  # 경계를 빨간색으로 그리기
    cv2.imshow('thresh', thr)
    cv2.imshow('contour', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

