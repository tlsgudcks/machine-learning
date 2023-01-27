# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 22:39:14 2022

@author: parkh
"""
from typing import List
from linear_algebra import vector_mean,scalar_multiply,add
import random


Vector = List[float]

inputs = [(-50, 4978.8), (-49, 4776.400000000001), (-48, 4578.200000000001), (-47, 4384.200000000001), (-46, 4194.400000000001), (-45, 4008.8), (-44, 3827.4000000000005), (-43, 3650.2000000000003), (-42, 3477.2000000000003), (-41, 3308.4000000000005), (-40, 3143.8), (-39, 2983.4), (-38, 2827.2000000000003), (-37, 2675.2000000000003), (-36, 2527.4), (-35, 2383.8), (-34, 2244.4), (-33, 2109.2000000000003), (-32, 1978.2), (-31, 1851.4), (-30, 1728.8), (-29, 1610.4), (-28, 1496.2), (-27, 1386.2), (-26, 1280.4), (-25, 1178.8), (-24, 1081.4), (-23, 988.2), (-22, 899.2), (-21, 814.4), (-20, 733.8), (-19, 657.4), (-18, 585.1999999999999), (-17, 517.1999999999999), (-16, 453.40000000000003), (-15, 393.8), (-14, 338.40000000000003), (-13, 287.20000000000005), (-12, 240.20000000000005), (-11, 197.40000000000003), (-10, 158.8), (-9, 124.39999999999999), (-8, 94.2), (-7, 68.2), (-6, 46.400000000000006), (-5, 28.8), (-4, 15.400000000000002), (-3, 6.200000000000002), (-2, 1.2000000000000002), (-1, 0.3999999999999999), (0, 3.8), (1, 11.399999999999999), (2, 23.2), (3, 39.2), (4, 59.4), (5, 83.8), (6, 112.4), (7, 145.20000000000002), (8, 182.20000000000002), (9, 223.4), (10, 268.8), (11, 318.40000000000003), (12, 372.20000000000005), (13, 430.20000000000005), (14, 492.40000000000003), (15, 558.8), (16, 629.4), (17, 704.1999999999999), (18, 783.1999999999999), (19, 866.4), (20, 953.8), (21, 1045.3999999999999), (22, 1141.2), (23, 1241.2), (24, 1345.4), (25, 1453.8), (26, 1566.4), (27, 1683.2), (28, 1804.2), (29, 1929.4), (30, 2058.8), (31, 2192.4000000000005), (32, 2330.2000000000003), (33, 2472.2000000000003), (34, 2618.4), (35, 2768.8), (36, 2923.4), (37, 3082.2000000000003), (38, 3245.2000000000003), (39, 3412.4), (40, 3583.8), (41, 3759.4000000000005), (42, 3939.2000000000003), (43, 4123.2), (44, 4311.400000000001), (45, 4503.8), (46, 4700.400000000001), (47, 4901.200000000001), (48, 5106.200000000001), 
 (49, 5315.400000000001)]
def linear_gradient2(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept, c = theta
    h=0.001
    predicted = slope * x**2 + intercept*x + c    # 모델
    error = (predicted - y)              # error is (predicted - actual)
    squared_error1 = error ** 2          # f(slope,intercept)
    predicted = predicted = slope * x**2 + intercept*x + c    # 모델
    error = (predicted - y)              # error is (predicted - actual)
    squared_error2= error ** 2           # f(slope+h,intercept)
    predicted = predicted = slope * x**2 + intercept*x + c    # 모델
    error = (predicted - y)              # error is (predicted - actual)
    squared_error3= error ** 2           # f(slope,intercept+h)
    predicted = predicted = slope * x**2 + intercept*x + c    # 모델
    error = (predicted - y)              # error is (predicted - actual)
    squared_error4 = error ** 2           # f(slope,intercept+h)
    # slope과 intercept의 x지점에서의 기울기
    grad = [(squared_error2-squared_error1)/h, (squared_error3-squared_error1)/h,(squared_error4-squared_error1)/h]    
    return grad

def gradient_step(v: Vector, gradient: Vector, 
                  step_size: float) -> Vector:
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)
    
# Start with random values for slope and intercept.
theta = [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)]
learning_rate = 0.001
print(theta)
for epoch in range(10000):
    # Compute the mean of the gradients
    grad = vector_mean([linear_gradient2(x, y, theta) for x, y in inputs])
    print('grad',grad)
    # Take a step in that direction
    theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)
#slope, intercept = theta
#assert 4.9 < slope < 5.1   
#assert 4.9 < -intercept < 5.1