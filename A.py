# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:47:21 2022

@author: parkh
"""
from collections import Counter
import matplotlib.pyplot as plt

f=open('samplefile.txt')

list_alpha=[]
lst=[]

for words in f:
    words = words.split()
    for word in words:
        word=word.upper()
        for i in word:
            list_alpha.append(i)
alpha = Counter(i for i in list_alpha)
lst = sorted(alpha.items(), key=lambda x: x[1], reverse=True)
lst = lst[:5]
print(lst)

alphabet =[]
number = []
for i in range(5):
    alphabet.append(lst[i][0])
    number.append(lst[i][1])

xs = [i + 0.1 for i, _ in enumerate(alphabet)]

plt.bar(xs,number)
plt.ylabel("count")
plt.title("alphabet")
plt.xticks([i + 0.1 for i, _ in enumerate(alphabet)], alphabet)

plt.show()

num_sum = sum(number)
percent_num = [i/num_sum for i in number]
plt.pie(percent_num, labels = alphabet)
plt.axis("equal")
plt.legend()
plt.show()

