# Write a function encode() to encode a secret string by firstly capitalize every
# character of that string and then converting each character to its ASCII value.
#
# Input:
# a secret string. Type: string
#
# Output:
# converted secret code. Type: string
#
# Example:
# encode('Hello') = '7269767679'


def encode(secret):
    ###
    new_word = ''
    for j in range(len(secret)):
        new_word = new_word + secret[j].capitalize()

    answer = ''
    for i in range(len(new_word)):
        answer = answer + str(ord(new_word[i]))

    return answer
    ###


print(encode('Hello'))
