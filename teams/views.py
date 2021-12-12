from django.shortcuts import render
from .forms import AddMemberForm
from .models import TeamMembers, Team
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def team_members(request):
    team = Team.objects.filter(leader=request.user).first()
    if request.method == 'POST':
        form = AddMemberForm(request.POST)
        name = form['name'].value()
        email = form['email'].value()
        phone = form['phone'].value()
        gender = form['gender'].value()
        if TeamMembers.objects.filter(email=email).first():
            team.members.add(TeamMembers.objects.filter(email=email).first())
        elif TeamMembers.objects.filter(phone=phone).first():
            team.members.add(TeamMembers.objects.filter(phone=phone).first())
        else:
            new_member = TeamMembers(name=name,email=email,phone=phone,gender=gender)
            new_member.save()
            team.members.add(new_member)
        team.save()
    else:
        form = AddMemberForm()
    all_members = []
    for member in team.members.all():
        all_members.append(member)
    return render(request,'teams/team_members.html',{'title':'Alcheringa | Teams','form':form,'team':all_members})