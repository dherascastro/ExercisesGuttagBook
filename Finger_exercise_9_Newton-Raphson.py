# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:34:01 2022

@author: home
"""
"""
Add some code to the implementation of
Newton–Raphson that keeps track of the number of iterations used
to find the root. Use that code as part of a program that compares the
efficiency of Newton–Raphson and bisection search. (You should
discover that Newton–Raphson is far more efficient.)
"""
# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0


k = float(input('Enter a positive integer: '))
epsilon = 0.01 

num_guesses_newton_raphson = 0
guess = k/2
while abs(guess**2 - k) >= epsilon:
    num_guesses_newton_raphson += 1
    guess = guess - (((guess**2) - k)/(2*guess))

print('Square root of', k, 'is about', guess)
print('Guesses needed with Newton-Raphson method:', num_guesses_newton_raphson)



num_guesses_bisection = 0
high = max (0, k)
low = 0
ans = (low + high)/2

while abs (ans ** 2 - k) >= epsilon:
    num_guesses_bisection += 1
    if ans ** 2 > k:
        high = ans
    else:
        low = ans
    ans = (low + high)/2


print('Square root of', k, 'is about', ans)
print('Guesses needed with bisection method:', num_guesses_bisection)
