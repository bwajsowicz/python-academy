import os
import omdb
import json
import datetime
os.system('cls')

omdb.set_default('apikey', '84f49445')

'''
resp = omdb.request(t='True Grit', r ='json')
data = json.loads(resp.content)
print(json.dumps(data, indent=4))

another_movie = omdb.title('Pulp Fiction')

print(another_movie['title'])
'''

'''
#1
user_movies = []
user_input = ''

while(user_input != 'end'):
    user_input = input("Type movie title: ")
    if user_input != 'end': user_movies.append(user_input)

for title in user_movies:
    resp = omdb.request(t=title, r = 'json')
    data = json.loads(resp.content)
    print(json.dumps(data, indent = 4))
'''

#2
user_movies = []
user_input = []

def print_movie_info(user_movies, parameter):
    if(parameter != 'none'):
        user_movies = sorted(user_movies, key=lambda k: k[parameter], reverse=True)

    for movie in user_movies:
        for key, value in movie.items():
            print(f'{key}: {value}')
        print('')

while(True):
    user_input = input('Type movie title or titles: ')

    if user_input == 'end':
        break
        
    user_input = user_input.split(':')
    movie_titles = user_input[0].split(', ')

    if len(user_input) > 1:
        parameter = user_input[1]
    else:
        parameter = 'none'

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
            user_movies.append({'Title': data['Title'], 'Released': release_date , 'Rating': data['Metascore'], 
                              'Runtime': runtime, 'Popularity': popularity })
    
print('')
print_movie_info(user_movies, parameter)
