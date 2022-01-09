from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

def get_rectangle_area(request, width:int, height:int):
    return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {width*height}')

def new_get_rectangle_area(request, width:int, height:int):
    new_url = reverse('rectangle', args=[width, height])
    return HttpResponseRedirect(new_url)

def get_square_area(request, width:int):
    return HttpResponse(f'Площадь квадрата размером {width}х{width} равна {width*width}')

def new_get_square_area(request, width:int):
    new_url = reverse('square', args=[width])
    return HttpResponseRedirect(new_url)

def get_circle_area(request, radius:int):
    return HttpResponse(f'Площадь круга размером {radius} равна {2*3.14*(radius**2)}')

def new_get_circle_area(request, radius:int):
    new_url = reverse('circle', args=[radius])
    return HttpResponseRedirect(new_url)