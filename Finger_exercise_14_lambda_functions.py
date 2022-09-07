# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 10:54:39 2022

@author: home
"""
"""
Write a lambda expression that has two numeric
parameters. If the second argument equals zero, it should return
None. Otherwise it should return the value of dividing the first
argument by the second argument. Hint: use a conditional
expression.
"""

save = lambda x, y : x / y if y != 0 else None
print (save (x = 2, y = 8))
