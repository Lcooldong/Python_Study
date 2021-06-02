import numpy as np
import cv2
import matplotlib.pyplot as plt

def showImage():
    imgfile = 'images/1.png'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)  # object

    #b, g, r = cv2.split(img)   # 성능이 numpy index 보다 안좋음

    #img[:, :, 0] = 0
    #img[:, :, 1] = 0
    #img[:, :, 2] = 0

    # numpy indexing
    b = img[:, :, 0]    # blue channel
    g = img[:, :, 1]    # green channel
    r = img[:, :, 2]    # red channel
    merged_img = cv2.merge((b, g, r))

    # B = img.item(340, 200, 0)
    # G = img.item(340, 200, 1)
    # R = img.item(340, 200, 2)
    # px = img[340, 200]  # 가로, 세로 위치의 픽셀 값
    # img.itemset((340, 200, 0), 100)  # 가로세로위치 Blue 값 변경


#    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
#    img = cv2.imread(imgfile, cv2.IMREAD_UNCHANGED)


    while True:
        cv2.namedWindow('Picture', cv2.WINDOW_NORMAL)   # 이름 입력, 사이즈 변경가능
        # cv2.imshow('Picture', img)      # 화면 출력
        cv2.imshow('Picture', merged_img)      # 화면 출력

        # subimg = img[300:400, 350:750]  # 이미지 자르기
        # cv2.imshow('cutting', subimg)   # 자른 이미지 출력
        # img[300:400, 0:400] = subimg    # 이 위치에 넣기
        # cv2.imshow('modified',img)      # 넣은 사진 출력

        k = cv2.waitKey(0) & 0xFF       # 지정된 시간동안 키보드 입력 기다림 0-> 누를때까지 기다림/ 0xFF 64비트


        # plt.imshow(img, cmap='gray', interpolation='bicubic')
        # plt.xticks([])
        # plt.yticks([])
        # plt.title('hello')
        # plt.show()

        if k == 27:                     # ESC
            cv2.destroyAllWindows()     # 모든 윈도우 제거
            break
        elif k == ord('c'):
            cv2.imwrite('images/1_copy.png', img)
            cv2.destroyAllWindows()
            break