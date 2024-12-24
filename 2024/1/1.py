# -*- coding: utf-8 -*-
import numpy as np

file_name = 'input.txt'
file = open(file_name,mode='r')
    
    
l1 = []
l2 = []
for line in file:
    line = line.strip()
    numero1, numero2 = line.split()  
    numero1 = int(numero1)
    numero2 = int(numero2)
    l1.append(numero1)
    l2.append(numero2)
    

def primera_parte(l1, l2):
    
    l1.sort()
    l1 = np.array(l1)
    l2.sort()
    l2 = np.array(l2)
    
    dif = np.abs(l1-l2)
    return(np.sum(dif))

def segunda_parte(l1,l2):
    similarity_score = 0
    for x in l1:
        apariciones = l2.count(x) 
        similarity_score += x*apariciones
    return similarity_score
        
print(segunda_parte(l1, l2))