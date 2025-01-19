# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')


#Read file
rooms = []
for line in file:
    room = line.strip().split('-')
    name = room[:-1]
    id_checksum = room[-1].split('[')
    room_id = int(id_checksum[0])
    chksum = id_checksum[1][:-1]
    rooms.append((name, room_id, chksum))

def isValid(room):
    name = ''.join(room[0])
    chksum = room[2]
    #Check order of checksum
    for i in range(4):
        if name.count(chksum[i]) < name.count(chksum[i+1]) or (name.count(chksum[i]) == name.count(chksum[i+1]) and chksum[i] > chksum[i+1]):
            return False
    #Assuming the right order, only need  to compare with the last character
    for c in name:
        if c not in chksum:
            if name.count(c) > name.count(chksum[-1]) or (name.count(c) == chksum[-1] and chksum[-1] > c):
                return False
    return True

total = 0
for room in rooms:
    if isValid(room):
        total += room[1]
        
print(total)
#---------------------------- Part 2 ----------------------------

def decrypt(name, room_id):
    decrypted = [''.join([chr(ord('a') + (ord(x) - ord('a') + room_id)%26) for x in word]) for word in name]
    decrypted_name = ''
    for word in decrypted:
        decrypted_name += word + ' '
    return decrypted_name[:-1]

for room in rooms:
    if isValid(room):
        decrypted = decrypt(room[0], room[1])
        if 'north' in decrypted:
            print(room[1])