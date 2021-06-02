import numpy as np
import cv2
#TODO

def drawLines(img1, img2, lines, pts1, pts2):
    r, c = img1.shape
    img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
    img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

    for r, pt1, pt2 in zip(lines, pts1, pts2):
        color = tuple(np.random.randint(0, 255, 3).tolist())
        x0, y0 = map(int, [0, -r[2]/r[1]])
        x1, y1 = map(int, [c, -(r[2] + r[0]*c)/r[1]])
        cv2.line(img1, (x0, y0), (x1, y1), color, 1)
        # cv2.circle(img1, tuple(pt1), 3, color, -1)
        cv2.circle(img2, tuple(pt2), 3, color, -1)

    return img1, img2

def epipolar():
    img1 = cv2.imread('images/ansung2.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('images/ansung1.jpg', cv2.IMREAD_GRAYSCALE)

    img1 = cv2.resize(img1, dsize=(0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
    img2 = cv2.resize(img2, dsize=(0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)

    sift = cv2.xfeatures2d.SIFT_create()

    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    good, pts1, pts2 = [], [], []

    for i, (m, n) in enumerate(matches):
        if m.distance < 0.5*n.distance:
            good.append(m)
            pts2.append(kp2[m.trainIdx].pt)
            pts1.append(kp2[m.queryIdx].pt)

    pts1 = np.float32(pts1)
    pts2 = np.float32(pts2)
    F, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_LMEDS)

    pts1 = pts1[mask.ravel() == 1]
    pts2 = pts2[mask.ravel() == 1]

    line1 = cv2.computeCorrespondEpilines(pts2.reshape(-1, 1, 2), 2, F)
    line1 = line1.reshape(-1, 3)
    img5, img6 = drawLines(img1, img2, line1, pts1, pts2)

    line2 = cv2.computeCorrespondEpilines(pts2.reshape(-1, 1, 2), 1, F)
    line2 = line2.reshape(-1, 3)
    img3, img4 = drawLines(img2, img1, line2, pts2, pts1)

    cv2.imshow('img1', img5)
    cv2.imshow('img2', img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()