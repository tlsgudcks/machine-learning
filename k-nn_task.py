# -*- coding: utf-8 -*-
"""
Created on Sat May 28 21:06:09 2022

@author: parkh
"""
from collections import Counter
from scratch.linear_algebra import distance
from scratch.statistics import mean
import math, random
import matplotlib.pyplot as plt
from sklearn import datasets

def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]


def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
   return math.sqrt(squared_distance(v, w))

def raw_majority_vote(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

def majority_vote(labels):
    """assumes that labels are ordered from nearest to farthest"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner                     # unique winner, so return it
    else:
        return majority_vote(labels[:-1]) # try again without the farthest

def knn_classify(k, labeled_points, new_point):
    """each labeled point should be a pair (point, label)"""

    # order the labeled points from nearest to farthest
    by_distance = sorted(labeled_points,
             key=lambda point_label: distance(point_label[0], new_point))

    # find the labels for the k closest
    k_nearest_labels = [label for _, label in by_distance[:k]]

    # and let them vote
    return majority_vote(k_nearest_labels)
wine = datasets.load_wine()
Y_test = []
Y = []
Y_pred = []

inputs = []

wines = []
wines_Test=[]

for i in range(0, len(wine.data), 3): 
    inputs.append([wine.data[i][x] for x in range(13)]) #test 데이터 생성
    Y_test.append(wine.target[i])
for i in range(len(inputs)):
    wines_Test.append([inputs[i],Y_test[i]])
    
inputs = []

for i in range(1, len(wine.data), 10):
    inputs.append([wine.data[i][x] for x in range(13)]) #검증 데이터 생성
    Y.append(wine.target[i])
for i in range(len(inputs)):
    wines.append([inputs[i],Y[i]])


from sklearn.metrics import accuracy_score
for k in [1,3,5,7]:
    num_correct = 0
    for x, y in wines:
        other_wines = [other_wine
                        for other_wine in wines_Test
                        if other_wine != (x, y)]
        predicted_y = knn_classify(k, other_wines, x) #예측 y생성
        Y_pred.append(predicted_y) #예측 y 리스트에 저장
        if predicted_y == y:
            num_correct += 1
    print(Y_pred) #예측 Y
    print(Y) # 실제 Y
    print(k, "neighbor[s]:", num_correct, "correct out of", len(wines))
    print(accuracy_score(Y, Y_pred)) #F1 SCORE
    Y_pred=[] #예측 초기화


