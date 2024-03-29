import numpy as np
import cv2

def convex_03():
    img = cv2.imread('images/convexhull.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rows, cols = img.shape[:2]

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[14]
    
    # 외접원(리턴값 : 중심좌표, 반지름)
    (x, y), r = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    r = int(r)
    
    cv2.circle(img, center, r, (255, 0, 0), 3)
    
    # 타원
    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(img, ellipse, (0, 255, 0), 3)
    
    # 직선(직선위 점 x,y   | 단위벡터 vx, vy)
    # DIST_L1 = r, DIST_L2 = r^2/2 등등
    [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
    ly = int((-x*vy/vx) + y)
    ry = int(((cols-x)*vy/vx) + y)

    cv2.line(img, (cols-1, ry), (0, ly), (0, 0, 255), 2)

    cv2.imshow('fitting', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()