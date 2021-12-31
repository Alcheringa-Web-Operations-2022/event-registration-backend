from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_members, name='team'),
    path('member/add', views.add_member, name='add-member'),
    path('member/update', views.update_member, name='update-member'),
    path('members/remove', views.remove_member, name='remove-member'),
]
