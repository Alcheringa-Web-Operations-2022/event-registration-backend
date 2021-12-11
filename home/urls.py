
from django.contrib import admin
from django.urls import path, include
from . import views as home_view

urlpatterns = [
    path('', home_view.home, name='home'),
]
