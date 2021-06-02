import numpy as np
import cv2

def transform_affine():
    img = cv2.imread('images/4.jpg')
    h, w = img.shape[:2]    # height, width [시작:끝]  0->행(높이), 1->열(폭)

    print(h)
    print(img.shape[0])
    print(w)
    print(img.shape[1])

    pts1 = np.float32([[50, 50], [200, 50], [20, 200]])
    pts2 = np.float32([[10, 1000], [200, 50], [100, 250]])

    M = cv2.getAffineTransform(pts1, pts2)

    img2 = cv2.warpAffine(img, M, (w, h))

    cv2.imshow('original', img)
    cv2.imshow('Affine-Transform', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()