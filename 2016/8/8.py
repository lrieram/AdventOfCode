# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
instructions = []
for line in file:
    instruction = line.strip().split()
    op = instruction[0]
    if op == 'rect':
        parameters = instruction[1].split('x')
        par1 = int(parameters[0])
        par2 = int(parameters[1])
    else:
        op += ' '+ instruction[1]
        par1 = int(instruction[2].split('=')[-1])
        par2 = int(instruction[-1])
    instructions.append((op, par1, par2))
    
screen = [[0] * 50 for _ in range(6)] 
    
def execute(instructions):
    for instruction in instructions:
        if instruction[0] == 'rect':
            for i in range(instruction[2]):
                for j in range(instruction[1]):
                    screen[i][j] = 1
        elif instruction[0] == 'rotate row':
            row = instruction[1]
            p = instruction[2]
            new_row = screen[row].copy()
            for i in range(50):
                new_row[(i+p)%50] = screen[row][i]
            screen[row] = new_row
        elif instruction[0] == 'rotate column':
            column = instruction[1]
            p = instruction[2]
            new_column = [0] * 6
            for i in range(6):
                new_column[(i+p)%6] = screen[i][column]
            for i in range(6):
                screen[i][column] = new_column[i]

execute(instructions)
print(sum([sum(x) for x in screen]))
#---------------------------- Part 2 ----------------------------

screen = [['-'] * 50 for _ in range(6)]

def draw(instructions):
    for instruction in instructions:
        if instruction[0] == 'rect':
            for i in range(instruction[2]):
                for j in range(instruction[1]):
                    screen[i][j] = '#'
        elif instruction[0] == 'rotate row':
            row = instruction[1]
            p = instruction[2]
            new_row = screen[row].copy()
            for i in range(50):
                new_row[(i+p)%50] = screen[row][i]
            screen[row] = new_row
        elif instruction[0] == 'rotate column':
            column = instruction[1]
            p = instruction[2]
            new_column = [0] * 6
            for i in range(6):
                new_column[(i+p)%6] = screen[i][column]
            for i in range(6):
                screen[i][column] = new_column[i]

draw(instructions)

for i in range(10):
    for j in range(6):
        print(screen[j][i*5:i*5+5])
    print()