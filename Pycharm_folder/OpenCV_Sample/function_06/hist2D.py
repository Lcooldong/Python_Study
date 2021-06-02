import numpy as np
import cv2

hscale = 10

def onMouse(x):
    global hscale
    hscale = x


def HSVmap():
    hsvmap = np.zeros((180, 256, 3), np.uint8)
    h, s = np.indices(hsvmap.shape[:2])

    hsvmap[:, :, 0] = h
    hsvmap[:, :, 1] = s
    hsvmap[:, :, 2] = 255

    hsvmap = cv2.cvtColor(hsvmap, cv2.COLOR_HSV2BGR)

    return hsvmap

def hist2D():
    img = cv2.imread('images/flower.jpg')

    hsvmap = HSVmap()

    cv2.namedWindow('hist2D', 0)
    cv2.createTrackbar('scale', 'hist2D', hscale, 32, onMouse)

    while True:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #[0,1] 2개 입력 채널값  | [180, 256] hue, saturation BIN 개수 |  [0, 180, 0, 256] hue, saturation 범위
        hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

        # 처음 매개변수가 min 보다 작으면 min(여기선 0), max(1)보다 크면 max로 numpy배열 리턴
        hist = np.clip(hist*0.005*hscale, 0, 1)
        hist = hsvmap*hist[:, :, np.newaxis]/255.0

        img2 = np.hstack(( hsv, img))

        cv2.imshow('hist2D', hist)
        cv2.imshow('hsv&org', img2)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()