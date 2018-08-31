import omdb
import json
from datetime import datetime
import os
import urllib

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
    word_list = open('C:\words.txt', 'rt').read().replace('\n', '').split(', ')

    for file in [f for f in os.listdir(path) if os.path.isfile(f'C:/Movies/{f}')]:
        movie_titles.append(os.path.splitext(file)[0])
        for word in word_list:
            movie_titles[-1] = movie_titles[-1].replace(word, '')

    return movie_titles

def put_movies_in_folder(user_movies : list):
    for movie in user_movies:
        if not os.path.exists(f'C:\Movies\{movie["Title"]}'):
            os.mkdir(f'C:\Movies\{movie["Title"]}')
            file = open(f'C:\Movies\{movie["Title"]}\info.txt', 'a')
            urllib.request.urlretrieve(movie['Poster'], f'C:\Movies\{movie["Title"]}\{movie["Title"]}.jpg')
            for key, value in movie.items():
                file.writelines(f'{key}: {value}\n')
        else:
            print('FOLDER EXIST!"')

while(True):
    user_input = input('Wanna type movie titles or load them from file?[load/type/end]:  ')

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
        if data['Response'] == 'False':
            user_input.remove(title)
            print(f'Movie {title} doesn\'t exist!')
        else:
            #TODO: fix problem with N/A
            runtime = int(data['Runtime'][:-3])
            release_date = datetime.strptime(data['Released'], '%d %b %Y').date()
            popularity = int(data['imdbVotes'].replace(',',''))
            rating = data['Metascore']
            user_movies.append({'Title': data['Title'], 'Released': release_date , 'Rating': rating, 
                              'Runtime': runtime, 'Popularity': popularity, 'Poster': data['Poster'] })
    
print()
put_movies_in_folder(user_movies)
print_movie_info(user_movies, parameter.strip())
