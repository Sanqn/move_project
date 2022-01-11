from django.urls import path, register_converter
from . import views



urlpatterns = [
    path('', views.index),  # dynamic URLS
    # path('movie/<int:id_movie>', views.about_movie, name='url_detail')  # dynamic URLS
    path('movie/<str:name_slug>', views.about_movie, name='url_detail')  # dynamic URLS
]