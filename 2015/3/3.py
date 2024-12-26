# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
indications = ''
for line in file:
    indications += line.strip()
    
    
def newPosition(old_position, move):
    if move == '<':
        movement = (-1, 0)
    elif move == '>':
        movement = (1, 0)
    elif move == '^':
        movement = (0, 1)
    elif move == 'v':
        movement = (0, -1)
    else: #invalid move
        movement = (0, 0)
    return (old_position[0] + movement[0], old_position[1] + movement[1])


visited = set()
position = (0, 0)
visited.add(position)
for move in indications:
    position = newPosition(position, move)
    visited.add(position)
    
#print(len(visited))

#---------------------------- Part 2 ----------------------------

santa_pos = (0, 0)
robo_santa_pos = (0, 0)
santas_turn = True
visited = set()

for move in indications:
    if santas_turn:
        santa_pos = newPosition(santa_pos, move)
        visited.add(santa_pos)
        santas_turn = False
    else:
        robo_santa_pos = newPosition(robo_santa_pos, move)
        visited.add(robo_santa_pos)
        santas_turn = True

print(len(visited))

