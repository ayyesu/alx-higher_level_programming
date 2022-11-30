#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
exe = 0
if number < 0:
    number *= -1
    exe = 1
lastd = number % 10
if exe == 1:
    number *= -1
    lastd *= -1
print(f"Last digit of {number} is ", end="")
if lastd > 5:
    print(f"{lastd} and is greater than 5")
elif lastd == 0:
    print(f"{lastd} and is 0")
else:
    print(f"{lastd} and is less than 6 and not 0")
