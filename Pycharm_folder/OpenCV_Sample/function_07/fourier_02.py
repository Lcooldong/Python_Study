# 28편
# OpenCV 이용 푸리에 변환

import numpy as np
import cv2
import matplotlib.pyplot as plt

def fourier_02():
    img = cv2.imread('images/11.jpg', cv2.IMREAD_GRAYSCALE)
    
    # float32로 랩핑, dft() 함수는 복소수 형태로 리턴해서
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    # ▼ 백터의 x성분, y성분 입력 (2차원 벡터의 크기 계산)
    m_spectrum = 20*np.log(cv2.magnitude(dft_shift[:, :, 0], dft[:, :, 1]))
    
    # 1 x 2 subplot 의 첫번째
    plt.subplot(121), plt.imshow(img, cmap='gray')  # cmap(color map)
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])

    # 1 x 2 subplot 의 두번째
    plt.subplot(122), plt.imshow(m_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

    plt.show()
