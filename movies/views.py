from django.shortcuts import render
from django.views.generic.base import View

from movies.models import Movie


class MoviesView(View):
    """List of movies"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {
            'movies': movies
        })
