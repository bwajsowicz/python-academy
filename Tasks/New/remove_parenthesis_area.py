import re
import os

os.system('cls')

def remove_parenthesis_area(sentence : str):
    for i in range(len(sentence)):
        res = re.findall(r'.[(][^()]*[)]', sentence[i])

        if len(res) > 0:
            for match in res:
                 sentence[i] = sentence[i].replace(match, '')
    return sentence

answer = ['Kamil Kaca to najlepsi przyjaciele']
assert remove_parenthesis_area(['Kamil (Mielnik) (Maciej) Kaca to (Xdfdf) najlepsi przyjaciele']) == answer
answer = ["example", "w3resource", "github", "stackoverflow"]
assert remove_parenthesis_area(["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]) == answer