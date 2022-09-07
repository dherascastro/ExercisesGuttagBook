# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 19:30:11 2022

@author: home
"""
"""
Si x = -25, los valores de ans se irían acercando a 0 al adquirir siempre el
valor de high por lo que ans tendería a 0 cuando num_guesses tendiese a
infinito. Como la respuesta no se encuentra en el rango de búsqueda, no se
encuentra ningún resultado y como no se puede escapar del bucle while, el
programa no para su ejecución y nunca se llega a imprimir ningún resultado.

Using bisection search to approximate square root
What would have to be changed to make the code
in Figure 3-5 work for finding an approximation to the cube root of
both negative and positive numbers? Hint: think about changing low
to ensure that the answer lies within the region being searched.
"""

x = int(input('Enter any integer: '))

epsilon = 0.01
num_guesses = 0
low = min (0, x)
high = max (0, x)
ans = (high + low) / 2

while abs(ans ** 3 - x) >= epsilon:
    print ('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans ** 3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2

print ('number of guesses =', num_guesses)
print (ans, 'is close to the cube of', x)