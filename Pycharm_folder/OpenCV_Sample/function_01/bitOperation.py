import numpy as np
import cv2

def bitOperation(hpos, vpos):
    img1 = cv2.imread('images/6.jpg')
    img2 = cv2.imread('images/2.jpg')

    #사진의 , 로고 넣을 영역 설정
    rows, cols, channels = img2.shape
    roi =img1[vpos:rows+vpos, hpos:cols+hpos]   # roi(region of images)

    # 로고의 마스크, 역마스크
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)   # 흑백으로
    ret, mask = cv2.threshold(img2gray, 160, 255, cv2.THRESH_BINARY)  # 마스크 범위 설정
    mask_inv = cv2.bitwise_not(mask)    # 역 마스크
    
    # 로고 해당부분 검은색
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    
    # 로고 부분만 추출
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
    
    # 합치기
    dst = cv2.add(img1_bg, img2_fg)
    img1[vpos:rows+vpos, hpos:cols+hpos] = dst

    cv2.imshow('result', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


