# Write a function called words_freq(sentence) that does the following:
# 1. find the frequency of occurrence of all the words in the sentence
# 2. assemble a dictionary whose keys are the words and values are the frequency of the key
# 3. return the dictionary from 2.
#
# function words_freq(sentence)
# Inputs: 1 input
#   - sentence: a string
# Outputs: 1 output
#   - a dictionary
#
# Example:
#   words_freq('hello world') -> {'hello': 1, 'world': 1}
#   words_freq('I think I know it') -> {'I': 2, 'think': 1, 'know': 1, 'it': 1}


def words_freq(sentence):
    ###
    new_dict = {}

    list_of_words = sentence.split(' ')
    for word in list_of_words:
        if word not in new_dict:
            new_dict[word] = list_of_words.count(word)

    return new_dict
    ###


print(words_freq('hello world'))
print(words_freq('I think I know it'))
