import re
import os

os.system('cls')

def valid_bracets(sentence):
    return bool(re.match(r'([(].{2,}[)]|[(][)])|([{].{2,}[}]|[{][}])|([[].{2,}[]]|[[][]])', sentence))


assert valid_bracets('(){}[]') == True
assert valid_bracets('([{}])') == True
assert valid_bracets('(}') == False
assert valid_bracets('[(])') == False