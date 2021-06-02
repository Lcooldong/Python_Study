# 28편
# 푸리에 변환 이미지 필터
# 낮은 영역 통과 LPF(Low Pass Filter), 높은 영역 통과 HPF(High Pass Filter)
# 색의 변화가 큰 부분을 검출
# 정중앙을 0으로 두는데 이 0부분을 넓히면(60x60) 낮은 주파수 부분은 제거
# ishift 역쉬프트 : 가운데 0이던거 원래대로


import numpy as np
import cv2
import matplotlib.pyplot as plt

def fourier_03():
    img = cv2.imread('images/12.jpg', cv2.IMREAD_GRAYSCALE)

    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)

    # 행, 열  -> 행, 열 절반 [01234],[56789] -> [01]
    rows, cols = img.shape
    crow, ccol = int(rows/2), int(cols/2)

    # 이미지 정중앙(60x60 영역) 값을 모두 0으로
    fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
    # 역 shift 함수 재배열된 주파수를 원래대로 되돌림
    f_ishift = np.fft.ifftshift(fshift)
    # 역 푸리에 변환을 하여 원래 이미지 영역으로 전환
    img_back = np.fft.ifft2(f_ishift)
    # 모든 값 절대값(컬러맵 jet)
    img_back = np.abs(img_back)

    # 원본 이미지 gray
    plt.subplot(131), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    # 되돌린 이미지 gray
    plt.subplot(132), plt.imshow(img_back, cmap='gray')
    plt.title('After HPF'), plt.xticks([]), plt.yticks([])
    
    # 되돌린 이미지
    plt.subplot(133), plt.imshow(img_back)
    plt.title('Result in JET'), plt.xticks([]), plt.yticks([])

    plt.show()
