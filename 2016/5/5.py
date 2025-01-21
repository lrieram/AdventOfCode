# -*- coding: utf-8 -*-
import hashlib

door_id = 'ojvtpuvg'

pw = ''
i = 0
while len(pw) < 8:
    complete_id = door_id + str(i)
    hash_result = hashlib.md5(complete_id.encode())
    hash_result = hash_result.hexdigest()
    if hash_result[:5] == '00000':
        pw += hash_result[5]
    i += 1

print(pw)
#---------------------------- Part 2 ----------------------------

pw = ['-'] * 8
i = 0
print(pw)
while '-' in pw:
    complete_id = door_id + str(i)
    hash_result = hashlib.md5(complete_id.encode())
    hash_result = hash_result.hexdigest()
    if hash_result[:5] == '00000':
        try:
            int(hash_result[5])
        except:
            i += 1
            continue
        else:
            index = int(hash_result[5])
            if index < 8:
                if pw[index] == '-':
                    pw[index] = hash_result[6]       
    i += 1
    
print(pw)