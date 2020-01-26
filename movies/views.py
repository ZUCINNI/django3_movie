from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.models import Movie


class MoviesView(ListView):
    """List of movies"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = 'movies/movie_list.html'


class MovieDetailView(DetailView):
    """Detail of the Movie"""
    model = Movie
    slug_field = 'url'

