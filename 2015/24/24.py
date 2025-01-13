# -*- coding: utf-8 -*-
import math
from itertools import combinations

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
weights = []
for line in file:
    weights.append(int(line.strip()))



target_weight = sum(weights) // 3
min_qe = math.prod(weights)

for i in range(len(weights)):
    comb = [x for x in combinations(weights, i) if sum(x) == target_weight]
    #Assuming that the rest can be divided in two part of same weight
    #If not only should add that to filter
    if len(comb) > 0:
        best_combination = []
        for combination in comb:
            min_qe = min(min_qe, math.prod(combination))
        break
    
print(min_qe)
#---------------------------- Part 2 ----------------------------

new_target_weight = sum(weights) // 4
min_qe = math.prod(weights)

for i in range(len(weights)):
    comb = [x for x in combinations(weights, i) if sum(x) == new_target_weight]
    #Assuming that the rest can be divided in two part of same weight
    #If not only should add that to filter
    if len(comb) > 0:
        best_combination = []
        for combination in comb:
            min_qe = min(min_qe, math.prod(combination))
        break
    
print(min_qe)
