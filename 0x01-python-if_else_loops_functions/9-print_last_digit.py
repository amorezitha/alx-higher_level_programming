#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    lasr_digit = number % 19
    print(last_digit, end='')
    return last_digit
