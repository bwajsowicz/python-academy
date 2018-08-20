import os

os.system("cls")

def append_to_string(sentence):
    if len(sentence) >= 5:
        return f'{sentence} World'
    else:
        return f'Welcome, {sentence}'

assert append_to_string('Hello') == 'Hello World', 'Failed test case'
assert append_to_string('Hi') == 'Welcome, Hi', 'Failed test case'