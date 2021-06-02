import numpy as np

print(np.random.rand(2, 3))
print(np.random.randn(3, 4))  # normal distribution 정규분포
print(np.random.randint(2, 51, size=(2, 5)))
np.random.seed(100)    # 시드 넘버에 고정
print(np.random.randn(2, 4))    # 고정됨
print(np.random.choice(100, size=(4, 5)))   # np.array

x = np.array([1,2,3,4,1.5,2.3, 4.7])
print(np.random.choice(x, size= (2,2)))