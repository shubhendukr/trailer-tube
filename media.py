import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""
    def __init__(
      self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ Inits a Movie object
        Args:
        title = a string of the movie's title
        storyline = a string briefly description of movie
        poster_url = a string containing a URL to movie's poster image
        trailer_youtube_url = a string containing a movie's trailer URL
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens trailer in a web browser """
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        """ Displays poster image of the movie """
        webbrowser.open(self.poster_image_url)
