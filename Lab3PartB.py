# We have a phone list of the Simpsons, yes, the famous Simpsons from the
# American animated TV series. The phone book can be obtained
# directly from the website 'https://www.python-course.eu/simpsons_phone_book.txt'
# by using urlopen from the module urllib.request.
# There are some people with the surname Neu. We are looking for a Neu, but we don't know the first name, we just know
# that it starts with a J.
#
# $ simpsons_phone_book.txt
# Allison Neu 555-8396
# Bob Newhall 555-4344
# C. Montgomery Burns 555-0001
# C. Montgomery Burns 555-0113
# ...
#
# Let's write a Python function findPhoneNumber(), which finds all the lines
# of the phone book, which contain a person with the described surname and a
# first name starting with J.
#
# Input: None
#
# Output:
# A list of all the lines of the phone book, which contain a person with a surname Neu and a
# first name starting with J
# Each line is a person's name followed by his/her phone number.
# E.g. ["Jack Neu 555-7666", ...]


from bs4 import BeautifulSoup
import requests

def findPhoneNumber(url='https://www.python-course.eu/simpsons_phone_book.txt'):
    ###
    page = requests.get('https://www.python-course.eu/simpsons_phone_book.txt')
    soup = BeautifulSoup(page.text, features= 'html.parser')

    new_list = []

    file = soup.prettify()

    for line in file.split('\n'):
        new_list.append(line)

    updated_list = []

    for info in new_list:
        if 'Neu' in info and info[0] == 'J':
            updated_list.append(info)

    results_list = list(map(str, updated_list))

    return results_list
    ###


print(findPhoneNumber())
