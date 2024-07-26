# Define the following vectors and matrices:
# vec1 = np.array([ -1., 4., -9.])
# mat1 = np.array([[ 1., 3., 5.], [7., -9., 2.], [4., 6., 8. ]]
#
# 1. You can multiply vectors by constants. Compute
#    vec2 = (np.pi/4) * vec1
# 2. You can add vectors and multiply by scalars. Compute
#    vec3 = vec1 + 2 * vec2
# 3. You can do row-column matrix multiplication. Compute the product of mat1 and vec3 and set vec4 equal to the result.
# 4. Compute the transpose of mat1. Set mat2 equal to the result.
#
# Write a function compute(vec1, mat1) to do the above four things, and
# return vec2, vec3, vec4, mat2.


import numpy as np


def compute(vec1, mat1):
    ###
    vec2 = (np.pi/4) * vec1
    vec3 = vec1 + (2 * vec2)
    vec4 = mat1 * vec3
    mat2 = mat1.transpose()

    return vec2, vec3, vec4, mat2
    ###


print(compute(np.array([ -1., 4., -9.]), np.array([[1., 3., 5.], [7., -9., 2.], [4., 6., 8.]])))
