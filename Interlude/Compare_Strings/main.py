import os

os.system("cls")


def compare_strings(first_string, second_string):
    if first_string[0] > second_string[0]:
        return first_string
    else:
        return second_string

  
def shortest_string():
        my_list = ['aaaa', 'bbbbb', 'ccccc']
        shortest = min(my_list, key=compare_strings)
        print(shortest)

shortest = compare_strings('aaaa', 'bbbbb')
print(shortest)

shortest_string()