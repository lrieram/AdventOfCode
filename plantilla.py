# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
strings = []
for line in file:
    strings.append(line.strip())
    
#---------------------------- Part 2 ----------------------------