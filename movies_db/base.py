import os
import requests

from helpers import formats


class MovieDB:

    BASE_URL = 'https://api.themoviedb.org/3'
    IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/{size}{url}'

    IMDB_URL = 'https://www.imdb.com/title/{imdb_id}/'

    endpoint = None
    kwargs = None
    name = None
    response = {}

    def __init__(self, api_key=None, **kwargs):
        self.API_KEY = api_key or os.getenv('THE_MOVIE_DB_KEY')
        self.kwargs = kwargs
        self.kwargs['api_key'] = self.API_KEY

    def set_url(self):
        self.url = self.BASE_URL + self.endpoint
        if self.kwargs:
            self.url = self.url.format(**self.kwargs)

    def get(self):
        self.set_url()
        response = requests.get(self.url, self.kwargs)

        if response.status_code == 200:
            self.response.update(response.json())
            return self.clean_response_data()
        return response.raise_for_status()

    def previous_page(self):
        current_page = self.response.get('page')
        if current_page and current_page > 1:
            self.kwargs['page'] = current_page - 1
            self.get()
        return self.response

    def next_page(self):
        current_page = self.response.get('page')
        total_pages = self.response.get('total_pages')
        if current_page and current_page != total_pages:
            self.kwargs['page'] = current_page + 1
            self.get()
        return self.response

    def get_movie_db_image_url(self, url, size):
        return self.IMAGE_BASE_URL.format(size=size, url=url)

    def clean_item(self, item, image_size='w500'):
        # Formatting the data to be easier to use
        if item.get('poster_path'):
            item['poster_path'] = self.get_movie_db_image_url(item['poster_path'], image_size)
        if item.get('backdrop_path'):
            item['backdrop_path'] = self.get_movie_db_image_url(item['backdrop_path'], image_size)
        if item.get('imdb_id'):
            item['imdb_id'] = self.IMDB_URL.format(imdb_id=item.get('imdb_id'))
        if item.get('budget'):
            item['budget'] = formats.money(item['budget'])
        if item.get('revenue'):
            item['revenue'] = formats.money(item['revenue'])
        if item.get('release_date'):
            item['release_date'] = formats.date(item['release_date'])
        return item

    def clean_response_data(self):
        if self.response.get('results'):
            for item in self.response['results']:
                self.clean_item(item)
        return self.response
