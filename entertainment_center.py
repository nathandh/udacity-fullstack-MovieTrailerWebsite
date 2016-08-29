import fresh_tomatoes
import media
import urllib

def get_movie_info(movie):
    """ Uses Rotten Tomatoes public API to get movie details. """
    connection = urllib.urlopen("http://api.rottentomatoes.com/api/public/v1.0/movies.json?q={
    

"""
inferno = media.Movie("Inferno",
                      "After waking up in a hospital with amnesia, professor Robert Langdon (Tom Hanks) and a doctor (Felicity Jones) must race against time to foil a deadly global plot.",
                      "http://t1.gstatic.com/images?q=tbn:ANd9GcRmT8smP6Lep5lGiC1Ls9dUMbfxGITPFS5_nOmPrnXazzVJ6TQ0",
                      "https://www.youtube.com/watch?v=Ln41GXKuo6Y")


star_trek_beyond = media.Movie("Star Trek: Beyond",
                               "A surprise attack in outer space forces the Enterprise to crash-land on a mysterious world.",
                               "http://static1.squarespace.com/static/53323bb4e4b0cebc6a28ffa2/t/573fe299f8baf3f38def74ec/1463804606303/Star+Trek+Beyond+Poster?format=2500w",
                               "https://www.youtube.com/watch?v=XRVD32rnzOw")

sultan = media.Movie("Sultan",
                     "A middle-aged wrestling champion (Salman Khan) tries to make a comeback to represent India at the Olympics.",
                     "http://t2.gstatic.com/images?q=tbn:ANd9GcS1cK4t_uWmqHaRYD9uq69hLEWy7f7NpIfjPlQECdooplpkQcEp",
                     "https://www.youtube.com/watch?v=wPxqcq6Byq0")

jason_bourne = media.Movie("Jason Bourne",
                           "It's been 10 years since Jason Bourne (Matt Damon) walked away from the agency that trained him to become a deadly weapon.",
                           "http://t3.gstatic.com/images?q=tbn:ANd9GcQ27a64TqUZLOU1QbJiBPhu4mBZMW50wFzR62ob5W9o9Mgx7blK",
                           "https://www.youtube.com/watch?v=F4gJsKZvqE4")

movies = [inferno, star_trek_beyond, sultan, jason_bourne]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
"""
