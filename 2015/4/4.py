# -*- coding: utf-8 -*-
import hashlib

key = 'iwrupvqb'

i = 1
first_digits = ''
while first_digits != '00000':    
    code = hashlib.md5((key+str(i)).encode())
    first_digits = code.hexdigest()[:5]
    i += 1

#print(i-1) 

#---------------------------- Part 2 ----------------------------

i = 1
first_digits = ''
while first_digits != '000000':    
    code = hashlib.md5((key+str(i)).encode())
    first_digits = code.hexdigest()[:6]
    i += 1

print(i-1) 