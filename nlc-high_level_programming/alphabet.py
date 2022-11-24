#!/usr/bin/python3
"""How to print A-Z in lowcases with importinf any module and also not storing it variable by using ASCII Alphabet"""
for i in range(97,123):
     print(chr(i), end = " ")

"""The chr() function in python returns unicode character for the provided ASCII value, chr(97) return "a" """