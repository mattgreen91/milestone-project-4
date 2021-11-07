from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('googlef6bdd563d9a6019b.html', views.google, name='google')
]

