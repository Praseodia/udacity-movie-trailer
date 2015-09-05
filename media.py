class Movie(object):
    """
    Provides structure to movie object used by create_movie_titles_content in
    fresh_tomatoes.py. The default attributes are: title, poster_image_url,
    and trailer_youtube_url.

    Args:
        title: A string representing the movie title.
        poster_image_url: A string representing the link to movie poster image.
        trailer_youtube_url: A string representing the link to movie's trailer on youtube.
        release_year: A string representing the year the movie was released.
        top_casts: A list of the strings fo the top two casts.
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url, release_year, top_casts):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_year = release_year
        self.top_casts = ', '.join(top_casts)