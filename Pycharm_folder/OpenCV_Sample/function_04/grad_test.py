# sobel 8u   검은색 -> 흰색 경계 o  흰색 -> 검은색 경계 x (음수-> 0)
# 64F-> 8u  양쪽 다 표시
# 미분 x 변화에 대해서 나타냄 y축이 생김

import numpy as np
import cv2
import matplotlib.pyplot as plt

def grad_test():

    img = cv2.imread('images/box.jpg', cv2.IMREAD_GRAYSCALE)

    sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)  # 8U

    tmp = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)  # 64F
    sobel64f = np.absolute(tmp)
    sobelx8u2 = np.uint8(sobel64f)  # 64F -> 8U

    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')      # 1행 3열/ 1,2,3
    plt.title('original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
    plt.title('Sobel 8U'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 3), plt.imshow(sobelx8u2, cmap='gray')
    plt.title('Sobel 64F'), plt.xticks([]), plt.yticks([])

    plt.show()