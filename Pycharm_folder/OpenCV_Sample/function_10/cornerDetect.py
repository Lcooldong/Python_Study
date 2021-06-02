# 37편
# 코너 검출

import numpy as np
import cv2

def cornerDetect():
    img = cv2.imread('images/corner.jpg')
    img2 = img.copy()
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgray = np.float32(imgray)
    dst = cv2.cornerHarris(imgray, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)  # 팽창

    img2[dst > 0.01*dst.max()] = [0, 0, 255]

    cv2.imshow('Harris', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
