# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 22:06:42 2022

@author: home
"""
"""
(625, 5, 0.001)
Resultado: 4.0 is close to the log base 5 of 625

(64, 2, 0.001)
Resultado: 6.0 is close to the log base 2 of 64

(243, 3, 0.001)
Resultado: 5.0 is close to the log base 3 of 243

(1, 1, 0.001)
Resultado: 0.0 is close to the log base 1 of 1
"""

def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
    x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon
    of x."""

    #Find lower_bound on ans
    lower_bound = 0
    while (base ** lower_bound < x):
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1

    #Perform bisection search
    ans = (high + low) / 2.
    while abs (base ** ans - x) >= epsilon:
        if (base ** ans < x):
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
        
    print (f' {ans} is close to the log base {base} of {x}')
    
log (1, 1, 0.001)