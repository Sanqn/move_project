from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

from .models import Models
def index(request):
    movies = Models.objects.all()
    context = {
        'hello': 'List of movies',
        'movies': movies
    }
    return render(request, 'movie_app/index.html', context=context)
