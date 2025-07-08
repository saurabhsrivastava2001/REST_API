from django.http import HttpResponse
from django.shortcuts import render


def home (request):
    """
    Home view that returns a simple greeting.
    """
    return HttpResponse("Welcome to the Watchmate API!")