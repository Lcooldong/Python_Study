#  가우시안 피라미드
#  downsampling 다운샘플링 : 해상도 낮추기

import numpy as np
import cv2

def pyramid_down():
    img = cv2.imread('images/10.jpg', cv2.IMREAD_GRAYSCALE)
    tmp = img.copy()

    win_titles = ['org', 'level1', 'level2', 'level3']
    g_down = []     # 해상도 낮추기 배열
    g_down.append(tmp)  # 배열에 사진 넣기 [0]

    for i in range(3):
        tmp1 = cv2.pyrDown(tmp)     # 다운샘플링 이미지 생성
        g_down.append(tmp1)         # 배열에 추가  [1] [2] [3]
        tmp = tmp1                  # 다운 샘플링을 저장 반복

    for i in range(4):
        cv2.imshow(win_titles[i], g_down[i])

    cv2.waitKey(0)
    cv2.destroyAllWindows()