import numpy as np


def softmax(vec):  # 그냥 소프트맥스 연산 수식을 그대로 사용
    denumerator = np.exp(vec - np.max(vec, axis=-1, keepdims=True))
    # 다만, exp를 할때 너무 큰 벡터는 overflow가 날 수 있어 max 값을 빼서 처리 한다.
    # 단순한 트릭 (이렇게 해도 소프트맥스 연산을 할 수 있다.)
    numerator = np.sum(denumerator, axis=-1, keepdims=True)
    val = denumerator / numerator
    return val


vec = np.array([[1, 2, 0], [-1, 0, 1], [-10, 0, 10]])
print(softmax(vec))
