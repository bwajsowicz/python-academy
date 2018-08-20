import os

os.system("cls")

def return_half(sentence):
    return sentence[:len(sentence)//2]

assert return_half('Tieto') == 'Ti', 'Failed test case'
assert return_half('Work') == 'Wo', 'Failed test case'
assert return_half('Academy') == 'Aca', 'Failed test case'