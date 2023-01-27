# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 22:39:14 2022

@author: parkh
"""
from typing import List
from linear_algebra import vector_mean,scalar_multiply,add
import random


Vector = List[float]

inputs = [(-50, -255), (-49, -250), (-48.1, -245), (-47, -240), (-46, -235), 
          (-45, -230), (-44, -225), (-43, -220), (-42, -215), (-41, -210), 
          (-40, -205), (-39, -200), (-38, -195), (-37, -190), (-36, -185), 
          (-35, -180), (-34, -175), (-33, -170), (-32, -165), (-31, -160), 
          (-30, -155), (-29, -150), (-28, -145), (-27, -140), (-26, -135), 
          (-25.2, -130), (-24, -125), (-23, -120), (-22, -115), (-21, -110), 
          (-20, -105), (-19, -100), (-18, -95), (-17, -90), (-16, -85), 
          (-15, -80), (-14, -75), (-13, -70), (-12, -65), (-11, -60), 
          (-10, -55), (-9, -50), (-8, -45), (-7, -40), (-6, -35), (-5, -30), 
          (-4, -25), (-3, -20), (-2, -15), (-1, -10), (0, -5), (1, 0.1), (2, 5), 
          (3, 10), (4, 15), (5, 20), (6, 25), (7, 30), (8, 35), (9, 40), (10, 45), 
          (11, 50), (12, 55), (13, 60), (14, 65), (15, 70), (16, 75), (17, 80), 
          (18, 85), (19, 90), (20, 95), (21, 100), (22, 105.7), (23, 110), 
          (24, 115), (25, 120), (26, 125), (27, 130), (28, 135), (29, 140), 
          (30, 144.8), (31, 150), (32, 155), (33, 160), (34, 165), (35, 170), 
          (36, 175), (37, 180), (38, 185), (39, 190), (40, 195), (41, 200), 
          (42, 205), (43, 210), (44, 215), (45, 220), (46, 225), (47, 230), 
          (48, 235), (49, 240)]
def linear_gradient2(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta
    h=0.001
    predicted = slope * x + intercept    # 모델
    error = (predicted - y)              # error is (predicted - actual)
    squared_error1 = error ** 2          # f(slope,intercept)
    predicted = (slope+h) * x + intercept    # 모델
    error = (predicted - y)              # error is (predicted - actual)
    squared_error2= error ** 2           # f(slope+h,intercept)
    predicted = slope * x + (intercept+h)    # 모델
    error = (predicted - y)              # error is (predicted - actual)
    squared_error3= error ** 2           # f(slope,intercept+h)
    # slope과 intercept의 x지점에서의 기울기
    grad = [(squared_error2-squared_error1)/h, (squared_error3-squared_error1)/h]    
    return grad

def gradient_step(v: Vector, gradient: Vector, 
                  step_size: float) -> Vector:
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)
    
# Start with random values for slope and intercept.
theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
learning_rate = 0.001
print(theta)
for epoch in range(100):
    # Compute the mean of the gradients
    grad = vector_mean([linear_gradient2(x, y, theta) for x, y in inputs])
    print('grad',grad)
    # Take a step in that direction
    theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)
# slope, intercept = theta
# assert 19.9 < slope < 20.1,   "slope should be about 20"
# assert 4.9 < intercept < 5.1, "intercept should be about 5"