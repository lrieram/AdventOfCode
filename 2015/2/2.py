# -*- coding: utf-8 -*-

#open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#read file
presents_dimensions = []
for line in file:
    dimensions = line.strip().split('x')
    presents_dimensions.append([int(side) for side in dimensions])    

#a box has 3 side sizes
boxes = []
for present in presents_dimensions:
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

#print(total)

#---------------------------- Part 2 ----------------------------

total_ribbon = 0
for present in presents_dimensions:
    ribbon = 0
    present.sort()
    ribbon += present[0] * 2 + present[1] * 2
    ribbon += present[0] * present[1] * present[2]
    total_ribbon += ribbon
    
print(total_ribbon)