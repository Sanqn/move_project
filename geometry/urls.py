from django.urls import path, register_converter
from . import views



urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area, name='rectangle'),
    path('square/<int:width>', views.get_square_area, name='square'),
    path('circle/<int:radius>', views.get_circle_area, name='circle'),
    path('get_rectangle_area/<int:width>/<int:height>', views.new_get_rectangle_area),
    path('get_square_area/<int:width>', views.new_get_square_area),
    path('get_circle_area/<int:radius>', views.new_get_circle_area),
]