
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from authentication.models import NewUser
User=get_user_model()

class UserRegisterForm(UserCreationForm):

    class Meta:
        model =User
        fields = ['fullname',
                  'username',
                  'email',
                  'phone',
                  'collegename',
                 'city'
            
                  ]
