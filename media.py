
class Movie:
    """
    Movie class
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """__init__ is called when a new object of the Movie class is created.

        Args:
            title (str): Title of the movie
            poster_image_url (str): Url of the poster of the movie
            trailer_youtube_url (str): Youtube url for the trailer of the movie
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
