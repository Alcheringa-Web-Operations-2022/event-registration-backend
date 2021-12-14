from django import forms
from competitions.models import CompTeam
from django.contrib.auth import get_user_model
User=get_user_model()
class CreateTeamForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = CompTeam
        fields = ['members', 'teamname']
    



