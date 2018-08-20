import os

os.system("cls")

def remove_chars(sentence):
    return sentence[1:-1]

assert remove_chars('country') == 'ountr', 'Failed test case'
assert remove_chars('Tieto') == 'iet', 'Failed test case'

