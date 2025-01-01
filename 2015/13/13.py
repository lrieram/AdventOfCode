# -*- coding: utf-8 -*-
import numpy as np

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
happiness_indications = []
for line in file:
    happiness_indications.append(line.strip())
    
cant_guests = int((1 + np.sqrt(1 + 8 *len(happiness_indications)))/2)
    
matrix = np.zeros((cant_guests, cant_guests))

#In case input is not ordered

def getIndex(guest, guest_list):
    if not (guest in guest_list):
        guest_list.append(guest)
    return guest_list.index(guest)

guest_list = []
#Create the matrix of happiness
for happiness_indication in happiness_indications:
    happiness_indication = happiness_indication.split(' happiness units by sitting next to ')
    #[:-1] to remove the dot at the end
    guest2 = happiness_indication[1][:-1]
    happiness_indication = happiness_indication[0].split(' would ')
    guest1 = happiness_indication[0]
    happiness = happiness_indication[1]
    if 'gain' in happiness:
        happiness = int(happiness[5:])
    elif 'lose' in happiness:
        happiness = - int(happiness[5:])
    index_1 = getIndex(guest1, guest_list)
    index_2 = getIndex(guest2, guest_list)
    matrix[index_1, index_2] = happiness
  
def maxHappiness(happiness_matrix, guests_left, guest_order):
    #Assuming there are at least 2 guests
    #Last guest
    if len(guests_left) == 1:
        new_guest = guests_left[0]
        left_guest = guest_order[-1]
        rigth_guest = guest_order[0]
        happiness_change = 0
        happiness_change += happiness_matrix[left_guest, new_guest]
        happiness_change += happiness_matrix[rigth_guest, new_guest]
        happiness_change += happiness_matrix[new_guest, left_guest]
        happiness_change += happiness_matrix[new_guest, rigth_guest]
        return happiness_change
    else:
        max_change_happiness = - np.inf
        for new_guest in guests_left:
            new_guest_order = guest_order.copy()
            new_guest_order.append(new_guest)
            new_guests_left = guests_left.copy()
            new_guests_left.remove(new_guest)
            happiness_change = 0
            #If there is at least one guest on the table
            if len(guest_order) >= 1:
                happiness_change += happiness_matrix[guest_order[-1],new_guest]
                happiness_change += happiness_matrix[new_guest, guest_order[-1]]
            max_change_happiness = max(max_change_happiness, happiness_change + maxHappiness(happiness_matrix, new_guests_left, new_guest_order))
        return max_change_happiness
    
print(maxHappiness(matrix, [x for x in range(len(guest_list))], []))
#---------------------------- Part 2 ----------------------------

def maxHappinessList(happiness_matrix, guests_left, guest_order):
    #Assuming there are at least 2 guests
    #Last guest
    if len(guests_left) == 1:
        new_guest = guests_left[0]
        left_guest = guest_order[-1]
        rigth_guest = guest_order[0]
        happiness_change = 0
        happiness_change += happiness_matrix[left_guest, new_guest]
        happiness_change += happiness_matrix[rigth_guest, new_guest]
        happiness_change += happiness_matrix[new_guest, left_guest]
        happiness_change += happiness_matrix[new_guest, rigth_guest]
        new_guest_order = guest_order.copy()
        new_guest_order.append(new_guest)
        return happiness_change, new_guest_order
    else:
        max_change_happiness = - np.inf
        final_guest_order = []
        for new_guest in guests_left:
            new_guest_order = guest_order.copy()
            new_guest_order.append(new_guest)
            new_guests_left = guests_left.copy()
            new_guests_left.remove(new_guest)
            happiness_change = 0
            #If there is at least one guest on the table
            if len(guest_order) >= 1:
                happiness_change += happiness_matrix[guest_order[-1],new_guest]
                happiness_change += happiness_matrix[new_guest, guest_order[-1]]
            happiness_change_rest, guest_order_rest = maxHappinessList(happiness_matrix, new_guests_left, new_guest_order)
            if happiness_change_rest + happiness_change > max_change_happiness:
                max_change_happiness = happiness_change_rest + happiness_change
                final_guest_order = guest_order_rest
        return max_change_happiness, final_guest_order
    
max_happiness, final_order = maxHappinessList(matrix, [x for x in range(len(guest_list))], [])

final_happiness = -np.inf
for i in range(len(final_order)):
    happiness_change = 0
    #I sit between i and i+1
    #If its the "last one" I sit between i and 0
    next_index = (i+1) % len(final_order)
    happiness_change -= matrix[final_order[i], final_order[next_index]]
    happiness_change -= matrix[final_order[next_index], final_order[i]]
    final_happiness = max(final_happiness, max_happiness + happiness_change)
    
print(final_happiness)