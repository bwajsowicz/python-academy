import os
import omdb
import json
import datetime
os.system('cls')

omdb.set_default('apikey', '84f49445')

user_movies = []
user_input = []
movie_titles = []
parameter = 'none'

def print_movie_info(user_movies, parameter):
    if(parameter != 'none'):
        user_movies = sorted(user_movies, key=lambda k: k[parameter], reverse=True)

    for movie in user_movies:
        for key, value in movie.items():
            print(f'{key}: {value}')
        print('')

def load_movies_from_file(path : str):
    movie_titles = []
    word_list = []

    with open('C:\words.txt', 'rt') as file:
        for line in file:
            for string in line.strip().split(', '):
                word_list.append(string)
    file.close()

    for file in os.listdir(path):
        movie_titles.append(os.path.splitext(file)[0])
        for word in word_list:
            movie_titles[-1] = movie_titles[-1].replace(word, '')

    return movie_titles

while(True):
    user_input = input('Wanna type movie titles or load them from file?: ')

    if user_input == 'type':
        user_input = input('Type movie title or titles: ')

        if user_input == 'end':
            break

        user_input = user_input.split(':')
        movie_titles += user_input[0].split(', ')

        if len(user_input) > 1:
            parameter = user_input[1]
        else:
            parameter = 'none'
    elif user_input == 'load':
        movie_titles = load_movies_from_file('C:\Movies\\')
    if user_input == 'end':
            break
        
    for title in movie_titles:
        res = omdb.request(t=title, r = 'json')
        data = json.loads(res.content)
        runtime = int(data['Runtime'][:-3])
        if data['Response'] == False:
            user_input.remove(title)
            print(f'Movie {title} doesn\'t exist!')
        else:
            release_date = datetime.datetime.strptime(data['Released'], '%d %b %Y').date()
            popularity = int(data['imdbVotes'].replace(',',''))
            user_movies.append({'Title': data['Title'], 'Released': release_date , 'Rating': int(data['Metascore']), 
                              'Runtime': runtime, 'Popularity': popularity })
    
print()
print_movie_info(user_movies, parameter)
