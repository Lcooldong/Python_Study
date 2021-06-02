import numpy as np
import cv2
import matplotlib.pyplot as plt
from random import shuffle


def showImage():
    imgfile = 'image/1.png'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR) # object
#    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
#    img = cv2.imread(imgfile, cv2.IMREAD_UNCHANGED)

    while True:
        cv2.namedWindow('Picture', cv2.WINDOW_NORMAL)   # 사이즈 변경가능
        cv2.imshow('Picture', img)      # 화면 출력
        k = cv2.waitKey(0) & 0xFF       # 지정된 시간동안 키보드 입력 기다림 0-> 누를때까지 기다림/ 0xFF 64비트

        # plt.imshow(img, cmap='gray', interpolation='bicubic')
        # plt.xticks([])
        # plt.yticks([])
        # plt.title('hello')
        # plt.show()

        if k == 27:                     # ESC
            cv2.destroyAllWindows()     # 모든 윈도우 제거
            break
        elif k == ord('c'):
            cv2.imwrite('image/1_copy.png', img)
            cv2.destroyAllWindows()
            break


def showVideo():
    try:
        print('카메라를 구동합니다.')
        cap = cv2.VideoCapture(0)
    except:
        print('카메라 구동 실패')
        return

    cap.set(3, 480)
    cap.set(4, 320)

    while True:
        ret, frame = cap.read()  # 한 프레임씩 읽기

        if not ret:
            print('비디오 읽기 오류')
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('video', gray)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


def writeVideo():
    try:
        print('카메라를 구동합니다.')
        cap = cv2.VideoCapture(0)   # 딜레이 0
    except:
        print('카메라 구동 실패')
        return

    fps = 20.0
    width = int(cap.get(3))  # 폭
    height = int(cap.get(4))  # 높이
    fcc = cv2.VideoWriter_fourcc(*'DIVX')

    out = cv2.VideoWriter('mycam.mp4', fcc, fps, (width, height))

    while True:
        ret, frame = cap.read()  # 한 프레임씩 읽기

        if not ret:
            print('비디오 읽기 오류')
            break

        # frame = cv2.flip(frame, 0)    #  뒤집기
        cv2.imshow('video', frame)
        out.write(frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            print('녹화를 종료합니다.')
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

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





#showImage()
#showVideo()
#writeVideo()
#drawing()