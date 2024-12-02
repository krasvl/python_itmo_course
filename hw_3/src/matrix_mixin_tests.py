import os
import pytest
import numpy as np
from matrix_mixin import MatrixMixin

def test_matrix_operations():
    os.makedirs('artifacts/3.2', exist_ok=True)
    
    np.random.seed(0)
    
    matrix1 = MatrixMixin(np.random.randint(0, 10, (10, 10)))
    matrix2 = MatrixMixin(np.random.randint(0, 10, (10, 10)))
    
    add = matrix1 + matrix2
    sub = matrix1 - matrix2
    mul = matrix1 * matrix2
    matmul = matrix1 @ matrix2
    div = matrix1 / matrix2
    
    with open('artifacts/3.2/matrix_add.txt', 'w') as f:
        f.write(str(add))
    
    with open('artifacts/3.2/matrix_sub.txt', 'w') as f:
        f.write(str(sub))
    
    with open('artifacts/3.2/matrix_mul.txt', 'w') as f:
        f.write(str(mul))
    
    with open('artifacts/3.2/matrix_matmul.txt', 'w') as f:
        f.write(str(matmul))
    
    with open('artifacts/3.2/matrix_div.txt', 'w') as f:
        f.write(str(div))
    
    assert os.path.exists('artifacts/3.2/matrix_add.txt')
    assert os.path.exists('artifacts/3.2/matrix_sub.txt')
    assert os.path.exists('artifacts/3.2/matrix_mul.txt')
    assert os.path.exists('artifacts/3.2/matrix_matmul.txt')
    assert os.path.exists('artifacts/3.2/matrix_div.txt')

def test_matrix_add():
    m1 = MatrixMixin([[1, 2], [3, 4]])
    m2 = MatrixMixin([[5, 6], [7, 8]])
    result = m1 + m2
    assert np.array_equal(result.data, np.array([[6, 8], [10, 12]]))

def test_matrix_sub():
    m1 = MatrixMixin([[1, 2], [3, 4]])
    m2 = MatrixMixin([[5, 6], [7, 8]])
    result = m1 - m2
    assert np.array_equal(result.data, np.array([[-4, -4], [-4, -4]]))

def test_matrix_mul():
    m1 = MatrixMixin([[1, 2], [3, 4]])
    m2 = MatrixMixin([[5, 6], [7, 8]])
    result = m1 * m2
    assert np.array_equal(result.data, np.array([[5, 12], [21, 32]]))

def test_matrix_matmul():
    m1 = MatrixMixin([[1, 2], [3, 4]])
    m2 = MatrixMixin([[5, 6], [7, 8]])
    result = m1 @ m2
    assert np.array_equal(result.data, np.array([[19, 22], [43, 50]]))

def test_matrix_div():
    m1 = MatrixMixin([[1, 2], [3, 4]])
    m2 = MatrixMixin([[5, 6], [7, 8]])
    result = m1 / m2
    assert np.allclose(result.data, np.array([[0.2, 1/3], [3/7, 0.5]]))


def test_matrix_file():
    m = MatrixMixin([[1, 2], [3, 4]])
    m.save_to_file('artifacts/3.2/test_matrix.txt')
    loaded_m = MatrixMixin.load_from_file('artifacts/3.2/test_matrix.txt')
    assert np.array_equal(m.data, loaded_m.data)

def test_matrix_str():
    m = MatrixMixin([[1, 2], [3, 4]])
    assert str(m) == "[[1, 2],\n [3, 4]]"

def test_matrix_props():
    m = MatrixMixin([[1, 2, 3], [4, 5, 6]])
    assert m.shape == (2, 3)
    assert m.size == 6

if __name__ == '__main__':
    pytest.main()