#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return 0
    sum = 0
    for char in roman_string:
        if char == "I":
            if sum == 0:
                sum -= 1
            else:
                sum += 1
        elif char == "V":
            sum += 5
        elif char == "X":
            sum += 10
        elif char == "L":
            sum += 50
        elif char == "C":
            sum += 100
        elif char == "D":
            sum += 500
        elif char == "M":
            sum += 1000
    return sum
