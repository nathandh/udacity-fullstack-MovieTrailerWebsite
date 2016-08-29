import webbrowser

class Video():
    """ This class is our base VIDEO class for all media """
    def __init__(self, video_title, video_duration):
        print("VIDEO base constructor called...")
        self.title = video_title
        self.duration = video_duration

class Movie(Video):
    """ This class provides a way to store MOVIE related information.
        It inherits from the VIDEO class. """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_duration, movie_storyline,
                 poster_image, trailer_youtube):
        print("MOVIE child constructor called...")
        Parent.__init__(self, movie_title, movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
