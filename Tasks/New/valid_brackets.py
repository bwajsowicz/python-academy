import re
import os

os.system('cls')

def valid_brackets(sentence):
    return bool(re.match(r'([(].{2,}[)]|[(][)])|([{].{2,}[}]|[{][}])|([[].{2,}[]]|[[][]])', sentence))


assert valid_brackets('(){}[]') == True
assert valid_brackets('([{}])') == True
assert valid_brackets('(}') == False
assert valid_brackets('[(])') == False