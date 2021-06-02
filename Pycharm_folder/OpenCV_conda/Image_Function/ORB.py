# 42편
# ORB (Oriented FAST and Rotated BRIEF)
# 키포인트 찾기 위해 FAST 사용
# 최상위 n 개 코너 검출 Harris 코너 검출 방법
# 크기 불변 이미지 특성 추출을 위해 다양한 스케일의 피라미드 적용
# 회전 불변 특성을 추춣기 위해 BRIEF descriptor 적용

import numpy as np
import cv2

def ORB():
    img = cv2.imread('images/book.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = None

    orb = cv2.ORB_create()
    kp, des = orb.detectAndCompute(img, None)

    img2 = cv2.drawKeypoints(img, kp, img2, (255, 0, 0), flags=0)

    cv2.imshow('ORB', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()