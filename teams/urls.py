from django.urls import path
from . import views 

urlpatterns = [
    path('', views.team_members, name='team'),
    path('member/<int:pk>', views.update_member, name='update-member'),
]
