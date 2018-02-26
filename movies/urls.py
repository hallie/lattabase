from django.conf.urls import url

from movies.views import (
    MovieDetailView,
    MovieListView,
)


urlpatterns = [
    url(
        r'^search/?$',
        MovieListView.as_view(),
        name='movie-search',
    ),
    url(
        r'^(?P<movie_id>[\w-]+)/?$',
        MovieDetailView.as_view(),
        name='movie-id',
    ),
]
