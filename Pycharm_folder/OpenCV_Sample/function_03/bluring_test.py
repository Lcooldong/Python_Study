import numpy as np
import cv2

def bluring_test():
    img = cv2.imread('images/8.jpg')

    kernel = np.ones((5, 5), np.float32)/25  # 커널 영역
    blur = cv2.filter2D(img, -1, kernel)     # 필터 적용

    cv2.imshow('original', img)
    cv2.imshow('blur', blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

