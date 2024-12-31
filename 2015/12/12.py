# -*- coding: utf-8 -*-
import json

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
inp = '' 
for line in file:
    inp += line.strip()


doc = json.loads(inp)

def valueOfElement(element):
    
    if type(element) == int:
        return element
    elif type(element) == list:
        value = 0
        for e in element:
            value += valueOfElement(e)
        return value
    elif type(element) == dict:
        value = 0
        for e in element.values():
            value += valueOfElement(e)
        return value
    else:
        return 0



#print(valueOfElement(doc))
    
#---------------------------- Part 2 ----------------------------

def valueWithoutRed(element):
    
    if type(element) == int:
        return element
    elif type(element) == list:
        value = 0
        for e in element:
            value += valueWithoutRed(e)
        return value
    elif type(element) == dict:
        value = 0
        for e in element.values():
            if e == "red":
                return 0
            value += valueWithoutRed(e)
        return value
    else:
        return 0
    
print(valueWithoutRed(doc))