from .base import MovieDB


class MoviePopular(MovieDB):

    endpoint = '/movie/popular'
    name = 'Popular Movies'
