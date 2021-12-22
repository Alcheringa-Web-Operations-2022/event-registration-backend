
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from authentication.models import NewUser
from phonenumber_field.formfields import PhoneNumberField
User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form__field', 'placeholder': 'Email *'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form__field', 'placeholder': 'Username *'}))
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form__field', 'placeholder': 'Full Name *'}))
    collegename = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form__field', 'placeholder': 'College Name *'}))
    city = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form__field', 'placeholder': 'City *'}))
    phone = PhoneNumberField(widget=forms.TextInput(attrs={
        'class': 'input_field', 'placeholder': 'Phone Number (e.g. +12125552368) *'}), label="Phone number (e.g. +12125552368)", )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input_field', 'placeholder': 'Password *'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input_field', 'placeholder': 'Confirm your Password *'}))

    class Meta:
        model = User
        fields = ['fullname',
                  'username',
                  'email',
                  'phone',
                  'collegename',
                  'city'
                  ]


class UserUpdateForm(forms.ModelForm):

    phone = PhoneNumberField(widget=forms.TextInput(
    ), label="Phone number (e.g. +12125552368)", required=False)

    class Meta:
        model = User
        fields = ['img', 'fullname',
                  'username',
                  'phone',
                  'collegename',
                  'city'
                  ]
