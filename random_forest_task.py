# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 02:08:49 2022

@author: parkh
"""

from typing import List
import math
from typing import Any
from collections import Counter
from typing import NamedTuple, Optional
from typing import Dict, TypeVar
from collections import defaultdict
from typing import NamedTuple, Union, Any

T = TypeVar('T')  # generic type for inputs

def entropy(class_probabilities: List[float]) -> float:
    """Given a list of class probabilities, compute the entropy"""
    return sum(-p * math.log(p, 2) for p in class_probabilities if p > 0)


def class_probabilities(labels: List[Any]) -> List[float]:
    total_count = len(labels)
    return [count / total_count
            for count in Counter(labels).values()]

def data_entropy(labels: List[Any]) -> float:
    return entropy(class_probabilities(labels))

def partition_entropy(subsets: List[List[Any]]) -> float:
    """Returns the entropy from this partition of data into subsets"""
    total_count = sum(len(subset) for subset in subsets)

    return sum(data_entropy(subset) * len(subset) / total_count
               for subset in subsets)

class Candidate(NamedTuple):
    level: str
    lang: str
    tweets: bool
    phd: bool
    did_well: Optional[bool] = None  # allow unlabeled data

                  #  level     lang     tweets  phd  did_well
inputs = [Candidate('Senior', 'Java',   False, False, False),
          Candidate('Senior', 'Java',   False, True,  False),
          Candidate('Mid',    'Python', False, False, True),
          Candidate('Junior', 'Python', False, False, True),
          Candidate('Junior', 'R',      True,  False, True),
          Candidate('Junior', 'R',      True,  True,  False),
          Candidate('Mid',    'R',      True,  True,  True),
          Candidate('Senior', 'Python', False, False, False),
          Candidate('Senior', 'R',      True,  False, True),
          Candidate('Junior', 'Python', True,  False, True),
          Candidate('Senior', 'Python', True,  True,  True),
          Candidate('Mid',    'Python', False, True,  True),
          Candidate('Mid',    'Java',   True,  False, True),
          Candidate('Junior', 'Python', False, True,  False),
          Candidate('Junior', 'Python', True,  False, True),
          Candidate('Junior', 'R',      True,  True,  False),
          Candidate('Mid',    'Python', True,  True,  True),
          Candidate('Senior', 'Python', False, False, False)
         ]

def partition_by(inputs: List[T], attribute: str) -> Dict[Any, List[T]]:
    """Partition the inputs into lists based on the specified attribute."""
    partitions: Dict[Any, List[T]] = defaultdict(list)
    for input in inputs:
        key = getattr(input, attribute)  # value of the specified attribute
        partitions[key].append(input)    # add input to the correct partition
    return partitions
partition_by(inputs, 'phd')

def partition_entropy_by(inputs: List[Any],
                         attribute: str,
                         label_attribute: str) -> float:
    """Compute the entropy corresponding to the given partition"""
    # partitions consist of our inputs
    partitions = partition_by(inputs, attribute)

    # but partition_entropy needs just the class labels
    labels = [[getattr(input, label_attribute) for input in partition]
              for partition in partitions.values()]

    return partition_entropy(labels)

senior_inputs = [input for input in inputs if input.level == 'Senior']

class Leaf(NamedTuple):
    value: Any
class Split(NamedTuple):
    attribute: str
    subtrees: dict
    default_value: Any = None
    
DecisionTree = Union[Leaf, Split]

hiring_tree = Split('level', {   # First, consider "level".
    'Junior': Split('phd', {     # if level is "Junior", next look at "phd"
        False: Leaf(True),       #   if "phd" is False, predict True
        True: Leaf(False)        #   if "phd" is True, predict False
    }),
    'Mid': Leaf(True),           # if level is "Mid", just predict True
    'Senior': Split('tweets', {  # if level is "Senior", look at "tweets"
        False: Leaf(False),      #   if "tweets" is False, predict False
        True: Leaf(True)         #   if "tweets" is True, predict True
    })
})

def classify(tree: DecisionTree, input: Any) -> Any:
    """classify the input using the given decision tree"""

    # If this is a leaf node, return its value
    if isinstance(tree, Leaf):
        return tree.value

    # Otherwise this tree consists of an attribute to split on
    # and a dictionary whose keys are values of that attribute
    # and whose values of are subtrees to consider next
    subtree_key = getattr(input, tree.attribute)

    if subtree_key not in tree.subtrees:   # If no subtree for key,
        return tree.default_value          # return the default value.

    subtree = tree.subtrees[subtree_key]   # Choose the appropriate subtree
    return classify(subtree, input)        # and use it to classify the input

def build_tree_id3(inputs: List[Any],
                   split_attributes: List[str],
                   target_attribute: str) -> DecisionTree:
    # Count target labels
    label_counts = Counter(getattr(input, target_attribute)
                           for input in inputs)
    most_common_label = label_counts.most_common(1)[0][0]

    # If there's a unique label, predict it
    if len(label_counts) == 1:
        return Leaf(most_common_label)

    # If no split attributes left, return the majority label
    if not split_attributes:
        return Leaf(most_common_label)

    # Otherwise split by the best attribute

    def split_entropy(attribute: str) -> float:
        """Helper function for finding the best attribute"""
        return partition_entropy_by(inputs, attribute, target_attribute)

    best_attribute = min(split_attributes, key=split_entropy)

    partitions = partition_by(inputs, best_attribute)
    new_attributes = [a for a in split_attributes if a != best_attribute]

    # recursively build the subtrees
    subtrees = {attribute_value : build_tree_id3(subset,
                                                 new_attributes,
                                                 target_attribute)
                for attribute_value, subset in partitions.items()}

    return Split(best_attribute, subtrees, default_value=most_common_label)

#새롭게 추가한 코드
import random
def select_input(inputs: List): #랜덤하게 데이터를 샘플링함(부트스트랩 개념)
    inputs2 = inputs[:]
    random.shuffle(inputs2) #리스트를 랜덤하게 뽑기위한 셔플
    train_data_set = []
    train_rate = 0.7 #전체 데이터의 70%를 테스트 데이터로 사용
    train_data_num = int(len(inputs2)*train_rate)# 갯수만큼 트레이닝 데이터를 리턴함
    for i in range(train_data_num):
        train_data_set.append(inputs2[i])
    return train_data_set

votes = [[0,0] for i in range(len(inputs))] #데이터의 갯수만큼 투표 공간을 생성
for i in range(5): #만들 나무 갯수 설정
    a=select_input(inputs) #나무를 만들 때 사용할 데이터를 추출
    tree = build_tree_id3(a,
                      ['level', 'lang', 'tweets', 'phd'],
                      'did_well') #나무 생성
    print(i+1,"번째-------------------------------------------------------------------------",tree)
    pred_Y = [classify(tree, input) for input in inputs] #나무 예측결과
    print(pred_Y)
    for i in range(len(pred_Y)): # 만약 True라면 [i][0]에 1을 더하고 False라면 [i][1]에 1을더함
        if pred_Y[i] == True:    
            votes[i][0] +=1
        else:
            votes[i][1] +=1
print(votes) #투표결과 확인
for i in range(len(pred_Y)): #투표를 확인해 더 많이 나왔던 것으로 pred_Y를 설정해줌
    if votes[i][0]>votes[i][1]:
        pred_Y[i] = True
    else:
        pred_Y[i] = False
Y = [input.did_well for input in inputs] #원래 Y데이터
print(pred_Y) #예측 Y
print(Y) #실제 Y
from sklearn.metrics import accuracy_score
print(accuracy_score(Y, pred_Y)) #정확도출력