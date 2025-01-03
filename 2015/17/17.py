# -*- coding: utf-8 -*-
import numpy as np

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
capacities = []
for line in file:
    capacities.append(int(line.strip()))
    
memo =  np.ones((151, len(capacities)+1)) * -1

def combinations(container, capacities, liters):
    if liters < 0:
        return 0
    elif memo[liters, container] != -1:
        return memo[liters, container]
    elif liters == 0:
        memo[liters, container] = 1
        return 1
    elif container == len(capacities):
        memo[liters, container] = 0
        return 0
    else:
        #Using the container
        liters_left = liters - capacities[container]
        comb = combinations(container +1, capacities, liters_left)
        #Not using it
        comb += combinations(container +1, capacities, liters)
        memo[liters, container] = comb
        return comb
    

print(combinations(0, capacities, 150))
#---------------------------- Part 2 ----------------------------

memo =  [[(-1, np.inf) for _ in range(len(capacities)+1)] for _ in range(151)]

def combinationsMin(container, capacities, liters):
    
    if liters < 0:
        return (0, np.inf)
    elif memo[liters][container][0] != -1:
        return memo[liters][container]
    elif liters == 0:
        memo[liters][container] = (1, 0)
        return (1, 0)
    elif container == len(capacities):
        memo[liters][container] = (0, np.inf)
        return (0, np.inf)
    else:
        #Using the container
        liters_left = liters - capacities[container]
        (comb_u, amount_u) = combinationsMin(container +1, capacities, liters_left)
        amount_u += 1
        
        #Not using it
        (comb_nu, amount_nu) = combinationsMin(container +1, capacities, liters)
        
        if amount_u == amount_nu:
            memo[liters][container] = (comb_u + comb_nu, amount_u)
            return (comb_u + comb_nu, amount_u)
        elif amount_u < amount_nu:
            memo[liters][container] = (comb_u, amount_u)
            return (comb_u, amount_u)
        else:
            memo[liters][container] = (comb_nu, amount_nu)
            return (comb_nu, amount_nu)
            

print(combinationsMin(0, capacities, 150))