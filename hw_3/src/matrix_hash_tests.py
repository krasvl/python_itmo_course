import os
import pytest
import numpy as np
from matrix_hash import MatrixHashMixinLine, MatrixHashMixinPoli, find_collision, cached_matmul

def test_matrix_hash_collisions():
    os.makedirs('artifacts/3.3', exist_ok=True)
    
    np.random.seed(0)  
    
    A, B, C, D = find_collision()
    
    AB = cached_matmul(A, B)
    CD = cached_matmul(C, D)
    
    A.save_to_file('artifacts/3.3/A.txt')
    B.save_to_file('artifacts/3.3/B.txt')
    C.save_to_file('artifacts/3.3/C.txt')
    D.save_to_file('artifacts/3.3/D.txt')
    AB.save_to_file('artifacts/3.3/AB.txt')
    CD.save_to_file('artifacts/3.3/CD.txt')
    
    with open('artifacts/3.3/hash.txt', 'w') as f:
        f.write(str(hash(AB)))
    
    A_loaded = MatrixHashMixinLine.load_from_file('artifacts/3.3/A.txt')
    C_loaded = MatrixHashMixinLine.load_from_file('artifacts/3.3/C.txt')
    AB_loaded = MatrixHashMixinLine.load_from_file('artifacts/3.3/AB.txt')
    CD_loaded = MatrixHashMixinLine.load_from_file('artifacts/3.3/CD.txt')
    
    assert hash(A_loaded) == hash(C_loaded)
    assert not np.array_equal(A_loaded.data, C_loaded.data)
    assert np.array_equal(B.data, D.data)
    assert not np.array_equal(AB_loaded.data, CD_loaded.data)

def test_matrix_hash_equal1():
    m1 = MatrixHashMixinPoli([[1, 2], [3, 4]])
    m2 = MatrixHashMixinPoli([[1, 2], [3, 4]])
    assert hash(m1) == hash(m2)

def test_matrix_hash_diff1():
    m1 = MatrixHashMixinPoli([[3, 4], [1, 2]])
    m2 = MatrixHashMixinPoli([[1, 2], [3, 4]])
    assert hash(m1) != hash(m2)

def test_matrix_hash_equal2():
    m1 = MatrixHashMixinPoli([[1, 2, 3, 4], [1, 2, 3, 4]])
    m2 = MatrixHashMixinPoli([[1, 2, 3, 4], [1, 2, 3, 4]])
    assert hash(m1) == hash(m2)

def test_matrix_hash_diff2():
    m1 = MatrixHashMixinPoli([[1, 2, 3, 4], [1, 2, 3, 4]])
    m2 = MatrixHashMixinPoli([[1, 2, 3, 4], [1, 2, 3, 5]])
    assert hash(m1) != hash(m2)

def test_matrix_hash_equal3():
    m1 = MatrixHashMixinPoli([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
    m2 = MatrixHashMixinPoli([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
    assert hash(m1) == hash(m2)

def test_matrix_hash_diff3():
    m1 = MatrixHashMixinPoli([[0, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
    m2 = MatrixHashMixinPoli([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 5]])
    assert hash(m1) != hash(m2)

if __name__ == '__main__':
    pytest.main()