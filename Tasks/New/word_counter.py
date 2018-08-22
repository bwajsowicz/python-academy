import os
os.system('cls')

# Write a Python program to count the occurrences of each word in a given sentence.
def word_counter(sentence):
    dictionary = {}
    
    words = sentence.split()
    chars = []

    for i, word in enumerate(words):
        if not words[i].isalpha():
            words[i] = word[:-1]
            chars.append(word[-1])

    words = words + chars
    words = set(words)

    for word in words:
        dictionary[word] = sentence.count(word)
    return dictionary

#answer = {"Ala": 2, "ma": 2, "kota.": 1, "psa.": 1}
#assert word_counter("Ala ma kota. Ala ma psa.") == answer

answer = {'psa': 1, 'kota': 1, '.': 2, 'Ala': 2, 'ma': 2, ',': 2}
assert word_counter("Ala, ma, kota. Ala ma psa.") == answer

