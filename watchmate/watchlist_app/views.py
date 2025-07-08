from django.shortcuts import render

# Create your views here.
from .models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'watchlist_app/movie_list.html', {'movies': movies})
