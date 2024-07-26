# coding=utf-8
# Use matplotlib.pyplot.plot to produce a plot of the functions
# f(x) = e^(−x/10)sin(πx) and
# g(x) = xe^(−x/3)
# over the interval [0, 10].
# Include labels for the x- and y-axes, and a legend explaining which line is which plot.
# Be sure to use enough points that the curve is closed and appears smooth。
# Note: This part will be manually graded.


import matplotlib.pyplot as plt
import math


def plotFunc():
    ###
    f_array_x_values = []
    for i in range(1001):
        f_array_x_values.append(float(i) * 10/1000)

    f_array_y_values = []
    for x in f_array_x_values:
        y = math.pow(math.e, ((-x/10) * math.sin(math.pi * x)))
        f_array_y_values.append(y)

    plt.plot(f_array_x_values, f_array_y_values, color='blue', label='f(x)')

    g_array_x_values = []
    for j in range(1001):
        g_array_x_values.append(float(j) * 10/1000)

    g_array_y_values = []
    for x in g_array_x_values:
        y = math.pow(x * math.e, (-x/3))
        g_array_y_values.append(y)

    plt.plot(g_array_x_values, g_array_y_values, color='red', label='g(x)')

    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.legend()
    plt.show()
    ###


plotFunc()
