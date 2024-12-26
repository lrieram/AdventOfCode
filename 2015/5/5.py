# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
strings = []
for line in file:
    strings.append(line.strip())
    
    
forbidden_combinations = ['ab', 'cd', 'pq', 'xy']
def isNice(s):
    vowels = 0
    double_letter = False
    prev = ''
    actual = ''
    for c in s:
        actual = c
        if actual in 'aeiou':
            vowels += 1
        if prev == actual:
            double_letter = True
        if prev+actual in forbidden_combinations:
            return False
        prev = c
    return vowels > 2 and double_letter

nice_strings = 0
for s in strings:
    if isNice(s):
        nice_strings += 1
        
#print(nice_strings)

#---------------------------- Part 2 ----------------------------

def isNicePart2(s):
    rule1 = False
    rule2 = False
    pairs = set()
    prev_pair = ''
    prev = ''
    prev2 = ''
    actual = ''
    for c in s:
        actual = c
        if actual == prev2:
            rule2 = True
        if prev + actual in pairs:
            rule1 = True
        #Only adding pairs when there are at least 2 characters
        if prev:
            #To avoid overlapping pairs, the pair is added
            #with delay
            if prev_pair:
                pairs.add(prev_pair)
            prev_pair = prev + actual
        prev2 = prev
        prev = actual
    return rule1 and rule2

nice_strings = 0
for s in strings:
    if isNicePart2(s):
        nice_strings += 1

print(nice_strings)
            