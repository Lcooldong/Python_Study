# 28편
# 푸리에 변환(Fourier Transform)
# 주기함수는 주파수가 다른 삼각함수의 합으로 표현 가능
# 시간 영역(time domain) -> 주파수 영역(frequency domain)  : 가로축
# 픽셀 값의 변화가 얼마나 빠른가, 픽셀값 변화가 크면 경계부분에서 노이즈 발생
# numpy 사용


import numpy as np
import cv2
import matplotlib.pyplot as plt

def fourier_01():
    img = cv2.imread('images/11.jpg', cv2.IMREAD_GRAYSCALE)

    # 2D 이산 푸리에 변환(2D Discrete Fourier Transform; 2D-DFT)
    f = np.fft.fft2(img)   # 고속 푸리에 변환(Fast Fourier Transform; FFT)

    # fftshift함수 : 주파수가 0인 부분을 정중앙에 위치시키고, 재배열해줌[012-3-2-1]->[-3-2-1012]
    fshift = np.fft.fftshift(f)
    m_spectrum = 20*np.log(np.abs(fshift))

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('input image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(m_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

    plt.show()

