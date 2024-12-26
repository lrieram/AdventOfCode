# -*- coding: utf-8 -*-

file_name = 'input.txt'
file = open(file_name,mode='r')

s = ''
for line in file:
    s += line

up = s.count('(')
down = s.count(')')

#print(up-down)

floor = 0
position = 0
while floor >= 0:
    if s[position] == '(':
        floor += 1
    elif s[position] == ')':
        floor -= 1
    else:
        print('Error')
    position += 1
    
print(position)