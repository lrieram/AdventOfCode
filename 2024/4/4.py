# -*- coding: utf-8 -*-

file_name = 'input.txt'
file = open(file_name,mode='r')

m = []
for line in file:
    m.append(line.strip())
    
def findUp(m, i, j):
    return m[i-1][j]=='M' and m[i-2][j]=='A' and m[i-3][j]=='S' 
    
def findDown(m, i, j):
    return m[i+1][j]=='M' and m[i+2][j]=='A' and m[i+3][j]=='S'
    
def findLeft(m, i, j):
    return m[i][j-1]=='M' and m[i][j-2]=='A' and m[i][j-3]=='S'

def findRigth(m, i, j):
    return m[i][j+1]=='M' and m[i][j+2]=='A' and m[i][j+3]=='S'

def findUpLeft(m, i, j):
    return m[i-1][j-1]=='M' and m[i-2][j-2]=='A' and m[i-3][j-3]=='S'

def findUpRigth(m, i, j):
    return m[i-1][j+1]=='M' and m[i-2][j+2]=='A' and m[i-3][j+3]=='S'

def findDownLeft(m, i, j):
    return m[i+1][j-1]=='M' and m[i+2][j-2]=='A' and m[i+3][j-3]=='S'

def findDownRigth(m, i, j):
    return m[i+1][j+1]=='M' and m[i+2][j+2]=='A' and m[i+3][j+3]=='S'


total = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]=='X' and i>=3:
            if findUp(m,i,j):
                #print('Up en i: ',i,' j: ',j)
                total += 1
            if j>=3:
                if findUpLeft(m,i,j):
                    #print('UpLeft en i: ',i,' j: ',j)
                    total += 1
            if j<len(m[i])-3:
                if findUpRigth(m,i,j):
                    #print('UpRigth en i: ',i,' j: ',j)
                    total += 1
        if m[i][j]=='X' and i<len(m)-3:
            if findDown(m,i,j):
                #print('Down en i: ',i,' j: ',j)
                total += 1
            if j>=3:
                if findDownLeft(m,i,j):
                    #print('DownLeft en i: ',i,' j: ',j)
                    total += 1
            if j<len(m[i])-3:
                if findDownRigth(m,i,j):
                    #print('DownRigth en i: ',i,' j: ',j)
                    total += 1
        if m[i][j]=='X' and j>=3:
            if findLeft(m,i,j):
                #print('Left en i: ',i,' j: ',j)
                total += 1
        if m[i][j]=='X' and j<len(m[i])-3:
            if findRigth(m,i,j):
                #print('Rigth en i: ',i,' j: ',j)
                total += 1

def findMAS(m,i,j):
    mas = 0
    if m[i-1][j-1] == 'M' and m[i+1][j+1] == 'S':
        mas += 1
    if m[i-1][j+1] == 'M' and m[i+1][j-1] == 'S':
        mas += 1
    if m[i+1][j-1] == 'M' and m[i-1][j+1] == 'S':
        mas += 1
    if m[i+1][j+1] == 'M' and m[i-1][j-1] == 'S':
        mas += 1
    return mas == 2

total = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == 'A' and i>0 and i<len(m)-1 and j>0 and j<len(m[i])-1:
            if findMAS(m,i,j):
                total += 1
print(total)