# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:47:45 2022

@author: home
"""
"""
Write a program that examines three variables—
x, y, and z—and prints the largest odd number among them. If none
of them are odd, it should print the smallest value of the three.
You can attack this exercise in a number of ways. There are eight
separate cases to consider: they are all odd (one case), exactly two of
them are odd (three cases), exactly one of them is odd (three cases),
or none of them is odd (one case). So, a simple solution would
involve a sequence of eight if statements, each with a single print
statement:
if x%2 != 0 and y%2 != 0 and z%2 != 0:
print(max(x, y, z))
if x%2 != 0 and y%2 != 0 and z%2 == 0:
print(max(x, y))
if x%2 != 0 and y%2 == 0 and z%2 != 0:
print(max(x, z))
if x%2 == 0 and y%2 != 0 and z%2 != 0:
print(max(y, z))
if x%2 != 0 and y%2 == 0 and z%2 == 0:
print(x)
if x%2 == 0 and y%2 != 0 and z%2 == 0:
print(y)
if x%2 == 0 and y%2 == 0 and z%2 != 0:
print(z)
if x%2 == 0 and y%2 == 0 and z%2 == 0:
print(min(x, y, z))
That gets the job done, but is rather cumbersome. Not only is it
16 lines of code, but the variables are repeatedly tested for oddness.
The following code is both more elegant and more efficient:
answer = min(x, y, z)
if x%2 != 0:
answer = x
if y%2 != 0 and y > answer:
answer = y
if z%2 != 0 and z > answer:
answer = z
print(answer)
"""
"""
a = 1
b = 1
c = 1
Resultado: 1
"""
a = 0
b = 4
c = 2
mayor_impar = 0
menor_par = 1000000

if (a%2 != 0):
    if (mayor_impar<a):
        mayor_impar = a
elif (menor_par>a):
    menor_par = a
    
if (b%2 != 0):
    if (mayor_impar<b):
        mayor_impar = b
elif (menor_par>b):
    menor_par = b
    
if (c%2 != 0):
    if (mayor_impar<c):
        mayor_impar = c
elif (menor_par>c):
    menor_par = c
    
if (mayor_impar != 0):
    print (mayor_impar)
else:
    print (menor_par)