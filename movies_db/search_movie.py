from .base import MovieDB


class SearchMovie(MovieDB):

    endpoint = '/search/movie'
    name = 'Search Results'
