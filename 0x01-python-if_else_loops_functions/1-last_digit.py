#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
orderRange = ""

if (last_digit > 5 and number > 0):
    orderRange = "greater than 5"
    print(f"last digit of {number} is {last_digit} and is {orderRange}")
elif (last_digit == 0):
    orderRange = "0"
     print(f"last digit of {number} is {last_digit} and is {orderRange}")
 else:
     orderRange = "less than 6 and not 0"
      print(f"last digit of {number} is -{last_digit} and is {orderRange}")
