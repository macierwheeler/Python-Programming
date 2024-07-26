# Write a function encode(inputStr) that takes a string as an input and does the following:
# 1. sums up the ASCII codes of all the individual characters of the inputStr
# 2. raise the sum computed in 1. to the length of the inputStr
# 3. divide the number computed in 2. by 95 and take get the remainder
# 4. add 33 to the remainder computed in 3.
# 5. return the character whose ASCII code is the number computed in 4.
#
# encode(inputStr)
# Inputs:
#   - a string
# Outputs:
#   - a string (one character)
#
# Example:
# encode('Hello!') -> '['
# encode('There') -> '>'


import math


def encode(sentence):
    ###
    sum_of_ascii = 0

    for i in range(len(sentence)):
        sum_of_ascii = sum_of_ascii + ord(sentence[i])

    power = sum_of_ascii ** len(sentence)
    remainder = power % 95
    add = remainder + 33
    character = chr(add)

    return character
    ###


print(encode('Hello!'))
print(encode("There"))
