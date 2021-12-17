
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('login/', views.Login, name='login'),
    path('logout/', views.logout,name='logout'),
    path('register/', views.register, name='register'),
]
