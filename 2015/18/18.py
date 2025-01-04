# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
lights = []
for line in file:
    lights.append(line.strip())
    
    
def neighbors(i, j, n, m):
    res = []
    positions = [(i-1, j-1), (i, j-1), (i+1, j-1),
                 (i-1, j), (i+1, j),
                 (i-1, j+1), (i, j+1), (i+1, j+1)]
    for (k, l) in positions:
        if 0 <= k < n and 0 <= l < m:
            res.append((k, l))
    return res
    

def neighborsLights(lights, i, j):
    neighborhood = neighbors(i, j, len(lights), len(lights[i]))
    n = 0
    for pos in neighborhood:
        if lights[pos[0]][pos[1]] == '#':
            n += 1
    return n
    
def nextStepSingle(lights, i, j):
    neighbors = neighborsLights(lights, i, j)
    if lights[i][j] == '#':
        if neighbors == 2 or neighbors == 3:
            return '#'
        else:
            return '.'
    else:
        if neighbors == 3:
            return '#'
        else:
            return '.'
    
def nextStep(lights):
    next_lights = []
    for i in range(len(lights)):
        new_row = ''
        for j in range(len(lights[0])):
            new_row += nextStepSingle(lights, i, j)
        next_lights.append(new_row)
    return next_lights

def lightsOn(lights):
    total = 0
    for row in lights:
        for light in row:
            if light == '#':
                total += 1
    return total

next_light_configuration = lights.copy()
for _ in range(100):
    next_light_configuration = nextStep(next_light_configuration)
    
print(lightsOn(next_light_configuration))
#---------------------------- Part 2 ----------------------------

def nextStepFixedCorners(lights):
    next_lights = []
    for i in range(len(lights)):
        new_row = ''
        for j in range(len(lights[0])):
            new_row += nextStepSingle(lights, i, j)
        if i == 0 or i == (len(lights) - 1):
            new_row = '#' + new_row [1:-1] + '#'
        next_lights.append(new_row)
    return next_lights
    
next_light_configuration = lights
#Turn on the corners
next_light_configuration[0] = '#' + next_light_configuration[0][1:-1] + '#'
next_light_configuration[len(lights) - 1] = '#' + next_light_configuration[len(lights) - 1][1:-1] + '#'

for _ in range(100):
    next_light_configuration = nextStepFixedCorners(next_light_configuration)
    
print(lightsOn(next_light_configuration))