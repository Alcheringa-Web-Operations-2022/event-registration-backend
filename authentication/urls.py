
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('login/', views.Login, name='login'),
    path('logout/', views.logout,name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile_edit/', views.profileedit, name='profileedit'),
    # Password reset urls
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name="authentication/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('activate/<uidb64>/<token>', views.VerificationView.as_view(), name="activate"),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(
        template_name='authentication/password/password_reset_complete.html'), name='password_reset_complete'),
]
