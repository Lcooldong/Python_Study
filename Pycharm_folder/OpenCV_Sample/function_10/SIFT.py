# 38편
# 큰 이미지에서 코더 검출(작은 필터)

# 1: Scale-space Extrema Detection (스케일-공간 극값 검출)
# ▲ 서로다른 필터를 적용한 가우시안 피라미드 이미지 차 (DoG) ,  (라플라시안 + 가우시안 :LoG는 느림), 극값:Potential Keypoint
# 2: Keypoint Localization (키포인트 지역화), 테일러 전개
# 3: Orientation Assignment (방향 할당하기), 방향성-불변, 확대회전에도 안변함
# 4: Keypoint Descriptor (키포인트 디스크립터 계산하기), 이미지 히스토그램 활용, 특징 보존
# 5: Keypoint Matching (키포인트 매칭), 두 개의 이미지에서 키포인트 매칭-> 동일한 이미지 추출



import numpy as np
import cv2

def SIFT():
    img = cv2.imread('images/butterfly.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2, img3 = None, None

    # sift = cv2.xfeatures2d.SIFT_create()   # 4.40 버전이후로 메인 모듈에 포함됨
    sift = cv2.SIFT_create()
    # 키포인트 계산 추출, 일부분만 검출하려면  Mask= 사용
    kp = sift.detect(imgray, None)
    
    # 키포인트 표시, flags 키포인트 크기, 방향성
    img2 = cv2.drawKeypoints(imgray, kp, img2)
    img3 = cv2.drawKeypoints(imgray, kp, img3, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow('SIFT1', img2)
    cv2.imshow('SIFT2', img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()