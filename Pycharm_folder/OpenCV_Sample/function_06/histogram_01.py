# 픽셀 분포도 (어두운 픽셀, 밝은 픽셀)


import numpy as np
import cv2
import matplotlib.pyplot as plt

def histogram_01():
    img1 = cv2.imread('images/5.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('images/5.jpg')
    
    # OpenCV 함수 히스토그램(가장 성능 좋음)
    hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])

    # numpy 히스토그램
    hist2, bins = np.histogram(img1.ravel(), 256, [0, 256])

    # 1-D 히스토그램의 경우,  numpy 가 빠름
    hist3 = np.bincount(img1.ravel(), minlength=256)

    # matplotlib 히스토그램
    plt.hist(img1.ravel(), 256, [0, 256])
    
    # 컬러 이미지 히스토그램
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist = cv2.calcHist([img2], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

#    plt.plot(hist1)
#    plt.plot(hist2)
#     plt.plot(hist3)

    # cv2.imshow('3.jpg', img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    plt.show()