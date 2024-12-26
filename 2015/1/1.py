# -*- coding: utf-8 -*-

#open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#read file
indications = ''
for line in file:
    indications += line.strip()

up = indications.count('(')
down = indications.count(')')

#print(up-down)

#---------------------------- Part 2 ----------------------------

floor = 0
position = 0
while floor >= 0:
    if indications[position] == '(':
        floor += 1
    elif indications[position] == ')':
        floor -= 1
    else:
        print('Error')
    position += 1
    
print(position)