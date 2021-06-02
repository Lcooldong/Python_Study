import numpy as np
import cv2

CONTOURS_MATCH_1 = 1
CONTOURS_MATCH_2 = 2
CONTOURS_MATCH_3 = 3

# TODO
# 추가로 22편 참고  https://blog.naver.com/samsjang/220534805843


def contour_06():
    imgfile_list = ['images/']

    wins = map(lambda x: 'img' + str(x), range(5))
    wins = list(wins)
    imgs =[]
    contour_list = []

    i = 0
    for imgfile in imgfile_list:
        img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
        imgs.append(img)

        ret, thr = cv2.threshold(img, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        contour_list.append(contours[0])
        i += 1

    for i in range(4):
        cv2.imshow(wins[i+1], imgs[i+1])
        ret = cv2.matchShapes(contour_list[0], contour_list[i+1], CONTOURS_MATCH_1, 0.0)

        print(ret)

    cv2.waitKey(0)
    cv2.destroyAllWindows()