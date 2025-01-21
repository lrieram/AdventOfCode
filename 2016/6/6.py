# -*- coding: utf-8 -*-
from collections import Counter

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
strings = []
for line in file:
    strings.append(line.strip())
    
def recover(messages):
    zipped = zip(*messages)
    return ''.join(Counter(message).most_common(1)[0][0] for message in zipped)

print(recover(strings))
#---------------------------- Part 2 ----------------------------

def recover2(messages):
    zipped = zip(*messages)
    return ''.join(Counter(message).most_common()[-1][0] for message in zipped)

print(recover2(strings))