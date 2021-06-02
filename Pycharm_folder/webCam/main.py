import cv2 as cv

cap = cv.VideoCapture(0)

while(True):    # 카메라 유지

    ret, img_color = cap.read()
    if ret == False:
        continue

    cv.imshow('bgr', img_color)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()