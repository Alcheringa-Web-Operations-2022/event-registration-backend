
from django.contrib import admin
from django.urls import path, include
from . import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_view.Login, name='login'),
    path('register/', user_view.register, name='register'),
]
