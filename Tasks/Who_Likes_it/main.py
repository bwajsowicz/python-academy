import os

os.system("cls")

def who_likes_it(list_of_likes):
    if len(list_of_likes) > 0:
        list_of_likes = list_of_likes[0].split(', ')
        number_of_likes = len(list_of_likes)
        if number_of_likes == 1:
            return f'{list_of_likes[0]} likes this'
        elif number_of_likes == 2:
            return f'{list_of_likes[0]} and {list_of_likes[1]} like this'
        elif number_of_likes == 3:
            return f'{list_of_likes[0]}, {list_of_likes[1]} and {list_of_likes[2]} like this'
        else:
            return f'{list_of_likes[0]}, {list_of_likes[1]} and {number_of_likes-2} others like this'
    else:
        return 'no one likes this'
        
assert who_likes_it([]) == "no one likes this", "Wrong like count!"
assert who_likes_it(["Ryszard"]) == "Ryszard likes this", "Wrong like count!"
assert who_likes_it(["Marcin, Michal"]) == "Marcin and Michal like this", "Wrong like count!"
assert who_likes_it(["Edyta, Igor, Kamil"]) == "Edyta, Igor and Kamil like this", "Wrong like count!"
assert who_likes_it(["Michal, Maciej, Bartosz, Przemek"]) == "Michal, Maciej and 2 others like this", "Wrong like count!"
