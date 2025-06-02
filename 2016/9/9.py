# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
strings = []
for line in file:
    strings.append(line.strip())
    
text = ''.join(strings)

def decompress(text):
    decompressed = ''
    i = 0
    while i < len(text):
        new_char = text[i]
        if new_char != '(':
            decompressed += new_char
            i += 1
        else:
            j = i + text[i:].find(')')
            marker = text[i+1:j].split('x')
            seq = text[j+1:j+1+int(marker[0])]
            decompressed += seq * int(marker[1])
            i = j+1+int(marker[0])
    return decompressed

print(len(decompress(text)))
#---------------------------- Part 2 ----------------------------

def lenDecompressV2(s):
    if '(' not in s:
        return len(s)
    res = 0
    while '(' in s:
        res += s.find('(')
        s = s[s.find('('):]
        marker = s[1:s.find(')')].split('x')
        s = s[s.find(')') + 1:]
        res += lenDecompressV2(s[:int(marker[0])]) * int(marker[1])
        s = s[int(marker[0]):]
    res += len(s)
    return res

print(lenDecompressV2(text))