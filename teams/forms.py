from django import forms
from phonenumber_field.formfields import PhoneNumberField

class MemberForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'border-b','size':'25','placeholder':'Enter Name'}))
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'class':'border-b','size':'25','placeholder':'Enter Phone Number'}))
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class':'border-b','size':'25','placeholder':'Enter Email'}))
    gender = forms.ChoiceField(choices=(('M','M'),('F','F')),widget=forms.Select(attrs={'class':'border-b text-gray-400 pr-36','width':'110%','placeholder':'Gender'}))