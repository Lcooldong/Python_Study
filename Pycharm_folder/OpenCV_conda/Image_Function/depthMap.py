import numpy as np
import cv2
import matplotlib.pyplot as plt

#TODO
def depthMap():
    imgL = cv2.imread('images/imgL.jpg', 0)
    imgR = cv2.imread('images/imgR.jpg', 0)

    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(imgL, imgR)

    plt.xticks([]), plt.yticks([])
    plt.imshow(disparity, 'gray')
    plt.show()