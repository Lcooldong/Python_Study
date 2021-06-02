# 확률적 허프변환
# 직선위 점과 극좌표 변화를 통한 직선 검출
# hough_02(극좌표카운팅 개수, 라인 최소 길이, 라인 최대 간격)

import numpy as np
import cv2

def hough_02(thr, minLineLength, maxLineGap):
    img = cv2.imread('images/sudoku.jpeg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(imgray, 50, 150, apertureSize=3)
    
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, thr, minLineLength, maxLineGap)
    
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    cv2.imshow('res', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()