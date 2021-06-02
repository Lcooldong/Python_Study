import numpy as np
import cv2


def backSubtraction_02():
    cap = cv2.VideoCapture(0)
    cap.set(3, 480)
    cap.set(4, 320)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

    while True:
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

        cv2.imshow('mask', fgmask)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()