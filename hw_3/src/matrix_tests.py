import os
import pytest
import numpy as np
from matrix import Matrix

def test_matrix_operations():
    os.makedirs('artifacts/3.1', exist_ok=True)
    
    np.random.seed(0)
    
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))
    
    add = matrix1 + matrix2
    mul = matrix1 * matrix2
    matmul = matrix1 @ matrix2
    
    with open('artifacts/3.1/matrix_add.txt', 'w') as f:
        f.write(str(add))
    
    with open('artifacts/3.1/matrix_mul.txt', 'w') as f:
        f.write(str(mul))
    
    with open('artifacts/3.1/matrix_matmul.txt', 'w') as f:
        f.write(str(matmul))
    
    assert os.path.exists('artifacts/3.1/matrix_add.txt')
    assert os.path.exists('artifacts/3.1/matrix_mul.txt')
    assert os.path.exists('artifacts/3.1/matrix_matmul.txt')

def test_matrix_add():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    result = m1 + m2
    assert np.array_equal(result.data, np.array([[6, 8], [10, 12]]))

def test_matrix_mul():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[2, 0], [1, 3]])
    result = m1 * m2
    assert np.array_equal(result.data, np.array([[2, 0], [3, 12]]))

def test_matrix_matmul():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[2, 0], [1, 3]])
    result = m1 @ m2
    assert np.array_equal(result.data, np.array([[4, 6], [10, 12]]))

def test_matrix_add_invalid_shape():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError):
        m1 + m2

def test_matrix_mult_invalid_shape():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError):
        m1 * m2

def test_matrix_matmult_invalid_shape():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with pytest.raises(ValueError):
        m1 @ m2


if __name__ == '__main__':
    pytest.main()