import fresh_tomatoes
import media
import urllib, json

"""
Movie Trailers Website - Udacity Project #1
--entertainment_center.py MODULE--
August 2016 - Initial iteration
Developed by: Nathan Hernandez
ver. 0.1

###Utilizes TheMovieDB public API###
"""

# Global variables
api_key = ""
config = ""
# Note: Poster size options include ("w92","w154","w185","w342","w500","w780","original")
POSTER_SIZE = "w342"

def get_api_key():
    """ Reads and returns locally stored API key for TheMovieDB access """
    # Api Key for access
    f = open('api_key.txt', 'r')
    api_key = f.readline()
    f.close()

    #print("Our API Key is: " + str(api_key))
    return str(api_key)

def get_themoviedb_configuration():
    """ Gets system wide configuration for the TheMovieDB resources """
    # Query config info
    connection = urllib.urlopen("http://api.themoviedb.org/3/configuration?api_key="+str(api_key))
    config_json = json.loads(connection.read())
    #print config_json
    return config_json
    

def get_movie_info(movie):
    """ Uses TheMovieDB public API to get movie details. """
    # Query TheMovie DB
    connection = urllib.urlopen("http://api.themoviedb.org/3/search/movie?query="+movie+"&api_key="+str(api_key))
    movieDB_json = json.loads(connection.read())

    # Our Movie ID
    movie_id = movieDB_json['results'][0]['id']
    print("Movie ID is: "+str(movie_id))
    connection.close()

    # Grab extended movie info
    extended_connection = urllib.urlopen("http://api.themoviedb.org/3/movie/"+str(movie_id)+"?api_key="+str(api_key)+"&append_to_response=videos")
    # Movie 'dict' object
    mdict = json.loads(extended_connection.read())
    print(mdict)
    extended_connection.close()

    print("VIDEO INFO")
    print mdict['videos']['results']
    videos = mdict['videos']['results']
    mvideo = ""
    for video in videos:
        print video['name']
        if video['name'] == "Official Trailer":
            mvideo = video
            break

    # In the case there is no 'Official Trailer' named, grab the 1st video associated
    if mvideo == "":
        mvideo = videos[0]

    print ("MVIDEO is: ")
    print mvideo
    print mvideo['key']

    # Our formatted movie info output
    movie_info = media.Movie(str(mdict['original_title']),
                             str(mdict['runtime']),
                             str(mdict['overview'].encode('utf8')),
                             str(config['images']['base_url']+POSTER_SIZE+str(mdict['poster_path'])),
                             "https://www.youtube.com/watch?v="+str(mvideo['key']))

    print(movie_info)
    return movie_info


##### Main #####
api_key = get_api_key()
config = get_themoviedb_configuration()
#print(config['images']['base_url'])

# Get some movies to populate our page
inferno = get_movie_info("Inferno")
star_trek_beyond = get_movie_info("Star Trek Beyond")
sultan = get_movie_info("Sultan")
jason_bourne = get_movie_info("Jason Bourne")
kubo_and_2strings = get_movie_info("Kubo and the Two Strings")
sully = get_movie_info("Sully")
blood_father = get_movie_info("Blood Father")
rogue_one = get_movie_info("Rogue One: A Star Wars Story")
zootopia = get_movie_info("Zootopia")

# Launch 'Fresh Tomatoes' Movie Trailer Site
movies = [inferno, star_trek_beyond, sultan, jason_bourne, kubo_and_2strings, sully, blood_father, rogue_one, zootopia]
fresh_tomatoes.open_movies_page(movies)
