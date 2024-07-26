# In C/C++, dividing one integer A by another interger B will return an integer C, no matter whether
# the integer A can be divided with no remainder. For example, in C/C++, 5/2=2. This is different
# from Python, where dividing one integer A by another interger B will return the exact result.
# i.e. in Python 5/2 will return 2.5 instead of 2.
# In this question, you're going to write a function divide(a,b) which takes two numbers as
# input, and divides a by b as in C/C++. You should first check if the two numbers are both
# integer or not. Then if they are both integers, the result c should also be a integer.
# Otherwise, the result c should be a float number.
#
# Input:
# a, b. Type: integer or float
#
# Output:
# c. Type: integer or float
#
# Example:
# divide(5, 2) = 2
# divide(5.4, 3) = 1.8

# or do if type(n1) == int and type(n2) == int:


def divide(n1, n2):
    ###
    if isinstance(n1, int) and isinstance(n2, int):
        return n1 // n2
    else:
        return n1 / n2
    ###


print(divide(5, 2))
print(divide(5.4, 3))
