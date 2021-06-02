# 50편
# 체스판 인식
# 15회 촬영 후 배열 저장

import numpy as np
import cv2

row = 10
col = 14

def chess_estimate():
    termination = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    objp = np.zeros((row*col, 3), np.float32)
    objp[:, :2] = np.mgrid[0:row, 0:col].T.reshape(-1, 2)

    objpoints = []
    imgpoints = []

    cap = cv2.VideoCapture(0)
    count = 0
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(gray, (row, col), None)

        if ret:
            objpoints.append(objp)
            cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), termination)
            imgpoints.append(corners)

            cv2.drawChessboardCorners(frame, (row, col), corners, ret)
            count += 1
            print('[%d]', count)

        cv2.imshow('img', frame)

        k = cv2.waitKey(0)
        if k == 27:
            break

        if count > 15:
            break

    # cap.release()
    cv2.destroyAllWindows()
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    np.savez('images/calib2.npz', ret=ret, mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)
    print('카메라 캘리브레이션 데이터를 저장했습니다.')

