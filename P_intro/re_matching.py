#!/usr/bin/python3
"""String Pattern matching"""
#import a python standard library tool
# for performing regex(regular expressions)
import re

match = re.match('The [ \t]*(.*)python', 'The Zen of python is The Zen of just python')
print(match.group())

match_brackets = re.match('[A-Za-z]*(.*)', 'The Zen of python is The Zen of just python')
print(match.group())


