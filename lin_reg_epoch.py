# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 21:29:36 2022

@author: parkh
"""

from typing import Callable
from typing import List

Vector = List[float]

def difference_quotient(f: Callable[[float], float],
                        x: float,
                        h: float) -> float:
    return (f(x + h) - f(x)) / h

def partial_difference_quotient(f: Callable[[Vector], float], 
                                v: Vector, 
                                i: int,h: float) -> float:
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h

def estimate_gradient(f: Callable[[Vector], float], v:Vector, h:float=0.0001):
	return [partial_difference_quotient(f,v,i,h) for i in range(len(v))]

import random
from linear_algebra import distance, add, scalar_multiply

def gradient_step(v: Vector, gradient: Vector, 
                  step_size: float) -> Vector:
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)

def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]

# pick a random starting point
v = [random.uniform(-10, 10) for i in range(3)]
for epoch in range(1000):  # 이 파트가 얼마나 정밀하게 근접하는가를 결정함
     grad = sum_of_squares_gradient(v)    # compute the gradient at v
     v = gradient_step(v, grad, -0.01)    # take a negative gradient step
     print(epoch, v)
  
assert distance(v, [0, 0, 0]) < 0.001

# x ranges from -50 to 49, y is always 20 * x + 5
inputs = [(x, 20 * x + 5) for x in range(-50, 50)]

def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope * x + intercept    # 모델
    error = (predicted - y)              # error is (predicted - actual)
    squared_error = error ** 2         # 손실함수->최소화, 미분해서 기울기계산필요
    grad = [2 * error * x, 2 * error]    # slope과 intercept의 x지점에서의 기울기
    return grad
import random
from linear_algebra import vector_mean

theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
    
learning_rate = 0.001
    
for epoch in range(5000):
# Compute the mean of the gradient
    grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
# Take a step in that direction
    theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)
    
slope, intercept = theta
assert 19.9 < slope < 20.1,   "slope should be about 20"
assert 4.9 < intercept < 5.1, "intercept should be about 5"






