import numpy as np

#if __name__ == '__main__':

x = np.array([1, 2, 3, 4])
y = np.array([[1, 3, 5],[2, 4, 6]])

print(x)
print(y)

print(type(y))

print(np.arange(10))
print(np.arange(1, 10))
print(np.arange(1, 10, 2))

print(np.ones((2, 5)))   # 1로 초기화
print(np.ones((2, 4, 5)))
print(np.zeros((5, 2, 4, 3)))  # 0으로 초기화 (1차원 추가, z축 ,행(y),열(x))

print(np.empty((2, 3)))
print(np.full((2, 3), 5))

print(np.eye(3)) # 대각선 1 정사각형 단위행렬
print(np.linspace(1, 10, 3))  # 1~10 3등분
print(np.linspace(1, 10, 4))  # 1~10 4등분

a = np.arange(1, 16)
print(a)
print(a.shape)  # 1차원 15칸
print(a.reshape(5, 3))  # y->5, x->3 전체 칸수 일치해야함
print(a.reshape(3, 5, 1))
