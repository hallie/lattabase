from django.views.generic import ListView

from movies_db import (
    MoviePopular,
    SearchMovie,
)


class MovieListView(ListView):

    context_object_name = 'movies'
    template_name = 'movies/list.html'
    title = 'Search'

    def get_context_data(self, **kwargs):
        context_data = super(MovieListView, self).get_context_data(**kwargs)
        context_data['title'] = self.title
        return context_data

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            search_movie = SearchMovie(query=query)
            return search_movie.get()
        movie_popular = MoviePopular()
        return movie_popular.get()
