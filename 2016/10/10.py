# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

bots = {}

def receiveValue(bot_ID, value):
    bot = bots.get(bot_ID, (False, False))
    if type(bot[0]) != int:
        bot = (value, False)            
    elif type(bot[1]) != int:
        bot = (bot[0], value)
    bots[bot_ID] = bot

#Read file
instructions = []
for line in file:
    line = line.strip().split()
    if line[0] == 'value':
        receiveValue(int(line[5]), int(line[1]))
    else:
        instructions.append(line)
        
outputs = {}
        
for instruction in instructions:
    bot = bots.get(int(instruction[1]), (False, False))
    if type(bot[1]) != int:
        print(instruction[1])
        print("no tiene numeros")
    else:
        min_value = min(bot)
        max_value = max(bot)
        if instruction[5] == 'output':
            outputs[int(instruction[6])] = min_value
        else:
            receiveValue(int(instruction[6]), min_value)
        if instruction[10] == 'output':
            outputs[int(instruction[11])] = min_value
        else:
            receiveValue(int(instruction[11]), min_value)

        

#---------------------------- Part 2 ----------------------------