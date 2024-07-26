# Write a function is_unique(given_string) and find whether a given
# string has unique characters.
# Hint: use set to detect duplicate characters.
#
# Input:
# A given string
#
# Output:
# True if the given string has unique characters, False otherwise
#
# Example:
# 'just' => has unique characters, so the function should return True
# 'Alexander' => has duplicates 'e', so the function should return False


def is_unique(given_string):
    ###
    for i in range(len(given_string)):
        if given_string.count(given_string[i]) > 1:
            return False
        else:
            continue
    return True
    ###


print(is_unique('just'))
print(is_unique('Alexander'))
