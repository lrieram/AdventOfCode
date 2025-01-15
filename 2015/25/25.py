# -*- coding: utf-8 -*-


row = 2947
column = 3029

start_number = 20151125  

def nextNumber(number):
    n = number * 252533
    return n % 33554393

#The number that I want is in the 2947 + 3029 - 1 = 5975th diagonal
#The nth diagonal has n numbers
#In the first 5974 diagonal there are 5974*5975/2 = 17847325  numbers
#Then I need to "advance" 3028 columns to reach the number  

number = start_number
for _ in range(17847325+3028):
    number = nextNumber(number)

print(number)
#---------------------------- Part 2 ----------------------------