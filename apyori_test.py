# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 03:12:36 2022

@author: parkh
"""

# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
print(transactions)
# print(transactions[0:1])
# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.01, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)

for item in results:
    print(item)
    print("----------------")
    # first index of the inner list
    # Contains base item and add item
    pair = item[0]
    items = [x for x in pair]
    print(items)
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")