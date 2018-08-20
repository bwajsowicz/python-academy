import collections

def count_duplicates(sentence, how_many_times):
    '''
    Function checks how many times a letter is present in a string.
    Return only those letters.
    See test cases for examples
    '''
    return_string = ''

    string_letters = list(collections.OrderedDict.fromkeys(sentence).keys())

    for letter in string_letters:
        if sentence.count(letter) == how_many_times:
            return_string += letter
    
    return return_string

assert count_duplicates("aabcdddee", 2) == "ae", "Failed to count!" # only 'a' end 'e' were present 2 times.
assert count_duplicates("indivisibility", 6) == "i", "Failed to count!"
assert count_duplicates("Karima", 1) == "Krim", "Failed to count!"
