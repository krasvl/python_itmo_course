import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)
        self.shape = self.data.shape

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Invalid shapes")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.shape != other.shape:
            raise ValueError("Invalid shapes")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Invalid shapes")
        return Matrix(self.data @ other.data)

    def __str__(self):
        return str(self.data)
