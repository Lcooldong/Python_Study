import numpy as np
import cv2

def featureMatching_SIFT():
    dst1 = cv2.imread('images/book1.jpg', cv2.IMREAD_GRAYSCALE)
    dst2 = cv2.imread('images/book2.jpg', cv2.IMREAD_GRAYSCALE)
    res = None

    img1 = cv2.resize(dst1, dsize=(0, 0), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    img2 = cv2.resize(dst2, dsize=(0, 0), fx=1, fy=1, interpolation=cv2.INTER_LINEAR)

    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)  # kp 특징점
    kp2, des2 = sift.detectAndCompute(img2, None)  # descriptor 기술자

    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x: x.distance)
    res = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], res, flags=0)

    cv2.imshow('Feature Matching', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()