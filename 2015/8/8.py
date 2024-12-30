# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
strings = []
for line in file:
    strings.append(line.strip())
    
char_codes = 0
char_strings = 0
for s in strings:
    #the first character is a "
    i = 1
    #the first and last " doesn't count to the string but does to the code
    #using new variables for testing purposes
    char_code = 2
    char_string = 0
    #the last character is also a "
    while i < len(s)-1:
        if s[i] != '\\':
            char_code += 1
            char_string += 1
            i += 1
        else:
            if s[i+1] in ['"', '\\']:
                char_code += 2
                char_string += 1
                i += 2
            elif s[i+1] == 'x':
                char_code += 4
                char_string += 1
                i += 4
    #print(s, char_code, char_string)
    char_codes += char_code
    char_strings += char_string
    
#print(char_codes - char_strings)
            
#---------------------------- Part 2 ----------------------------

char_codes = 0
char_encodeds = 0

for s in strings:
    #the first character is a "
    i = 1
    #the first and last " need "\" and \"" to encode
    char_code = 2
    char_encoded = 6
    while i < len(s)-1:
        if s[i] in ['\\', '"']:
            char_code += 1
            char_encoded += 2
        else:
            char_code += 1
            char_encoded += 1
        i += 1
    #print(s, char_encoded, char_code)
    char_codes += char_code
    char_encodeds += char_encoded

print(char_encodeds - char_codes)
    
    