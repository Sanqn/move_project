from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

from .models import Models
def index(request):
    movies = Models.objects.all()
    context = {
        'hello': 'List of movies',
        'movies': movies,
    }
    return render(request, 'movie_app/index.html', context=context)

def about_movie(request, id_movie:int):
    # movie = Models.objects.get(id=id_movie)
    movie = get_object_or_404(Models, id=id_movie)
    context = {
        'movie': movie,
        'about': 'About movie',
    }
    return render(request, 'movie_app/about_movie.html', context=context)