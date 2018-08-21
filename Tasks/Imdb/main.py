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
user_input = ['']

def print_movie_info(user_movies, parameter):
    if(parameter != 'none'):
        user_movies = sorted(user_movies, key=lambda k: k[parameter], reverse=True)

    for movie in user_movies:
        for key, value in movie.items():
            print(f'{key}: {value}')
        print('')

def get_parameter(user_input : str):
    for element in user_input:
        if element.find(':') >= 0:
            rating = element[element.find(':')+1:]
            element = element[:element.find(':')-1]
            return rating
    return 'none'

while(True):
    user_input = input('Type movie title or titles: ').split(', ')

    if(user_input[-1] == 'end'):
        break

    parameter = get_parameter(user_input)

    if(parameter != 'none'):
        xd = user_input.pop()
        xd = xd[:xd.find(':')-1]
        user_input.append(xd)

    for title in user_input:
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
