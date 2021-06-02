import cv2

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