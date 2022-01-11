from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

from .models import Models
def index(request):
    movies = Models.objects.order_by('-rating', '-sum_money') # sort by field order_by('rating', 'sum_money')
    # for movie in movies: #заполняем в бд колонку slug
    #     movie.save()
    context = {
        'hello': 'List of movies',
        'movies': movies,
    }
    return render(request, 'movie_app/index.html', context=context)

def about_movie(request, name_slug:str):
    # movie = Models.objects.get(id=id_movie)
    movie = get_object_or_404(Models, slug=name_slug)
    context = {
        'movie': movie,
        'about': 'About movie',
    }
    return render(request, 'movie_app/about_movie.html', context=context)