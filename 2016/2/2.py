# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
numbers = []
for line in file:
    numbers.append(line.strip())
    
    
keypad = [[1,2,3],
          [4,5,6],
          [7,8,9]]

x = 1
y = 1

def move(direction, x, y):
    match direction:
        case 'U':
            y = max(0, y-1)
        case 'D':
            y = min(2, y+1)
        case 'R':
            x = min(2, x+1)
        case 'L':
            x = max(0, x-1)
    return x, y

for directions in numbers:
    for direction in directions:
        x, y = move(direction, x, y)
    print(keypad[y][x])
#---------------------------- Part 2 ----------------------------
print('--Part2--')
keypad = [[1],
          [2,3,4],
          [5,6,7,8,9],
          ['A', 'B', 'C'],
          ['D']]

x = 0
y = 2

def move2(direction, x, y):
    match direction:
        case 'U':
            match y:
                case 0:
                    y = 0
                case 1:
                    if x == 1:
                        y = 0
                        x = 0
                case 2:
                    if 1 <= x <= 3:
                        y = 1
                        x -= 1
                case _:
                    y -= 1
                    x += 1
        case 'D':
            match y:
                case 4:
                    y = 4
                case 3:
                    if x == 1:
                        y = 4
                        x = 0
                case 2:
                    if 1 <= x <= 3:
                        y = 3
                        x -= 1
                case _:
                    y += 1
                    x += 1
        case 'R':
            x = min(len(keypad[y]) - 1, x+1)
        case 'L':
            x = max(0, x-1)
    return x, y

for directions in numbers:
    for direction in directions:
        x, y = move2(direction, x, y)
    print(keypad[y][x])
    