#!/usr/bin/python3
def uppercase(str1):
    num_upper = 0
    for letter in str1: 
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 0:
        return str1.upper()
    return str1

print(uppercase('obasi sunday'))
