#!/usr/bin/python3
# Python3 code to demonstrate working of
# Alternate cases in String
# Using upper() + lower() + loop
 
# initializing string
letters = "abcdefghijklmnopqrstuvwxyz"
 
# printing original string
print("The original string is : " + str(letters))
 
# Using upper() + lower() + loop
# Alternate cases in String
result = ""
for letter in range(len(letters)):
    if not letter % 2 :
       result = result + letters[letter].upper()
    else:
       result = result + letters[letter].lower()
 
# printing result
print("The alternate case string is : " + str(result))