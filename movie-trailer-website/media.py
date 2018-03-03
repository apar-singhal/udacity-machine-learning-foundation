class Movie():
    '''
    This class stores movie related information
    '''
    API_KEY = 'edb7d107e2f9f6d1aaea1abb2031793f'
    TRAILER_URL_START = r'https://www.youtube.com/watch?v='
    POSTER_URL_START = r'https://image.tmdb.org/t/p/w500'

    VALID_RATINGS = ['-NA-', '1.0', '2.0', '3.0', '4.0', '5.0']

    def __init__(self, title,
                 poster_path, trailer_path,
                 storyline, release_date):
        self.title = title
        self.poster_image_url = self.POSTER_URL_START + poster_path
        self.trailer_youtube_url = self.TRAILER_URL_START + trailer_path
        self.storyline = storyline
        self.release_date = release_date
