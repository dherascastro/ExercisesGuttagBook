# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 12:03:47 2022

@author: home
"""
"""
s = 'hhhhh'
sub = 'h'
Resultado: 4

s = 'ohohohoh'
sub = 'ho'
Resultado: 5

s = 'ohohohoh'
sub = 'oh'
Resultado: 6

s = 'ermano'
sub = 'h'
Resultado: None

s = 'run, Forrest, run'
sub = 'run'
Resultado: 14
"""

def find_last(s, sub):
    """s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s"""
    index = -1
    save_find = s.find (sub)
    while save_find >= 0:
        index += save_find + 1
        s = s[(save_find + 1):]
        save_find = s.find (sub)
    if index != -1:
        return index
    else:
        return None

s = 'run, Forrest, run'
sub = 'run'
print (find_last (s, sub))

