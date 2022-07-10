import matplotlib.pyplot as plt
import numpy as np


f = 1           #Freq.
f_s = 100        #smapling Rate, or number of Measurements per second
sec = 1

Amp = 1
offset = 1

t = np.linspace(0, sec, sec * f_s, endpoint=False)  # 0 ~ sec
x = Amp * np.sin(f * 2 * np.pi * t) + offset  # 2π x f x t


fig, ax = plt.subplots()
ax.plot(t, x)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Signal amplitude')


plt.show()


if __name__ == '__main__':
    pass


