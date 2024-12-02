from functools import lru_cache
import numpy as np
from matrix_mixin import FileMixin, MatmulMixin

BASE0 = 257
BASE1 = 269

#Полиномиальное хеширование строк
#Коллизии только на больших матрицах из-за этого вывод не очень читаемый
class HashMixinPoli:
    def __hash__(self):
        hash_value = 0
        for i in range(self.data.shape[0]):
            s = 0
            for j in range(self.data.shape[1]):
                s = s * BASE0 + int(self.data[i, j])
            hash_value = hash_value * BASE1 + s
        return hash_value

class HashMixinLine:
    def __hash__(self):
        hash_value = 0
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                hash_value = int(self.data[i, j])
        return hash_value
    
@lru_cache(maxsize=None)
def cached_matmul(a, b):
    return a @ b

class MatrixHashMixinPoli(MatmulMixin, FileMixin, HashMixinPoli):
    def __init__(self, data):
        self.data = np.array(data)

class MatrixHashMixinLine(MatmulMixin, FileMixin, HashMixinLine):
    def __init__(self, data):
        self.data = np.array(data)

# Функция для поиска коллизии
def find_collision():
    while True:
        A = MatrixHashMixinLine(np.random.randint(0, 10, (6, 6)))
        C = MatrixHashMixinLine(np.random.randint(0, 10, (6, 6)))
        if hash(A) == hash(C) and not np.array_equal(A.data, C.data):
            B = MatrixHashMixinLine(np.random.randint(0, 10, (6, 6)))
            D = MatrixHashMixinLine(B.data.copy())
            if not np.array_equal((A @ B).data, (C @ D).data):
                return A, B, C, D