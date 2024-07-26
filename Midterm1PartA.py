# Write a function called numberOfUniqueElements that finds the number of unique elements in a list.

# numberOfUniqueElements(listOfElements) takes as input a list, and returns the number of unique elements in it.
#
# Example:
#   numberOfUniqueElements([1,2,2,4]) -> 3

# could do
# answer = set(listOfElements)
# return len(answer)


def numberOfUniqueElements(listOfElements):
    ###
    sum_of_elements = 0
    counted = False

    for i in range(len(listOfElements)):
        if listOfElements.count(listOfElements[i]) > 1:
            if counted:
                sum_of_elements = sum_of_elements
                if listOfElements.count(listOfElements[i]) > 2:
                    counted = True
                else:
                    counted = False
            else:
                sum_of_elements = sum_of_elements + 1
                counted = True
        else:
            sum_of_elements = sum_of_elements + 1

    return sum_of_elements
    ###


print(numberOfUniqueElements([1, 2, 2, 4]))
