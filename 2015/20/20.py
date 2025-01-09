# -*- coding: utf-8 -*-

input_number = 36000000

target = 3600000

def part1():
    presents = [0] * target
    for i in range(1,target):
        if presents[i] + i >= target:
            return i
        for j in range(i, target, i):
            presents[j] = presents[j] + i

#print(part1())
#---------------------------- Part 2 ----------------------------


def part2():
    presents = [0] * input_number
    for i in range(1,input_number):
        if presents[i] + (i * 11) >= input_number:
            return i
        for j in range(i, min(i * 51, input_number), i):
            presents[j] = presents[j] + i*11
    
        
print(part2())