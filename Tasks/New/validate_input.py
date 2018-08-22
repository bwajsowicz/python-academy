import re
import os
os.system('cls')

def validate_input(word):
    # Write a simple regex to validate a username. Allowed characters are:
    # lowercase letters, numbers, underscore
    # Length should be between 5 and 20 characters (both included).
    if re.match(r'[a-z0-9_]{5,20}$', word):
        return True
    else:
        return False

#assert validate_input("Summer Academmy") == False, "Bad validation!"
#assert validate_input("Summer_Academmy") == False, "Bad validation!"
#assert validate_input("summer_academmy") == True, "Bad validation!"
