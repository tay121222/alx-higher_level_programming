#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }

    sum = 0
    i = 0
    while i < len(roman_string):
        char = roman_string[i]

        if char in roman_dict:
            if i + 1 < len(roman_string) and roman_dict[char] < roman_dict[roman_string[i + 1]]:
                sum += roman_dict[roman_string[i + 1]] - roman_dict[char]
                i += 2
            else:
                sum += roman_dict[char]
                i += 1
        else:
            return 0

    return sum
