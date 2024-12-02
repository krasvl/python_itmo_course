import numpy as np

class AddMixin:
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.data + other)
        elif isinstance(other, self.__class__):
            return self.__class__(np.add(self.data, other.data))
        else:
            return NotImplemented

class SubMixin:
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.data - other)
        elif isinstance(other, self.__class__):
            return self.__class__(np.subtract(self.data, other.data))
        else:
            return NotImplemented

class MulMixin:
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.data * other)
        elif isinstance(other, self.__class__):
            return self.__class__(np.multiply(self.data, other.data))
        else:
            return NotImplemented

class MatmulMixin:
    def __matmul__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(np.matmul(self.data, other.data))
        else:
            return NotImplemented

class TruedivMixin:
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.data / other)
        elif isinstance(other, self.__class__):
            return self.__class__(np.divide(self.data, other.data))
        else:
            return NotImplemented

class FileMixin:
    def save_to_file(self, filename):
        np.savetxt(filename, self.data, fmt='%d')

    @classmethod
    def load_from_file(cls, filename):
        return cls(np.loadtxt(filename, dtype=int))

class StrMixin:
    def __str__(self):
        return np.array2string(self.data, separator=', ')

class PropMixin:
    @property
    def shape(self):
        return self.data.shape

    @property
    def size(self):
        return self.data.size

class MatrixMixin(AddMixin, SubMixin, MulMixin, MatmulMixin, TruedivMixin, FileMixin, StrMixin, PropMixin):
    def __init__(self, data):
        self.data = np.array(data)