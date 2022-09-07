# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 19:52:14 2022

@author: home
"""

"""
Practicing nested for loops.

Write a program that prints the sum of the prime
numbers greater than 2 and less than 1000. Hint: you probably want
to use a for loop that is a primality test nested inside a for loop that
iterates over the odd integers between 3 and 999.

El primer bucle for selecciona los primos en el
rango de 2 a 1000 y el segundo bucle for halla los números menores que el
impar determinado por el anterior bucle for. Después, se comprueba si impar
es primo y se apunta en la variable prime_indicator. Se van imprimiendo
los primos según se encuentran. La variable prime_indicator debe estar en
True por defecto por lo que al inicio de cada loop se le asigna el valor
True.
"""
sum_primes = 0
prime_indicator = True

for impar in range (3, 1000, 2):
   prime_indicator = True
   for divisor in range (2, impar):
       if (impar % divisor == 0):
           prime_indicator = False
           break
   if (prime_indicator):
       sum_primes = sum_primes + impar

print (sum_primes)
       
       
       