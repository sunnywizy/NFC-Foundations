#!/usr/bin/python3
def islower():
    c = str(input("Enter a letter:"))
    if c.islower() == True:
        print("{} is lower".format(c))
    else:
        print("{} is upper".format(c))
        
islower()