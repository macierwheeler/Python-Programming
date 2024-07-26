# Write a function invert(dict) that accepts a dictionary as input. It should return a dictionary whose keys
# are the values in the input dictionary (dict) and whose values are the corresponding keys in the input dictionary
# (dict)
#
# function invert(dict)
# Inputs: 1 input
#   - dict: a dictionary
# Outputs: 1 output
#   a dictionary
#
# Examples:
# invert({1: 'hello', 2: 'world'}) should return {'hello': 1, 'world': 2}
# invert({'Jd': 3.5, 'Xinru': 3.9, 'Ruby': 4.0}) should return {3.5: 'Jd', 3.9: 'Xinru', 4.0: 'Ruby'}


def invert(dict):
    ###
    return {y:x for x, y in dict.items()}
    ###


print(invert({1: 'hello', 2: 'world'}))
print(invert({'Jd': 3.5, 'Xinru': 3.9, 'Ruby': 4.0}))
