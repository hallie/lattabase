from django.views.generic import DetailView

from movies_db import Movie


class MovieDetailView(DetailView):

    context_object_name = 'movie'
    pk_url_kwarg = 'movie_id'
    template_name = 'movies/detail.html'

    def get_object(self, queryset=None):
         movie_id = Movie(**self.kwargs)
         movie = movie_id.details()
         self.title = movie.get('title')
         return movie
