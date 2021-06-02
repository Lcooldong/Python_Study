import numpy as np
import cv2

def addImage(imgfile1, imgfile2):   # 사이즈 같을 때 가능
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)

    add_img1 = img1 + img2      # 255보다 커지면 257 > 257%256 -> 픽셀값 1 넘어가면 어두워짐
    add_img2 = cv2.add(img1, img2)  # 255보다 크면 255 더해져서 밝아짐

    cv2.imshow('img1 + img2', add_img1)
    cv2.imshow('add(img1, img2)', add_img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()