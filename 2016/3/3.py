# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
triangles = []
for line in file:
    triangles.append([int(side) for side in line.strip().split()])
    
    
def isValid(triangle):
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True
    
count = 0
for triangle in triangles:
    if isValid(triangle):
        count += 1

print(count)
#---------------------------- Part 2 ----------------------------

file_name = 'input.txt'
file = open(file_name,mode='r')

triangles = []
line = file.readline()
while line:
    a = line.strip().split()
    line = file.readline()
    b = line.strip().split()
    line = file.readline()
    c = line.strip().split()
    for i in range(3):
        triangles.append([int(a[i]), int(b[i]), int(c[i])])
    line = file.readline()

count = 0
for triangle in triangles:
    if isValid(triangle):
        count += 1

print(count)