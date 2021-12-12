from django import forms
from phonenumber_field.formfields import PhoneNumberField

class AddMemberForm(forms.Form):
    name = forms.CharField(label='Enter name', max_length=100)
    phone = PhoneNumberField(label='Enter phone number')
    email = forms.EmailField(label='Enter email', max_length=100)
    gender = forms.CharField(label='Enter gender', max_length=1)