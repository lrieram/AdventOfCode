# -*- coding: utf-8 -*-

start = '1113122113'

def lookAndSay(number):
    res = ''
    actual = number[0]
    cant = 0
    for n in number:
        if n == actual:
            cant += 1
        else:
            res += str(cant) + actual
            actual = n
            cant = 1
    res += str(cant) + actual
    return res

next_number = start
for _ in range(40):
    next_number = lookAndSay(next_number)  

print(len(next_number))
#---------------------------- Part 2 ----------------------------

next_number = start
for _ in range(50):
    next_number = lookAndSay(next_number)  

print(len(next_number))