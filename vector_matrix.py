# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 00:40:13 2022

@author: parkh
"""
import math

def func(a: str, b: float = 3.5) -> int:
    return a + b

value = func(3)
print(value)

from typing import List

Vector = List[float]

height_weight_age = [70,  # inches,
                     170, # pounds,
                     40 ] # years

grades = [95,   # exam1
          80,   # exam2
          75,   # exam3
          62 ]  # exam4

def add(v: Vector, w: Vector) -> Vector: # 두 개의 벡터 더하기
    """Adds corresponding elements"""
    assert len(v) == len(w) 

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def substract(v: Vector, w: Vector) -> Vector: # 두 개의 벡터 빼기
    assert len(v) == len(w)  
    return [v_i - w_i for v_i, w_i in zip(v, w)]
assert substract([4,5,6], [1,2,3]) == [3,3,3]

def vector_sum(vectors: List[Vector]) -> Vector: # 여러개의 벡터 더하기
    return [sum(i) for i in zip(*vectors)]    
assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

def scalar_multiply(c:float, v: Vector)-> Vector:
    return[c*v_i for v_i in v]
assert scalar_multiply(3, [1,2,3]) == [3,6,9]

def vector_mean(vectors: List[Vector])->Vector:
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w)
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6

def sum_of_squares(v: Vector) -> float: # [1,2,3]  1*1+2*2+3*3
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14  # 1 * 1 + 2 * 2 + 3 * 3

def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))   # math.sqrt is square root function

assert magnitude([3, 4]) == 5

def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(substract(v, w))

def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(squared_distance(v, w))

Matrix = List[List[float]]

A = [[1, 2, 3],  # A has 2 rows and 3 columns
     [4, 5, 6]]

B = [[1, 2],     # B has 3 rows and 2 columns
     [3, 4],
     [5, 6]]

from typing import Tuple
def shape(A: Matrix) -> Tuple[int, int]:
    return(len(A),len(A[0]))
assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)

def get_row(A: Matrix, i: int) -> Vector:
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    return [A_i[j] for A_i in A]

from typing import Callable

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    return[[entry_fn(i,j) for i in range(num_cols)]for j in range(num_rows)]
ma=make_matrix(3, 4, lambda x, y : x + y)
print(ma)

def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]



