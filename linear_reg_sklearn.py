# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:00:26 2022

@author: parkh
"""
from scratch.statistics import num_friends_good, daily_minutes_good
from sklearn.linear_model import LinearRegression
X = [[x] for x in num_friends_good]
Y = [[y] for y in daily_minutes_good]
reg = LinearRegression().fit(X, Y)

print(reg.score(X, Y)) 
print(reg.coef_)  
print(reg.intercept_) 