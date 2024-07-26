# coding=utf-8
# Write a function polar2Rect which converts Polar coordinates to rectangular coordinates.
# The function should accept two numbers (length, ‹angle in radians›) as input
# Polar coordinates, and return two numbers (x, y) as rectangular coordinates.
#
# Input:
# length, ‹angle in radians›. Type: float
#
# Output:
# x, y. Type: float
#
# Example:
# polar2Rect(2, math.pi) = (-2.0, 2.4492935982947064e-16)


import math


def polar2Rect(l, ang):
    ###
    x = l * math.cos(ang)
    y = l * math.sin(ang)
    tup1 = (x, y)
    return tup1
    ###


print(polar2Rect(2, math.pi))
