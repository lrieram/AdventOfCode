# -*- coding: utf-8 -*-

file_name = 'input.txt'
file = open(file_name,mode='r')

presents = []
for line in file:
    dimensions = line.split('x')
    presents.append([int(side) for side in dimensions])    

boxes = []
for present in presents:
    sides = []
    for i in range(3):
        side = present[i] * present[(i+1)%3]
        sides.append(side)
    boxes.append(sides)

total = 0
for box in boxes:
    paper = 0
    for side in box:
        paper += 2 * side
    paper += min(box)
    total += paper

total_ribbon = 0
for present in presents:
    ribbon = 0
    present.sort()
    ribbon += present[0] * 2 + present[1] * 2
    ribbon += present[0] * present[1] * present[2]
    total_ribbon += ribbon
    
#print(total)
print(total_ribbon)