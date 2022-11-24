#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#print(number)
num = str(number)
lastNum = int(num[-1])
#print(lastNum)
if lastNum > 5:
    print("Last digit of {} is {} and is greater than 5" .format(number, lastNum))
elif lastNum == 0:
    print("Last digit of {} is {} and is 0" .format(number, lastNum))
elif lastNum < 6:
    print("Last digit of {} is {} and is last than 6 and not 0" .format(number, lastNum))
