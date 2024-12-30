# -*- coding: utf-8 -*-
import numpy as np
#The input is small so I can use simple recursion

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
distances = []
for line in file:
    distances.append(line.strip())
    
cant_cities = int((1 + np.sqrt(1 + 8 *len(distances)))/2)
    
matrix = np.zeros((cant_cities, cant_cities))

#In case input is not ordered

def getIndex(city, city_list):
    if not (city in city_list):
        city_list.append(city)
    return city_list.index(city)

city_list = []
#Create the matrix of distances
for distance_line in distances:
    distance_args = distance_line.split(' = ')
    distance = int(distance_args[1])
    cities = distance_args[0].split(' to ')
    index_0 = getIndex(cities[0], city_list)
    index_1 = getIndex(cities[1], city_list)
    matrix[index_0, index_1] = distance
    matrix[index_1, index_0] = distance
    
    
def minTravelTime(distances, cities_to_visit, last_city):
    #Already visited all cities
    if len(cities_to_visit) == 0:
        return 0
    else:
        if last_city == -1:
            res = np.inf
            for city in cities_to_visit:
                cities_rest = cities_to_visit.copy()
                cities_rest.remove(city)
                travel_time = minTravelTime(distances, cities_rest, city)
                res = min(res, travel_time)
            return res
        else:
            res = np.inf
            for city in cities_to_visit:
                cities_rest = cities_to_visit.copy()
                cities_rest.remove(city)
                travel_time = minTravelTime(distances, cities_rest, city)
                time_to_city = distances[last_city, city]
                res = min(res, travel_time + time_to_city)
            return res
                

print(minTravelTime(matrix, [x for x in range(cant_cities)], -1))
#---------------------------- Part 2 ----------------------------

def maxTravelTime(distances, cities_to_visit, last_city):
    #Already visited all cities
    if len(cities_to_visit) == 0:
        return 0
    else:
        if last_city == -1:
            res = 0
            for city in cities_to_visit:
                cities_rest = cities_to_visit.copy()
                cities_rest.remove(city)
                travel_time = maxTravelTime(distances, cities_rest, city)
                res = max(res, travel_time)
            return res
        else:
            res = 0
            for city in cities_to_visit:
                cities_rest = cities_to_visit.copy()
                cities_rest.remove(city)
                travel_time = maxTravelTime(distances, cities_rest, city)
                time_to_city = distances[last_city, city]
                res = max(res, travel_time + time_to_city)
            return res
        
print(maxTravelTime(matrix, [x for x in range(cant_cities)], -1))