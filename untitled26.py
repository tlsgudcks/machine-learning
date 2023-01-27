# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:24:05 2022

@author: parkh
"""
from typing import NamedTuple, Optional
from typing import Dict, TypeVar
from typing import List
T = TypeVar('T')  # generic type for inputs
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
import random
def select_input(inputs:List):
    random.shuffle(inputs)
    train_data_set = []
    train_rate = 0.7
    train_data_num = int(len(inputs)*train_rate)
    for i in range(11):
        train_data_set.append(inputs[i])
    return train_data_set
for i in range(5):
    print(i+1,"번째 input 데이터 ----------------------")
    a=select_input(inputs)
    print(a)
