# Under the folder ../resource/asnlib/public there're 5 text files you can have access to,
# test1.txt, test2.txt, test3.txt, test4.txt, and test5.txt.
#
# Write a function file_analysis(filename) that does the following:
# 1. read the contents of the file passed as the parameter.
# 2. remove all but alphanumeric characters from the contents of the file read in step 1. This means removing all
#    punctuation marks, and special characters like '$', '@', '*', curly quotation marks etc.
# 3. create a dictionary that has five keys: 'characters', 'vowels', 'alphabetic', 'non-alphabetic', 'words'. A number
#    itself would be considered a word too, e.g. 100 would be a word. So would be abc123.
# 4. the values for each key should be the count of the key in the contents of the file after removing punctuation in
#    step 2, e.g. the value against the key 'vowels' should be the number of vowels occurring in the file passed.
# 5. return the dictionary created in step 4.
#
# function file_analysis(filename)
# Inputs: 1 input
#   - filename: a string representing the file, e.g. '/Users/user1/Desktop/input1.txt'
# Outputs: 1 output
#   a dictionary
#
# Examples
# - for test1.txt, the function should return the following
#   {'characters': 11, 'vowels': 3, 'alphabetic': 10, 'non-alphabetic': 1, 'words': 3}
#
# - for test2.txt, the function should return the following
#   {'characters': 26, 'vowels': 11, 'alphabetic': 24, 'non-alphabetic': 2, 'words': 9}


import re


def file_analysis(filename):
    ###
    myfile = open(filename, 'r')
    content = myfile.read()
    myfile.close()

    content = re.sub(r'[^\w\s]', '', content)
    content = re.sub(r'\n', ' ', content)

    result = {'characters': 0, 'vowels': 0, 'alphabetic': 0, 'non-alphabetic': 0, 'words': 0}

    words = content.split()

    characters = (''.join(words)).lower()

    vowels = ['a', 'e', 'i', 'o', 'u']
    total_vowels = 0
    for vowel in vowels:
        total_vowels = total_vowels + list(characters).count(vowel)

    result['characters'] = len(characters)
    result['vowels'] = total_vowels
    result['non-alphabetic'] = len(re.findall(r'[0-9]', characters))
    result['alphabetic'] = len(characters) - result['non-alphabetic']
    result['words'] = len(words)

    return result
    ###
