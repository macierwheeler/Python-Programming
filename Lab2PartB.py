# Write a Python function common_data() that takes two lists
# and returns True if they have at least one common member.
#
# Input:
# two lists
#
# Output:
# True if they have at least one common member and False otherwise.
#
# Example:
# common_data([1,2,3,4,5], [5,6,7,8,9]) = True


def common_data(list1, list2):
    ###
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False
    ###


print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
