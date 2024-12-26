# -*- coding: utf-8 -*-
import math

#open file
file_name = 'input.txt'
file = open(file_name,mode='r')

rules = {}
updates = []

#read rules
line = file.readline()
while line != '\n':
    numeros = line.split('|')
    rule = rules.get(int(numeros[0]), [])
    rule.append(int(numeros[1]))
    rules[int(numeros[0])] = rule
    line = file.readline()

#read updates
line = file.readline()
while line:
    update = [int(x) for x in line.split(',')]
    updates.append(update)
    line = file.readline()

def isValid(update, rules):
    for i in range(len(update)):
        num1 = update[i]
        for j in range(i+1,len(update)):
            num2 = update[j]
            if num1 in rules.get(num2, []):
                return False
    return True

total = 0
for update in updates:
    if isValid(update,rules):
        #the number in the middle
        total += update[math.ceil(len(update)/2 - 1)]

#print(total)

#---------------------------- Part 2 ----------------------------
        
#assuming it can be valid
def fixUpdate(update, rules):
    new_update = update.copy()
    #swap pages until is valid
    while not isValid(new_update, rules):
        for i in range(len(new_update)):
            num1 = new_update[i]
            for j in range(i+1,len(new_update)):
                num2 = new_update[j]
                if num1 in rules.get(num2, []):
                    #swap the two pages that are invalid
                    aux = new_update[i]
                    new_update[i] = new_update[j]
                    new_update[j] = aux
    return new_update
        

total = 0
for update in updates:
    if not isValid(update,rules):
        fixed = fixUpdate(update, rules)
        total += fixed[math.ceil(len(fixed)/2 - 1)]
print(total)