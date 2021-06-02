# down(해상도 낮춤, 사이즈 작아짐) -> up (해상도 높힘)
# 높은 해상도로 바뀌나 품질이 높아지는 건 아님

import numpy as np
import cv2

def pyramid_up():

    img = cv2.imread('images/10.jpg', cv2.IMREAD_GRAYSCALE)
    tmp = img.copy()

    win_titles = ['org', 'level1', 'level2', 'level3']  # 사이즈
    g_down = []     # 다운샘플링 배열
    g_up = []       # 업샘플링 배열

    g_down.append(tmp)      # original을  down [0]

    for i in range(3):
        tmp1 = cv2.pyrDown(tmp)
        g_down.append(tmp1)    # 다운 샘플링한 것을  down [1] [2] [3]
        tmp = tmp1

    cv2.imshow('level3', tmp)  # down [3] 출력  upsampling x,  level3


    for i in range(3):
        tmp = g_down[i+1]   # down [1], [2] , [3]
        tmp1 = cv2.pyrUp(tmp)   # upsampling -> bluring  한 느낌
        g_up.append(tmp1)   # down[1]-> up[0], down[2]-> up[1], down[3]->up[2]

    for i in range(3):
        cv2.imshow(win_titles[i], g_up[i])  # org, level1, level2 , up[0][1][2]

    cv2.waitKey(0)
    cv2.destroyAllWindows()