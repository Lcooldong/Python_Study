import numpy as np
import cv2
import pytesseract

def showVideo():
    try:
        print('카메라를 구동합니다.')
        cap = cv2.VideoCapture(0)
    except:
        print('카메라 구동 실패')
        return
    
    # cap.set(3, 480)
    # cap.set(4, 320)
    cap.set(3, 400)
    cap.set(4, 300)

    while True:
        ret, frame = cap.read()
        
        if not ret:
            print('비디오 읽기 오류')
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(gray, 75, 200)
        adpt_thes = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)   # 뒤 숫자 두께(홀수), 밀도


        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([90, 100, 100])  # h색상 s채도 v명도
        upper_blue = np.array([170, 240, 240])

        lower_green = np.array([30, 100, 100])
        upper_green = np.array([70, 240, 240])

        lower_red = np.array([-10, 100, 100])
        upper_red = np.array([10, 240, 240])

        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        BLUE = cv2.bitwise_and(frame, frame, mask=mask_blue)
        GREEN = cv2.bitwise_and(frame, frame, mask=mask_green)
        RED = cv2.bitwise_and(frame, frame, mask=mask_red)



        cv2.imshow('original', frame)
        cv2.imshow('gray', gray)
        cv2.imshow('hsv', hsv)
        cv2.imshow('Canny edge', edge)
        cv2.imshow('thes', adpt_thes)
        cv2.imshow('BLUE', BLUE)
        cv2.imshow('GREEN', GREEN)
        cv2.imshow('RED', RED)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()