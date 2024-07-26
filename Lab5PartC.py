# In this exercise, write a function named random_digits(prefix, N) that generates random telephone numbers with a given
# prefix and it has N digits in total. For example, given N=10 and prefix '765', the function random _digits() should
# return a valid phone number such as '765-494-1234'. The first digit should not be 0.
#
# Input:
# a prefix (less than N digits). Type: string
# an integer N (>=7). Type: int
#
# Output:
# a phone number has N digits. Type: string (with the format 'NPA-NXX-XXXX')
#
# Example:
# random_digits('765', 10) = '765-862-2549'
# random_digits('831', 9) = '831-304-264'
# random_digits('', 10) = '851-537-6933'


import random


def random_digits(prefix, N):
    ###
    if len(prefix) > 0 and prefix[0] == '0':
        return 'First digit was 0'

    length_of_prefix = len(prefix)

    if length_of_prefix == 0:
        random_number = random.randrange(1, 10)
    else:
        random_number = random.randrange(0, 10)

    digits = list(prefix) + [str(random_number)]
    digits = digits[0:N]

    for i in range(N - length_of_prefix - 1):
        digits.append(str(random.randrange(0, 10)))

    return ''.join(digits[0:3]) + '-' + ''.join(digits[3:6]) + '-' + ''.join(digits[6:len(digits)])
    ###


print(random_digits('1234567',7))
