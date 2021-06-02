import numpy as np
import cv2

def histogram_02():
    img = cv2.imread('images/11.jpg', cv2.IMREAD_GRAYSCALE)

    hist, bins = np.histogram(img.ravel(), 256, [0, 256])
    cdf = hist.cumsum()

    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m-cdf_m.min()*255/(cdf_m.max()-cdf_m.min()))
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    img2 = cdf[img]

    cv2.imshow('Histogram Equalizati', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()