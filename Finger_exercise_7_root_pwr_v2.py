# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 13:49:33 2022

@author: home
"""
"""
125
Resultado: 5 to the power of 3 equals 125

126
Resultado: There is no root, pwr such that root ** pwr = 126

64
Resultado: 8 to the power of 2 equals 64

128
Resultado: There is no root, pwr such that root ** pwr = 128

256
Resultado: 16 to the power of 2 equals 256
"""

"""
Practicing (nested) loops. El programa siempre consigue la combinación de
pwr y root en la que root tiene el mayor valor posible para el caso en 
cuestión. Si el orden en el que aparecen los bucles estuviera invertido,
es decir, que el bucle pwr root estuviera dentro del bucle root, entonces
siempre aparecería el menor valor posible para root (y el mayor posible para
power). En esta versión, se han eliminado los breaks para incluir los
requerimientos para salir del bucle en la propia condición del bucle. Se ha
cambiado el bucle for a bucle while.

Write a program that asks the user to enter an
integer (x) and prints two integers, root and pwr, such that 1 < pwr < 6
and root**pwr is equal to the integer entered by the user. If no such
pair of integers exists, it should print a message to that effect.
"""

x = int(input('Enter any integer: '))
pwr = 1
finished = False

while pwr < 6 and not finished:
    pwr = pwr + 1
    root = 1
    while root ** pwr < (x + 1) and not finished:
        root = root + 1
        if root ** pwr == x:
            finished = True
if finished:
    print (root, 'to the power of', pwr, 'equals', x)
else:
    print (f'There is no root, pwr such that root ** pwr = {x}')
        