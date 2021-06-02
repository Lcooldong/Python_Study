import cv2
import numpy as np

def drawing():
    img = np.zeros((512, 512, 3), np.uint8)

    cv2.line(img, (0, 0), (511, 511), (255, 0, 255), 4)   # 시작, 끝, 색, 두께
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)    # 좌측상단, 우측 하단, 색, 두께
    cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)     # 원중심, 반지름, 색, 채움
    cv2.ellipse(img, (256, 256), (100, 50), 0, 30, 330, (255, 0, 0), -1)
    # 타원중심, (장축(1/2), 단축(1/2)), (기울기, 시작각도, 끝각도) , 색, 채움

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)

    cv2.imshow('drawing', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()