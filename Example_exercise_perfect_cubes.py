# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 09:02:26 2022

@author: home
"""

#Find the cube rootof a perfect cube

x = int(input('Enter an integer: '))
ans = 0

while ans**3 < abs (x):
    ans = ans + 1
    #print ('Value of the decrementing function abs (x) - ans**3 is', 
           #abs (x) - ans**3)
    
if ans**3 != abs (x):
    print (x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print ('Cube root of' , x, 'is', ans)