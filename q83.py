#coding:utf-8

from itertools import combinations

def roman_to_int(roman):
    values={'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    """Convert from Roman numerals to an integer."""

    numbers = []
    for char in roman:
        numbers.append(values[char])
        print(numbers)
    total = 0
    for num1, num2 in zip(numbers, numbers[1:]):
        if num1 >= num2:
            total += num1
        else:
            total -= num1
    return total + num2

print(roman_to_int("IX"))