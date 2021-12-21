
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.showallcompetitions, name='showallcompetitions'),
    path('register/<slug>',
         views.registercompetition, name='registercomp'),
]
