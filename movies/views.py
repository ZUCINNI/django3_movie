from django.views.generic import View, ListView, DetailView
from django.shortcuts import redirect
from movies.models import Movie
from .forms import ReviewForm


class MoviesView(ListView):
    """List of movies"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Detail of the Movie"""
    model = Movie
    slug_field = 'url'


class AddPost(View):
    """Adding Review"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
