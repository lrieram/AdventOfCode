# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
instructions = []
for line in file:
    instructions = line.strip().split(', ')
    
position = (0, 0)
#in order: North, East, South, West
facing = 0
def turn(direction, facing):
    if direction == 'R':
        return (facing + 1) % 4
    elif direction == 'L':
        return (facing - 1) % 4
    else:
        print('Error')

def move(position, facing, steps):
    match facing:
        case 0:
            x_multiplier = 0
            y_multiplier = 1
        case 1:
            x_multiplier = 1
            y_multiplier = 0
        case 2:
            x_multiplier = 0
            y_multiplier = -1
        case 3:
            x_multiplier = -1
            y_multiplier = 0
    new_x = position[0] + steps * x_multiplier
    new_y = position[1] + steps * y_multiplier
    return (new_x, new_y)

for instruction in instructions:
    direction = instruction[0]
    steps = int(instruction[1:])
    facing = turn(direction, facing)
    position = move(position, facing, steps)
    
print(sum([abs(x) for x in position]))
    
#---------------------------- Part 2 ----------------------------


def part2(instructions):
    position = (0,0)
    visited = [(0,0)]
    facing = 0
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        facing = turn(direction, facing)
        for _ in range(steps):
            position = move(position, facing, 1)
            if position in visited:
                return sum([abs(x) for x in position])
            visited.append(position)

print(part2(instructions))