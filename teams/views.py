from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import TeamMembers, Team
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def team_members(request):
    team = Team.objects.filter(leader=request.user).first()
    all_members = []
    for member in team.members.all():
        all_members.append(member)
    return render(request, 'teams/team_members.html', {'team': all_members,'active_page':'team'})


@login_required(login_url='login')
def add_member(request):
    memberemail = TeamMembers.objects.filter(email=request.POST.get('email'))
    memberphone = TeamMembers.objects.filter(phone=request.POST.get('phone'))
    if request.method == 'POST':
        if (memberemail.count() > 0):
            return HttpResponse('User with same email already exist')

        if (memberphone.count() > 0):
            return HttpResponse('User with same phone already exist')

        TeamMembers(name=request.POST.get('name'),
                    email=request.POST.get('email'), phone=request.POST.get('phone'), gender=request.POST.get('gender')).save()
        team = Team.objects.get(leader=request.user)
        team.members.add(TeamMembers.objects.get(
            email=request.POST.get('email')))
        team.save()
    return HttpResponse('OK')


@login_required(login_url='login')
def update_member(request):
    memberemail = TeamMembers.objects.filter(email=request.POST.get('email'))
    memberphone = TeamMembers.objects.filter(phone=request.POST.get('phone'))
    member = TeamMembers.objects.get(id=request.POST.get('id'))
    if request.method == 'POST':
        if (memberemail.count() > 0 and member not in memberemail):
            return HttpResponse('User with same email already exist')

        if (memberphone.count() > 0 and member not in memberphone):
            return HttpResponse('User with same phone already exist')
        member.name = request.POST.get('name')
        member.email = request.POST.get('email')
        member.phone = request.POST.get('phone')
        member.gender = request.POST.get('gender')
        member.save()
    return HttpResponse('OK')


@login_required(login_url='login')
def remove_member(request):
    if request.POST["id"]:
        member = TeamMembers.objects.filter(id=request.POST["id"]).first()
        member.delete()
        return HttpResponse("ok")
