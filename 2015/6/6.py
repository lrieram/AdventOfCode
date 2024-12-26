# -*- coding: utf-8 -*-
import numpy as np

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
instructions = []
for line in file:
    instructions.append(line.strip())
    
lights = np.zeros((1000,1000))

def turnOff(lights, corners):
    dl_corner_s = corners[0].split(',')
    ur_corner_s = corners[1].split(',')
    dl_corner = [int(x) for x in dl_corner_s]
    ur_corner = [int(x) for x in ur_corner_s]
    #+1 is to make it inclusive
    for i in range(dl_corner[0],ur_corner[0]+1):
        for j in range(dl_corner[1],ur_corner[1]+1):
            lights[i,j] = 0
            
def turnOn(lights, corners):
    dl_corner_s = corners[0].split(',')
    ur_corner_s = corners[1].split(',')
    dl_corner = [int(x) for x in dl_corner_s]
    ur_corner = [int(x) for x in ur_corner_s]
    #+1 is to make it inclusive
    for i in range(dl_corner[0],ur_corner[0]+1):
        for j in range(dl_corner[1],ur_corner[1]+1):
            lights[i,j] = 1
            
def toggle(lights, corners):
    dl_corner_s = corners[0].split(',')
    ur_corner_s = corners[1].split(',')
    dl_corner = [int(x) for x in dl_corner_s]
    ur_corner = [int(x) for x in ur_corner_s]
    #+1 is to make it inclusive
    for i in range(dl_corner[0],ur_corner[0]+1):
        for j in range(dl_corner[1],ur_corner[1]+1):
            lights[i,j] = (lights[i,j]+1)%2
            
for instruction in instructions:
    if instruction[:8] == 'turn off':
        corners = instruction[8:].split('through')
        turnOff(lights, corners)
    elif instruction[:7] == 'turn on':
        corners = instruction[7:].split('through')
        turnOn(lights, corners)
    elif instruction[:6] == 'toggle':
        corners = instruction[6:].split('through')
        toggle(lights, corners)

print(sum(sum(lights)))
        
#---------------------------- Part 2 ----------------------------

lights = np.zeros((1000,1000))

def turnOffPart2(lights, corners):
    dl_corner_s = corners[0].split(',')
    ur_corner_s = corners[1].split(',')
    dl_corner = [int(x) for x in dl_corner_s]
    ur_corner = [int(x) for x in ur_corner_s]
    #+1 is to make it inclusive
    for i in range(dl_corner[0],ur_corner[0]+1):
        for j in range(dl_corner[1],ur_corner[1]+1):
            lights[i,j] = max(0,lights[i,j]-1)
            
def turnOnPart2(lights, corners):
    dl_corner_s = corners[0].split(',')
    ur_corner_s = corners[1].split(',')
    dl_corner = [int(x) for x in dl_corner_s]
    ur_corner = [int(x) for x in ur_corner_s]
    #+1 is to make it inclusive
    for i in range(dl_corner[0],ur_corner[0]+1):
        for j in range(dl_corner[1],ur_corner[1]+1):
            lights[i,j] = lights[i,j]+1
            
def togglePart2(lights, corners):
    dl_corner_s = corners[0].split(',')
    ur_corner_s = corners[1].split(',')
    dl_corner = [int(x) for x in dl_corner_s]
    ur_corner = [int(x) for x in ur_corner_s]
    #+1 is to make it inclusive
    for i in range(dl_corner[0],ur_corner[0]+1):
        for j in range(dl_corner[1],ur_corner[1]+1):
            lights[i,j] = lights[i,j]+2
            
for instruction in instructions:
    if instruction[:8] == 'turn off':
        corners = instruction[8:].split('through')
        turnOffPart2(lights, corners)
    elif instruction[:7] == 'turn on':
        corners = instruction[7:].split('through')
        turnOnPart2(lights, corners)
    elif instruction[:6] == 'toggle':
        corners = instruction[6:].split('through')
        togglePart2(lights, corners)

print(sum(sum(lights)))
  