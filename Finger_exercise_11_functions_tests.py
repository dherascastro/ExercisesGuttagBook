# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 19:00:26 2022

@author: home
"""
"""
Write a function to test is_in
"""

def is_in (str1, str2):
    if str1 in str2 or str2 in str1:
        return True
    else:
        return False
    
def test_is_in (str1_values, str2_values):
    for str1 in str1_values:
        for str2 in str2_values:
            result = is_in (str1, str2)
            if str1 in str2 or str2 in str1:
                resultado_esperado = True
            else: 
                resultado_esperado = False
            if result == resultado_esperado:
                feedback = 'Okay'
            else:
                feedback = 'Bad'
            print (f' str1 = {str1}, str2 = {str2}, Result = {result}, Test evaluation: {feedback}')
str1_values = ('pocholo', 'mamotreto', 'golardo')
str2_values = ('juanete', 'mamotretoncio', 'gol')
test_is_in (str1_values, str2_values)