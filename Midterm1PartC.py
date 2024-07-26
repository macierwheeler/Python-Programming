# write a function mergeDictionaries(dictionary1, dictionary2) with the following specifications:
# Inputs       : two dictionaries
# Outputs      : one dictionary
# Functionality: it should merge and return a single dictionary whose keys should be the keys in each of the input dictionaries,
#                and its values should be the values that appear against the corresponding keys in the input dictionaries. In
#                case of a key that appears in both the input dictionaries, the value in the final dictionary should be a list
#                containing both the values.
#
# e.g. dictionary1 = {1 : 'a', 2 : 'b'}, dictionary2 = {2 : 5, 3 : 6}
# then mergeDictionaries should return {1 : 'a', 2 : ['b', 5], 3 : 6}


def mergeDictionaries(dict1,dict2):
    ###
    new_dictionary = dict1

    for i in dict2:
        if i in new_dictionary:
            new_dictionary[i] = [new_dictionary[i], dict2[i]]
        else:
            new_dictionary[i] = dict2[i]

    return new_dictionary
    ###


print(mergeDictionaries({1: 'a', 2: 'b'}, {2: 5, 3: 6}))
