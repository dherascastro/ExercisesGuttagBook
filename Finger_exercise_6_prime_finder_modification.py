# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 09:35:28 2022

@author: home
"""

# Test if an int > 2 is prime. If not, print smallest divisor
x = int(input('Enter an integer greater than 2: '))
largest_divisor = None
for guess in range (x-1, 1):
    if x % guess  == 0:
        largest_divisor = guess
        break
if largest_divisor != None:
    print ('Largest divisor of', x, 'is', largest_divisor)
else:
    print (x, 'is a prime number')