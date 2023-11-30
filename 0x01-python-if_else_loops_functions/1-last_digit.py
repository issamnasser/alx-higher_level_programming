#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastN = number % 10 if number>0 else number % -10
print(f"Last digit of {number:d} is {lastN:d} and is ", end="")
if lastN > 5:
    print("greater than 5")
elif lastN == 0:
    print("0")
else:
    print("less than 6 and not 0")
