# -*- coding: utf-8 -*-

#open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#read file
instructions = ''
for line in file:
    instructions += line.strip()


def totalSum(s):
    total = 0
    #a valid mul has, at max, two 3-digit numbers, a ',' and a ')'
    posiblesMuls = [x[:8] for x in s.split('mul(')]
    
    for posibleMul in posiblesMuls:
        wo_parentheses = posibleMul.split(')')
        if len(wo_parentheses) == 1:  
            #if the parentheses is not closed
            continue
        #remove the rest
        wo_parentheses = wo_parentheses[0]
        numbers = wo_parentheses.split(',',1)
        if len(numbers) != 2:
            #abscent or ilegal coma
            continue
        try:
            num1 = int(numbers[0])
            num2 = int(numbers[1])
        except:
            continue
        else:
            total += num1*num2
    return total
        
#print(totalSum(instructions))

#---------------------------- Part 2 ----------------------------

total = 0
mulEnable = instructions.split('do()')
withoutDont = [x.split("don't()")[0] for x in mulEnable]

for l in withoutDont:
    total += totalSum(l)
print(total)









        