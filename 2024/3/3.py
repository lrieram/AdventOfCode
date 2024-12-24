# -*- coding: utf-8 -*-
file_name = 'input.txt'
file = open(file_name,mode='r')

instructions = ''
for line in file:
    instructions += line


#Primera Parte
def totalSum(s):
    total = 0
    posiblesMuls = [x[:8] for x in s.split('mul(')]
    #print(posiblesMuls)
    
    for posibleMul in posiblesMuls:
        #print(posibleMul)
        sinParentesis = posibleMul.split(')')
        #print('sinParentesis = ', sinParentesis)
        if len(sinParentesis) == 1:
            #print('invalido')
            continue
        sinParentesis = sinParentesis[0]
        numeros = sinParentesis.split(',',1)
        #print('numeros = ', numeros)
        if len(numeros) != 2:
            #print('invalido')
            continue
        try:
            num1 = int(numeros[0])
            num2 = int(numeros[1])
        except:
            #print('invalido')
            continue
        else:
            #print('num1 = ', num1, 'num2 = ', num2)
            total += num1*num2
    return total
        
#print(totalSum(instructions))


#Segunda Parte
total = 0
mulEnable = instructions.split('do()')
withoutDont = [x.split("don't()")[0] for x in mulEnable]

for l in withoutDont:
    total += totalSum(l)
print(total)









        