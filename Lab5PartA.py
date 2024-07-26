# You are going to visit a city during your Spring break. Assume that you have
# a list of cities and you want to retrieve an item at random from this list.
# Write a function chooseDest(city_list) which takes a list of cities as
# input. In the function, you may firstly shuffle the list, and then randomly
# pick one city using random library, to decide which city to be
# your travel destination.
#
# Input:
# city_list. Type: a list of strings
#
# Output:
# a chosen city. Type: string
#
# Example:
# chooseDest(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']) = 'Los Angeles'


import random


def chooseDest(city_list):
    ###
    random.shuffle(city_list)
    answer = random.choice(city_list)
    return answer
    ###


print(chooseDest(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']))
