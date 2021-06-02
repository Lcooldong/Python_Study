# 39편
# SURF(Speeded-Up Robust Features)
# 박스필터(Box Filter)로 LoG를 근사하는 방법
# 뷰포인트, 조명이 바뀌면 검출 제대로 못함
# ▲ 두 이미지 중 한장을 블러, 회전은 동일하게 검출, 바뀌면 다르게 검출

import numpy as np
import cv2

def SUTF():
    img = cv2.imread('images/butterfly.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2, img3 = None, None

    # 객체 생성
    surf = cv2.SIFT_create()    # 고 버전은 없음
    # surf.setHessianThreshold(10000) surf 없어서 작동 x

    # surf.setUpright(True) 사용 x


    # 키 포인트 검출
    kp, des = surf.detectAndCompute(img, None)
    # 키 포인트 그리기
    img2 = cv2.drawKeypoints(imgray, kp, img2, (0, 0, 255), 4)
    
    cv2.imshow('SURF', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()