# A submatrix S of a matrix M is a matrix itself, which start at some row and column of M, say M[i,j] and extends to
# some row and column of M, say M[k,l], where i,j,k,l are all integers,and 0 <= i,k <= total rows of M,
# and 0 <= j,l <= total columns of M, with further k >= i and l >= j.
# E.g. for the matrix M = [1, 2, 3
#                          4, 5, 6
#                          7, 8 ,9]
# a submatrix S can be M[0,1] to M[1,2], giving us S = [2, 3
#                                                       5, 6]
#
# A common operation in data science is keeping track of the sum of numbers in a subsmatrix of a matrix.
# Write a function sub_matrix_sum(mat) which takes a numpy matrix as input, and does the following:
# 1. the starting row and column of the submatrix is always 0 and 0 respectively, i.e. the submatrix always starts at
#    the first row (numbered 0 in numpy) and the first column (numbered 0 in numpy)
# 2. it creates a numpy matrix of the same size as the input numpy matrix
# 3. the i,j entry of the matrix from step 2. should be the the sum of all entries of the submatrix of the INPUT matrix
#    starting at row number 0 and column number 0 and ending at row number i and column number j
#
# function sub_matrix_sum(M)
# Inputs: 1 input
#   - a numpy matrix
# Outputs: 1 output
#   - a numpy matrix
#
# Examples:
# 1. for the numpy matrix [[0 1 2]
#                        [3 4 5]
#                        [6 7 8]], the output should be the following:
# [[ 0  1  3]
#  [ 3  8 15]
#  [ 9 21 36]]
#
# 2. for the numpy matrix [[0 1 2]
#                          [3 4 5]], the output should be the following:
# [[ 0  1  3]
#  [ 3  8 15]]


import numpy as np


def sub_matrix_sum(M):
    ###
    return (M.cumsum(axis=0)).cumsum(axis=1)
    ###


print(sub_matrix_sum(np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8]])))
print(sub_matrix_sum(np.array([[0, 1, 2], [3, 4, 5]])))
