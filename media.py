import webbrowser

class Movie():
     #   """this is for documentation of this class can be called { print(media.Movie.__doc__)}  """

   # VALID_RATING = ["G","PG","PG-13","R"]           #CLASS VARIABLE
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


        #uses webbrowser to open a youtube link to the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

