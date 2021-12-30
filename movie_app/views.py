from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


def index(request):
    context = {
        'hello': 'Hello my friend'
    }
    return render(request, 'movie_app/index.html', context=context)
