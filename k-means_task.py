# -*- coding: utf-8 -*-
"""
Created on Sat May 28 21:19:08 2022

@author: parkh
"""

from scratch.linear_algebra import Vector
def num_differences(v1: Vector, v2: Vector) -> int:
    assert len(v1) == len(v2)
    return len([x1 for x1, x2 in zip(v1, v2) if x1 != x2])

from typing import List
from scratch.linear_algebra import vector_mean

def cluster_means(k: int,
                  inputs: List[Vector],
                  assignments: List[int]) -> List[Vector]:
    # clusters[i] contains the inputs whose assignment is i
    clusters = [[] for i in range(k)]
    for input, assignment in zip(inputs, assignments):
        clusters[assignment].append(input)

    # if a cluster is empty, just use a random point
    return [vector_mean(cluster) if cluster else random.choice(inputs)
            for cluster in clusters]

import itertools
import random
import tqdm
from scratch.linear_algebra import squared_distance

class KMeans:
    def __init__(self, k: int) -> None:
        self.k = k                      # number of clusters
        self.means = None

    def classify(self, input: Vector) -> int:
        """return the index of the cluster closest to the input"""
        return min(range(self.k),
                   key=lambda i: squared_distance(input, self.means[i]))

    def train(self, inputs: List[Vector]) -> None:
        # Start with random assignments
        assignments = [random.randrange(self.k) for _ in inputs]

        with tqdm.tqdm(itertools.count()) as t:
            for _ in t:
                # Compute means and find new assignments
                self.means = cluster_means(self.k, inputs, assignments)
                new_assignments = [self.classify(input) for input in inputs]

                # Check how many assignments changed and if we're done
                num_changed = num_differences(assignments, new_assignments)
                if num_changed == 0:
                    return assignments

                # Otherwise keep the new assignments, and compute new means
                assignments = new_assignments
                self.means = cluster_means(self.k, inputs, assignments)
                t.set_description(f"changed: {num_changed} / {len(inputs)}")

def main():
    inputs : List[List[float]]=[]
    from sklearn import datasets
    wine = datasets.load_wine()
    Y = []
    for i in range(5, len(wine.data), 5):
        inputs.append([wine.data[i][x] for x in range(13)]) #데이터 이용
        Y.append(wine.target[i])
    
    random.seed(14)                   # so you get the same results as me
    clusterer = KMeans(k=3)
    pred_Y=clusterer.train(inputs)
    means = sorted(clusterer.means)   # sort for the unit test
    print(means)
    print(pred_Y) #예측값
    print(Y) #실제 클래스
    
    # Check that the means are close to what we expect.
    from sklearn.metrics import accuracy_score
    print(accuracy_score(Y, pred_Y)) #F1 SCORE
    
    
if __name__ == "__main__": main()