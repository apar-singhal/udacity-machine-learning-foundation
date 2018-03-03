from media import Movie
import fresh_tomatoes
import json
import requests


# Return the path of trailer to be added with media.Movies.TRAILER_URL_START
# Retrive path with the help of IMDB's movie id
def getTrailerPath(id, key):
    query = "https://api.themoviedb.org/3/movie/" + str(id) + \
            "/videos?api_key=" + key + "&language=en-US"

    connection = requests.get(query)
    json_obj = json.loads(connection.text)
    connection.close()
    return json_obj['results'][0]['key']


# Return an object of media.Movies
# Extract details from the distionary passed
def getMovieObject(movie_dict, key):
    title = movie_dict['title']
    poster_path = movie_dict['poster_path']
    trailer_path = getTrailerPath(movie_dict['id'], key)
    storyline = movie_dict['overview']
    release_date = movie_dict['release_date']
    return Movie(title, poster_path, trailer_path, storyline, release_date)


# Connects with API to get dictionary of each movie name passed
def getListOfMovies(query, key, list_movie_names):
    list_movies = []

    for i in range(len(list_movie_names)):
        connection = requests.get(query + list_movie_names[i])
        json_obj = json.loads(connection.text)
        if('results' in json_obj.keys()):
            if len(json_obj['results']) != 0:
                movie_dict = json_obj['results'][0]
                list_movies.append(getMovieObject(movie_dict, key))
                print list_movie_names[i].replace('+', ' ') + ' added!'
            else:
                print 'Skipping ' + list_movie_names[i].replace('+', ' ') + '!'
        else:
            print 'Invalid Key!'
    connection.close()
    return list_movies


def start():
    # List of movies to be displayed
    list_movie_names = [
        'Spider-Man Homecoming',
        'Annabelle: Creation',
        'Thor: Ragnarok',
        'Transformer: The Last Knight',
        'Despicable Me 3',
        'Wonder Woman'
        ]

    # Converting ' ' to '+' in movie names
    for i in range(len(list_movie_names)):
        list_movie_names[i] = str(list_movie_names[i]).replace(" ", '+')

    api_key = raw_input('Enter a TMDb API Key: ')
    SEARCH_QUERY = "https://api.themoviedb.org/3/search/movie?api_key=" + \
        api_key + '&query='
    list_movies = getListOfMovies(SEARCH_QUERY, api_key, list_movie_names)
    if list_movies != []:
        print "Creating Web Page!"
        fresh_tomatoes.open_movies_page(list_movies)


start()
