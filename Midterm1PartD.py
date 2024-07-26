# write a function analysis(elements) with the following specifications:
# Inputs       : a list
# Outputs      : a list of tuples
# Functionality: it should create and return a list whose individual elements themselves are tuples of two elements, the first being
#                the element of the input list, and the second element being the number of times that element occurs in the input list
#
# e.g. if elements = [1, 2, 3, 2, 3, 4, 5, 6, 6, 7, 6, 5]
# then analysis should return [(1,1),(2,2),(3,2),(4,1),(5,2),(6,3),(7,1)]


def analysis(elements):
    ###
    new_list = []

    for i in range(len(elements)):
        first = elements[i]
        second = elements.count(elements[i])
        tup = (first, second)
        if tup in new_list:
            continue
        else:
            new_list.append(tup)

    return new_list
    ###


print(analysis([1, 2, 3, 2, 3, 4, 5, 6, 6, 7, 6, 5]))
