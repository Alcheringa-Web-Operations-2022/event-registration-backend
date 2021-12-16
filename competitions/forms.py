from django import forms
from competitions.models import CompTeam
from django.contrib.auth import get_user_model

from teams.models import Team, TeamMembers
User = get_user_model()


class CreateTeamForm(forms.ModelForm):
    
    team = Team.objects.none()
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = CompTeam
        fields = ['members', 'teamname']

    def __init__(self, user, * args, ** kwargs):
        super(CreateTeamForm, self).__init__(* args, ** kwargs)
        self.fields['members'].queryset = Team.objects.get(leader=user).members
        
