#!/usr/bin/python3

options = ["Sausage roll", "Spagetti", "Rice and Stew", "Amala and Soup"]
print(options, end="\n")
choice = input("Pick your Choice?:")
if choice in options:
    pick = options.index(choice)
    print(f"You have been serve with {options[pick]}")
else: print("Your choice is not in our list")

# How to calculate or know which year is a leap year
print("We want to know which is the a leap year by the user input")
year = int(input("Enter your favority year:"))
num1 = 4
num2 = 100
num3 = 400
if year%num1 != 0:
    print("This is a leap year thanks!")
elif year%num2 != 0:
    print("This not a leap year thanks!")
elif year%num3 != 0:
    print("This is a leap year thanks!")
else: print("WOOOH!")

# Program that tells if someone is invited to a birthday party by inputing his or her names
print("If your name appears in the list please juct enter it for more confirmation but if not try next time thanks")
cadidates = ["Sunday", "Ebube", "Emeka", "Olamide", "Mark", "Usman", "Samuel", "Monday", "Ebuka", "Femi", "Tope"]
print(cadidates)
name = input("Enter your name:")
if name in cadidates:
    firstName = cadidates.index(name)
    print(f"You are welcome {cadidates[firstName]} thanks for honoring the invitation")
else: print("Please you are not invited come next time")
