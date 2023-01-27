# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:05:56 2022

@author: parkh
"""
from typing import List
from collections import Counter
import math

def mean(xs: List[float]) -> float: #리스트의 평균
    return sum(xs) / len(xs)
assert mean([3,4,5,6,7]) == 5

def median(v: List[float]) -> float: #리스트의 중앙값
    sv = sorted(v)
    if len(v) % 2 == 0:
        return (sv[len(sv)//2]+sv[len(sv)//2-1])/2
    else:
        return sv[len(sv)//2]

assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2

def quantile(xs: List[float], p: float) -> float: #리스트의 분위값
    """Returns the pth-percentile value in x"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]
num_friends = [1,2,3,4,5,6,7,8,1,1,6,6] 
daily_minutes = [3,3,2,3,1,4,1,2,3,4,2,1]

def mode(x: List[float]) -> List[float]: #리스트의 최빈값
    v=Counter(x).most_common(2)
    a= []
    a.append(v[0][0])
    a.append(v[1][0])
    return a
assert set(mode(num_friends)) == {1, 6}

from linear_algebra import sum_of_squares,dot

def de_mean(xs: List[float]) -> List[float]: # 평균과 차잇값
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float: #분산
    """Almost the average squared deviation from the mean"""
    assert len(xs) >= 2, "variance requires at least two elements"

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(xs: List[float]) -> float: #표준편차
    return math.sqrt(variance(xs))

def interquartile_range(xs: List[float]) -> float: #
    return quantile(xs, 0.75) - quantile(xs, 0.25)
a=interquartile_range(num_friends)
print(a)

def covariance(xs: List[float], ys: List[float]) -> float: #공분산
    assert len(xs) == len(ys)
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

cv=covariance(num_friends,daily_minutes)
print(cv)

def correlation(xs: List[float], ys: List[float]) -> float:
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0    # if no variation, correlation is zero

#assert 0.24 < correlation(num_friends, daily_minutes) < 0.25








