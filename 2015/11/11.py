# -*- coding: utf-8 -*-

start = 'cqjxjnds'
    
def nextPassword(pw):
    j = 7
    end = ''
    while j != 0 and pw[j] == 'z':
        end += 'a'
        j -= 1
        
    #In case pw = zzzzzzzz
    if j == 0:
        if pw[j] == 'z':
            return 'aaaaaaaa'
    
    return pw[0:j] + chr(ord(pw[j]) + 1) + end

def doesntHasInvalidChar(pw):
    invalid_chars = ['i', 'o', 'l']
    for c in pw:
        if c in invalid_chars:
            return False
    return True

def increasingRule(pw):
    last_char = ''
    consecutive = 0
    for c in pw:
        if last_char and ord(c) == ord(last_char) + 1:
            consecutive += 1
            if consecutive >= 2:
                return True
        else:
            consecutive = 0
        last_char = c
    return False

def pairsRule(pw):
    pairs = 0
    last_char = ''
    for c in pw:
        if last_char == c:
            pairs += 1
            last_char = ''
        else:
            last_char = c
    return pairs >= 2

def isValid(pw):
    return doesntHasInvalidChar(pw) and increasingRule(pw) and pairsRule(pw)

next_pw = nextPassword(start)
while not isValid(next_pw):
    next_pw = nextPassword(next_pw)

#print(next_pw)
    
#---------------------------- Part 2 ----------------------------

next_pw = nextPassword(next_pw)
while not isValid(next_pw):
    next_pw = nextPassword(next_pw)

print(next_pw)