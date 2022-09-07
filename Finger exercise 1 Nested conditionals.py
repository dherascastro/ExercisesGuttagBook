# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

a = 0
b = 0
c = 0
Resultado: 0

a = 5
b = 3
c = 1
Resultado: 5

a = 1
b = 5
c = 3
Resultado: 5

a = 3
b = 1
c = 5
Resultado: 5

a = 5
b = 3
c = 8
Resultado: 5

a = 3
b = 5
c = 2
Resultado: 5

a = 3
b = 8
c = 6
Resultado: 3

a = 4
b = 1
c = 6
Resultado: 1

a = 4
b = 6
c = 3
Resultado: 3

a = 16
b = 12
c = 4
Resultado: 4

a = 44
b = 12
c = 34
Resultado: 12

a = 4
b = 6
c = 8
Resultado: 4
"""

a = 3
b = 1
c = 5

if (a%2 != 0 and b%2 != 0 and c%2 != 0):
    if (a>b):
        if (a>c):
            print (a)
        else:
            print (c)
    elif (b>c):
        print (b)
    else:
        print (c)
        
if (a%2 != 0 and b%2 != 0 and c%2 == 0):
    if (a>b):
        print (a)
    else:
        print (b)
        
if (a%2 == 0 and b%2 != 0 and c%2 != 0):
    if (b>c):
        print (b)
    else:
        print (c)
        
if (a%2 != 0 and b%2 == 0 and c%2 != 0):
    if (c>a):
        print (c)
    else:
        print (a)
        
if (a%2 != 0 and b%2 == 0 and c%2 == 0):
    print (a)
    
if (a%2 == 0 and b%2 != 0 and c%2 == 0):
    print (b)
    
if (a%2 == 0 and b%2 == 0 and c%2 != 0):
    print (c)
    
if (a%2 == 0 and b%2 == 0 and c%2 == 0):
    if (a<b):
        if (a<c):
            print (a)
        else:
            print (c)
    elif (b<c):
        print (b)
    else:
        print (c)