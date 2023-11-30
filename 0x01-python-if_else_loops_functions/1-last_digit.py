#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
N = abs(number) % 10
if number < 0:
    N = -N
print(f"Last digit of {number:d} is {digit:d} and is ", end="")
if N > 5:
    print("greater than 5")
elif N == 0:
    print("0")
else:
    print("less than 6 and not 0")
