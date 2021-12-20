from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import TeamMembers, Team
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def team_members(request):
    team = Team.objects.filter(leader=request.user).first()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        name = form['name'].value()
        email = form['email'].value()
        phone = form['phone'].value()
        gender = form['gender'].value()
        flag=0
        for member in team.members.all():
            if member.email==email or member.phone==phone:
                messages.error(request,"Member already exists in your team")
                flag=1
                break 
        if flag==0:
            new_member = TeamMembers(name=name,email=email,phone=phone,gender=gender)
            new_member.save()
            team.members.add(new_member)
            team.save()
    else:
        form = MemberForm()
    all_members = []
    for member in team.members.all():
        all_members.append(member)
    return render(request,'teams/team_members.html',{'title':'Alcheringa | Teams','form':form,'team':all_members})


@login_required(login_url='login')
def update_member(request,id):
    team = Team.objects.filter(leader=request.user).first()
    all_members = []
    for member in team.members.all():
        all_members.append(member)
    member = TeamMembers.objects.filter(id=id).first()
    if request.method == 'POST':
        if '_remove' in request.POST:
            member.delete()
        else:
            form = MemberForm(request.POST)
            member.name = form['name'].value()
            member.email = form['email'].value()
            member.phone = form['phone'].value()
            member.gender = form['gender'].value()
            member.save()
        return redirect('team')
    else:
        form = MemberForm()
        form.fields['name'].widget.attrs['value'] = member.name
        form.fields['email'].widget.attrs['value'] = member.email
        form.fields['phone'].widget.attrs['value'] = member.phone
        form.fields['gender'].widget.attrs['value'] = member.gender
    return render(request,'teams/update_member.html',{'title':'Alcheringa | Teams','form':form,'member':member,'team':all_members})
