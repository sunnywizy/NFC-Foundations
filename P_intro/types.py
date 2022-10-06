#!/usr/bin/python3
"""
Most important python core data type
"""

# Number Type
from tokenize import single_quoted


integer = 12345
float = 14.35
complex_Num = 123+3j
binary = 0b111

print('This is an integer', integer, type(integer), sep=', ')
print('This is an float', float, type(float), sep=', ')
print('This is an complex_Num', complex_Num, type(complex_Num), sep=', ')
print('This is binary', binary, type(binary), sep=', ')

#String Types
single_quoted = 'This is a single quoted string'
double_quoted = "This a double quoted string"
raw_string = r'This is a raw string'

#fortmatted strings
name = input('Enter your name: ')
formatted_string = f'Good evening, {name}'
formatted_string2 = 'Good evening, {}'.format(name)
formatted_string3 = 'Good evening, %s' %name
print(single_quoted, double_quoted, raw_string, formatted_string, formatted_string2, formatted_string3, sep='\n ');