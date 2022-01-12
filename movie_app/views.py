from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Models
from django.db.models import F, Sum, Max, Min, Count, Avg

def index(request):
    movies = Models.objects.all() # sort by field order_by('rating', 'sum_money')
    # for movie in movies: #заполняем в бд колонку slug
    #     movie.save()
    mov = movies.aggregate(Avg('sum_money'), Count('name'))
    context = {
        'hello': 'List of movies',
        'movies': movies,
        'mov': mov,
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