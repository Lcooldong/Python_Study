# 47편
# 광학 흐름 : 비디오 프레임 사이의 이미지 객체의 가시적인 동작 패턴

# 3가지 응용
# 움직임을 통한 구조 분석
# 비디오 압축
# Video Stabilizaiton : 영상이 흔들렸거나 블러가 된 경우 깨끗한 영상으로 처리하는 기술

# 가정
# 1. 객체의 픽셀 intensity 는 연속된 프레임 속에서 변하지 않는다
# 2. 이웃한 픽셀들 역시 비슷한 움직임을 보인다.

# 추적할 포인트 결정, cv2.goodFeaturesToTrack()
# 첫번째 프레임에서, Shi-Tomasi 코너 검출, 이 점을 Lucas-Kanade Optical Flow로 반본적 점 추적
# cv2.calcOpticalFlowPyLK()의 인자로 이전 프레임, 이전 검출 포인트을 다음 프레임에 전달


import numpy as np
import cv2

termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
feature_params = dict(maxCorners=200, qualityLevel=0.01, minDistance=7, blockSize=7)
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=termination)

class App:
    def __init__(self):
        self.track_len = 10
        self.detect_interval = 5
        self.tracks = []
        self.cam = cv2.VideoCapture(0)
        self.frame_idx = 0
        self.blackscreen = False
        self.width = int(self.cam.get(3))
        self.height = int(self.cam.get(4))

    def run(self):
        while True:
            ret, frame = self.cam.read()
            if not ret:
                break

            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            vis = frame.copy()

            if self.blackscreen:
                vis = np.zeros((self.height, self.width, 3), np.uint8)

            if len(self.tracks) > 0:
                img0, img1 = self.prev_gray, frame_gray
                p0 = np.float32([tr[-1] for tr in self.tracks]).reshape(-1, 1, 2)
                p1, st, err = cv2.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)
                p0r, st, err = cv2.calcOpticalFlowPyrLK(img1, img0, p1, None, **lk_params)
                d = abs(p0-p0r).reshape(-1, 2).max(-1)
                good = d < 1
                new_tracks = []
                for tr, (x, y), good_flag in zip(self.tracks, p1.reshape(-1, 2), good):
                    if not good_flag:
                        continue

                    tr.append((x, y))
                    if len(tr) > self.track_len:
                        del tr[0]

                    new_tracks.append(tr)
                    # cv2.circle(vis, (x, y), 2, (0, 255, 0), -1)

                self.tracks = new_tracks
                cv2.polylines(vis, [np.int32(tr) for tr in self.tracks], False, (0, 255, 0))

            if self.frame_idx % self.detect_interval == 0:
                mask = np.zeros_like(frame_gray)
                mask[:] = 255
                for x, y in [np.int32(tr[-1]) for tr in self.tracks]:
                    cv2.circle(mask, (x, y), 5, 0, -1)
                p = cv2.goodFeaturesToTrack(frame_gray, mask=mask, **feature_params)
                if p is not None:
                    for x, y in np.float32(p).reshape(-1, 2):
                        self.tracks.append([(x, y)])

            self.frame_idx += 1
            self.prev_gray = frame_gray

            cv2.imshow('frame', vis)

            k = cv2.waitKey(30) & 0xFF
            if k == 27:
                break

            if k == ord('b'):
                self.blackscreen = not self.blackscreen

        self.cam.release()
        cv2.destroyAllWindows()
