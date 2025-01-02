# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
deer_descriptions = []
for line in file:
    deer_descriptions.append(line.strip())

def getDeerNumbers(description):
    deer = description.split(' ')
    return (int(deer[3]), int(deer[6]), int(deer[13]))

deers = []
for deer_description in deer_descriptions:
    deers.append(getDeerNumbers(deer_description))
    
def distanceFlew(deer, seconds):
    distance = 0
    fly_speed = deer[0]
    fly_time = deer[1]
    rest_time = deer[2]
    #While there's still time
    while seconds >= 0:
        #Fly all the time that they can
        distance += fly_speed * min(fly_time, seconds)
        #Rest
        seconds -= (fly_time + rest_time)
    return distance

max_distance = 0
for deer in deers:
    max_distance = max(max_distance, distanceFlew(deer, 2503))
    
print(max_distance)
#---------------------------- Part 2 ----------------------------

points = [0] * len(deers)

for s in range(1, 2504):
    leader = []
    leader_distance = 0
    for i in range(len(deers)):
        distance = distanceFlew(deers[i], s) 
        if distance > leader_distance:
            leader_distance = distance
            leader = [i]
        elif distance == leader_distance:
            leader.append(i)
    for j in leader:
        points[j] += 1

print(max(points))
