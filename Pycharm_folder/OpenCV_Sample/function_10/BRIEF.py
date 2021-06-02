import numpy as np
import cv2

def BRIEF():
    img = cv2.imread('images/corner.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = None
