# Write a Python function combineValues(item_list) to combine values in a
# list of dictionaries. Each dictionary in the list specifies an item name and
# its amount, e.g. {'item': 'item1', 'amount': 400}. You task is to summary those
# items and their total amount, e.g. {'item1': 400}.
#
# Input:
# item list. Type: a list of dictionaries.
#
# Output:
# a combination of the input dictionary list. Type: dictionary, where keys are names of items
# appeared in the input list, values are the total amount of that item.
#
# Example:
# combineValues([{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}])
#     = {'item1': 1150, 'item2': 300}


def combineValues(item_list):
    ###
    answers = {}
    for i in range(len(item_list)):
        current = item_list[i]
        name1 = current['item']
        sum = current['amount']
        for j in range(len(item_list)):
            if i != j:
                other = item_list[j]
                name2 = other['item']
                if name1 == name2:
                    value2 = other['amount']
                    sum = sum + value2
        answers[name1] = sum
    return answers
    ###


print(combineValues([{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]))
