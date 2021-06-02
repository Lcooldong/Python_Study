import numpy as np
import cv2

def houghCirce():
    img1 = cv2.imread('images/circles.jpg')
    img2 = img1.copy()
    
    # 가우시안 필터
    img2 = cv2.GaussianBlur(img2, (3, 3), 0)
    imgray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # 1 : 원본이미지와 허프변환 카운팅 결과 이미지의 ratio
    # 20 : 원들의 중심간 최소 거리
    # param1 : 내부 Canny 함수 maxVal
    # param2 : 원으로 판단하는 허프변환 카운팅 값
    circles = cv2.HoughCircles(imgray, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=60, param2=70, minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.uint16(np.around(circles))

        # print(circles)
        # print(circles[0])
        # print(circles[0, 0:3])
        # print(circles[0, 0])
        # print(circles[0, 1])
        # print(circles[0, 2])
        # print(circles[0, 3])
        # print(circles[0, 0, 1])  # 최외각, 행, 열
        # print(circles[0, :, 1])  # 최외각, 행, 열


        for i in circles[0, :]:
            cv2.circle(img1, (i[0], i[1]), i[2], (255, 20, 255), 5)
            # print(i[0], end=" ")
            # print(i[1], end=" ")
            # print(i[2], end=" ")
            # print()
        #cv2.imshow('HoughCircles', img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('원을 찾지 못했습니다.')