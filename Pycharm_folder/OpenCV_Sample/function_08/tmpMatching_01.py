# 30편
# 템플릿 매칭
# 어떤 이미지에서 부분 이미지를 검색하고 찾는 방법
# 결과 이미지 사이즈  W-w+1, H-h+1

import numpy as np
import cv2
from matplotlib import pyplot as plt

def tmpMatching_01():
    # 타겟 이미지
    img1 = cv2.imread('images/12.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = img1.copy()
    
    # 템플릿 이미지, width, height
    template = cv2.imread('images/12_face.jpg', cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    
    # 결과출력 방법 이름 리스트
    methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED',
               'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        img1 = img2.copy()
        method = eval(meth)

        try:
            # 이미지에서 특정 방식을 이용하여 템플릿을 찾은 결과->
            res = cv2.matchTemplate(img1, template, method)
            # 주어진 행렬의 최솟값, 최댓값을 찾는 함수 (val 값, loc 위치좌표)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        except:
            print('오류', meth)
            continue

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc  # 결과값의 최솟값
        else:
            top_left = max_loc  # 결과값의 최대값

        bottom_right = (top_left[0]+w, top_left[1]+h)
        cv2.rectangle(img1, top_left, bottom_right, 255, 2)

        plt.subplot(121), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])

        plt.subplot(122), plt.imshow(img1, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)

        plt.show()