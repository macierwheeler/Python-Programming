# Write a function named findNumbers to find those numbers which are
# divisible by 7 and multiple of 5, between 1869 and 2020 (both included).
#
# Input: None
#
# Output: a list of numbers which are divisible by 7 and multiple of 5,
# between 1869 and 2020 (both included).


def findNumbers():
    ###
    list_of_numbers = []

    for num in range(1869, 2021):
        if num % 7 == 0 and num % 5 == 0:
            list_of_numbers.append(num)
        else:
            continue

    return list_of_numbers
    ###


print(findNumbers())
