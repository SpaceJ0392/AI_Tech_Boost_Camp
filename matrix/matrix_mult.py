# 행렬의 내적 계산 (결과적으로는 같은 결과)
import numpy as np

X = np.array([[1, -2, 3], [7, 5, 0], [-2, -1, 2]])

Y = np.array([[0, 1, -1], [1, -1, 0]])

# 수학적인 방법의 내적 계산 (전치 행렬과 내적)
print("X @ Y.T : ", X @ Y.T)

# inner를 이용한 계산 (그냥 같은 위치의 행벡터 끼리 내적)
print("np.inner : ", np.inner(X, Y))

# 역행렬 (1. 행렬의 행수와 열수가 같아야 한다, 2. determinant = 0 이 아니어야 한다)

print("np.linalg.inv(X) : ", np.linalg.inv(X))
# 행 열의 개수는 파악할 수 있으나, determinant는 계산하기 어려우므로 메소드가 통과하는지를 살펴볼 것

# X X^-1 = I
print("X X^-1 = I : ", X @ np.linalg.inv(X))
