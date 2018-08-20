import os

os.system("cls")

def filter_list(list):
    return [x for x in list if type(x) is int]

assert filter_list([1, 5, 'A', 30, 'Hello', 50, 2.75]) == [1, 5, 30, 50], 'Bad filtering'