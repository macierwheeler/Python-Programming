# These days usually passwords are required to be of at least a specific length, have some special characters etc.
# Write a function pswd_check(password) that takes a string, the password as input and decides if the password
# 1. is at least 8-characters in length
# 2. has both uppercase and lowercase letters
# 3. has at least one of the following special characters: ~!@#$%^&*()
# 4. has at least one number
#
# function pswd_check(password)
# Inputs: 1 input
#   - a string
# Outputs: 1 output
#   - returns True if the password entered fulfills all the four requirements, and False otherwise
#
# Examples
# pswd_check('BoilerUp!123') should return True
# pswd_check('boilerup!234') should return False (no uppercase letters)
# pswd_check('boilerUp123') should return False (no special characters)


import re


def pswd_check(password):
    ###
    return (any(char.isupper() for char in password) and
            any(char.islower() for char in password) and
            any(char.isdigit() for char in password) and
            len(password) >= 8 and
            bool(re.search(r'[~!@#$%^&*()]', password)))
    ###


print(pswd_check('BoilerUp!123'))
print(pswd_check('boilerup!234'))
print(pswd_check('boilerUp123'))
