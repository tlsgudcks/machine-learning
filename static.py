# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:39:42 2022

@author: parkh
"""

def updf(x:float)->float: #확률 밀도함수
    if (x<2 or x>3):
        return 0
    else:
        return 1/(3-2)
def ucdf(x:float)->float: #누적 분포함수
    if x<2: 
        return 0
    if x>3:
        return 1
    else:
        return x-2
print(updf(2.3))
print(round(ucdf(2.3),10))

import math
SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))
print(normal_pdf(1.96))
coin = 0.5
count = 1
while coin>0.05:
    coin = 0.5
    coin = coin**count
    count = count+1
print(count-1)
    
    
