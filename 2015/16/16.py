# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
aunts = []
for line in file:
    aunt_data = line.strip().split(' ')
    aunt = {}
    #In case there's different amounts of features for aunt
    i = 2
    while i < len(aunt_data):
        #[:-1] to remove the :
        feature = aunt_data[i][:-1]
        if i != len(aunt_data)-2:
            #[:-1] to remove the ,
            amount = int(aunt_data[i+1][:-1])
        else:
            amount = int(aunt_data[i+1])
        aunt[feature] = amount
        i += 2
    aunts.append(aunt)
    
mfcsam = {'children': 3,
          'cats': 7,
          'samoyeds': 2,
          'pomeranians': 3,
          'akitas': 0,
          'vizslas': 0,
          'goldfish': 5,
          'trees': 3,
          'cars': 2,
          'perfumes': 1}
    
#Assuming there's only 1 aunt sue that match
for i in range(len(aunts)):
    correct_sue = True
    sue = aunts[i]
    for feature in sue:
        if sue.get(feature) != mfcsam.get(feature):
            correct_sue = False
    if correct_sue:
        #i+1 because aunts are numbered from 1 to 500
        print(i+1)
        


#---------------------------- Part 2 ----------------------------


for i in range(len(aunts)):
    correct_sue = True
    sue = aunts[i]
    for feature in sue:
        if feature in ['trees', 'cats']:
            if sue.get(feature) <= mfcsam.get(feature):
                correct_sue = False
        elif feature in ['pomeranians', 'goldfish']:
            if sue.get(feature) >= mfcsam.get(feature):
                correct_sue = False
        else:
            if sue.get(feature) != mfcsam.get(feature):
                correct_sue = False
    if correct_sue:
        #i+1 because aunts are numbered from 1 to 500
        print(i+1)