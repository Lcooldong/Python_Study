import numpy as np
import cv2
from random import shuffle

r = [i for i in range(256)]
b = [i for i in range(256)]
g = [i for i in range(256)]

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        shuffle(r), shuffle(b), shuffle(g)
        cv2.circle(param, (x, y), 50, (r[0], b[0], g[0]), -1)


def mouseBrush():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('paint')
    cv2.setMouseCallback('paint', onMouse, param=img)

    while True:
        cv2.imshow('paint', img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break

    cv2.destroyAllWindows()


mouseBrush()
