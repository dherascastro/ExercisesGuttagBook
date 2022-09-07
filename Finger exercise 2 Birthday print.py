# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 21:37:40 2022

@author: home
"""
"""
Practicing inputs and f-strings

Write code that asks the user to enter their
birthday in the form mm/dd/yyyy, and then prints a string of the
form ‘You were born in the year yyyy.’
"""

birthday = input ('Enter your birthday mm/dd/yyyy: ')

print (f' You were born in the year {birthday [6:]}')