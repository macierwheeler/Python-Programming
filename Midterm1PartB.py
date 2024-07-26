# Write a function called split_and_join(my_str) so that it will
# return a modified version of the given string based on the length
# of the string.
#
# If the length of the string is even:
# Swap the first and second halves of the string.
#
# Example:
# split_and_join('purdue') should return 'duepur'
#
# If the length of the string is odd:
# Repeat what you did above but leave the middle element unchanged.
#
# Example:
# split_and_join('Bilbo') should return 'bolBi'
#
# INPUT:
# my_str: the input string, type: String
#
# RETURNS:
# The modified string, type: String
#
# SAMPLE INPUT/OUTPUT:
#
# split_and_join('purdue') should return 'duepur'
# split_and_join('abcde') should return 'decab'
# split_and_join('university') should return 'rsityunive'
# split_and_join('Larry') should return 'ryrLa'
# split_and_join('Moe') should return 'eoM'
# split_and_join('hi') should return 'ih'
# split_and_join('x') should return 'x'
# split_and_join('') should return '' ('' refers to empty string)


def split_and_join(my_str):
    ###
    if len(my_str) % 2 == 0:
        halfpoint = len(my_str) // 2
        first_part_of_string = my_str[0:halfpoint]
        second_part_of_string = my_str[halfpoint:]
        return second_part_of_string + first_part_of_string
    else:
        halfpoint2 = len(my_str) // 2
        first_part_of_string2 = my_str[0:halfpoint2]
        middle_part_of_string2 = my_str[halfpoint2]
        last_part_of_string2 = my_str[halfpoint2 + 1:]
        return last_part_of_string2 + middle_part_of_string2 + first_part_of_string2
    ###


print(split_and_join('purdue'))
print(split_and_join('abcde'))
print(split_and_join('university'))
print(split_and_join('Larry'))
print(split_and_join('Moe'))
print(split_and_join('hi'))
print(split_and_join('x'))
print(split_and_join(''))
