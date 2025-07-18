from django.shortcuts import render

# Create your views here.
from .models import Movie

from django.http import JsonResponse #queryset->python dict-> json response


def movie_list(request):
    movies = Movie.objects.all() # we want to use it as a json response 
    data= {
        'movies':list (movies.values()) # object list .values when used as a iterable gives dicts
    }# dict till here
    return JsonResponse(data)  #returning the json format of this 