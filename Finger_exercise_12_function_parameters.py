# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 08:26:23 2022

@author: home
"""
"""
Write a function mult that accepts either one or
two ints as arguments. If called with two arguments, the function
prints the product of the two arguments. If called with one argument,
it prints that argument.
"""

def mult (int1, int2 = 1):
    return int1 * int2
print (mult (3, 4))