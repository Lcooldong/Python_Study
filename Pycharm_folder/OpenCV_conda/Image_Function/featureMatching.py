# 43편
# 전수조사 방법 (Brute-Force, BF 매칭)
# 디스크립터 거리 계산 방법을 통해 측정
# SIFT, SURF cv2.NORM_L2
# ORB, BRIEF cv2.NORM_HAMMING
# crossCheck True 면 가장 일치하는 부분만 리턴

import numpy as np
import cv2

def featureMatching():
    # dst1 = cv2.imread('images/book1.jpg', cv2.IMREAD_GRAYSCALE)
    # dst2 = cv2.imread('images/book2.jpg', cv2.IMREAD_GRAYSCALE)
    dst1 = cv2.imread('images/m1.jpg', cv2.IMREAD_GRAYSCALE)
    dst2 = cv2.imread('images/m2.jpg', cv2.IMREAD_GRAYSCALE)
    res = None

    img1 = cv2.resize(dst1, dsize=(0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
    img2 = cv2.resize(dst2, dsize=(0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)

    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)    # kp 특징점
    kp2, des2 = orb.detectAndCompute(img2, None)    # descriptor 기술자

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x: x.distance)
    res = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], res, flags=0)

    cv2.imshow('Feature Matching', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()