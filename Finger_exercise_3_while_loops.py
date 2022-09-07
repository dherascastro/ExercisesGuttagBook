# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:18:02 2022

@author: home
"""
"""
Practicing while loops

Replace the comment in the following code with a
while loop.

num_x = int(input('How many times should I print the letter X? '))
to_print = ''
#concatenate X to to_print num_x times
print(to_print)
"""

to_print = ' '
num_x = int (input ('How many times should I print the letter X?'))

counter = 0
while (counter < abs (num_x)):
    to_print = to_print + 'X'
    counter = counter + 1
#concatenate X to to_print num_x times
print (to_print)