# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:38:17 2022

@author: home
"""

"""
Practicing while loops

Write a program that asks the user to input 10
integers, and then prints the largest odd number that was entered. If
no odd number was entered, it should print a message to that effect.
"""

largest_odd = -1000000

counter = 0
while (counter<10):
    number = int(input('Enter any integer number'))
    if (number % 2 != 0 and number > largest_odd):
        largest_odd = number
    counter = counter + 1
    
if largest_odd == -1000000:
    print ('No odd numbers were entered, so there is no largest odd number')
else:
    print (largest_odd)