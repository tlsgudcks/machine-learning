# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 10:05:17 2022

@author: parkh
"""
from typing import List
from scratch.linear_algebra import dot, Vector
from sklearn import datasets
def predict(x:Vector, beta:Vector)->float:
    return dot(x, beta)
def error(x: Vector, y: float, beta: Vector) -> float:
    return predict(x, beta) - y

def squared_error(x: Vector, y: float, beta: Vector) -> float:
    return error(x, y, beta) ** 2

def sqerror_gradient(x: Vector, y: float, beta: Vector) -> Vector:
    err = error(x, y, beta)
    return [2 * err * x_i for x_i in x]
import random
import tqdm
from scratch.linear_algebra import vector_mean
from scratch.gradient_descent import gradient_step
from scratch.statistics import daily_minutes_good
linnerud = datasets.load_linnerud()
inputs:List[List[float]] = [[1.0,1.0,1.0,1.0] for x in range(20)]
Y=[]
for i in range(20):
    for x in range(3):
        inputs[i][x+1] = float(linnerud.data[i][x])#데이터 이용
    Y.append(linnerud.target[i][0])

def least_squares_fit(xs: List[Vector],
                      ys: List[float],
                      learning_rate: float = 0.001,
                      num_steps: int = 1000,
                      batch_size: int = 1) -> Vector:
    
    # Start with a random guess
    guess = [random.random() for _ in xs[0]]
    for _ in tqdm.trange(num_steps, desc="least squares fit"):
        for start in range(0, len(xs), batch_size):
            batch_xs = xs[start:start+batch_size]
            batch_ys = ys[start:start+batch_size]
            gradient = vector_mean([sqerror_gradient(x, y, guess)
                                    for x, y in zip(batch_xs, batch_ys)])
            guess = gradient_step(guess, gradient, -learning_rate)
    return guess

from scratch.simple_linear_regression import total_sum_of_squares

def multiple_r_squared(xs: List[Vector], ys: Vector, beta: Vector) -> float:
    sum_of_squared_errors = sum(error(x, y, beta) ** 2
                                for x, y in zip(xs, ys))
    return 1.0 - sum_of_squared_errors / total_sum_of_squares(ys)

beta=least_squares_fit(inputs, Y, 0.001, 1000 ,1)
r = multiple_r_squared(inputs, Y, beta)
print(beta)
print(r)

