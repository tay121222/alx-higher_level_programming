#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
default = "Last digit of " + str(number) + " is " + str(last_digit)
if last_digit > 5:
    print(default, "and is greater than 5")
elif last_digit == 0:
    print(default, "and is 0")
else:
    print(default, "and is less than 6 and not 0")