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
    memberemail = TeamMembers.objects.filter(
        email=request.POST.get('addemail'))
    if request.method == 'POST':
        if (memberemail.count() > 0):
            return HttpResponse('User with same email already exist')

        if(request.FILES.getlist('addimg')):
            TeamMembers(img=request.FILES.getlist('addimg')[0], name=request.POST.get('addname'),
                    email=request.POST.get('addemail'), phone=request.POST.get('addphone'), gender=request.POST.get('addgender')).save()
        else:
            TeamMembers(name=request.POST.get('addname'),
                        email=request.POST.get('addemail'), phone=request.POST.get('addphone'), gender=request.POST.get('addgender')).save()
            
        team = Team.objects.get(leader=request.user)
        team.members.add(TeamMembers.objects.get(
            email=request.POST.get('addemail')))
        team.save()
    return HttpResponse('OK')


@login_required(login_url='login')
def update_member(request):
    memberemail = TeamMembers.objects.filter(email=request.POST.get('editemail'))
    member = TeamMembers.objects.get(id=request.POST.get('editid'))
    if request.method == 'POST':
        if (memberemail.count() > 0 and member not in memberemail):
            return HttpResponse('User with same email already exist')

        if(request.FILES.getlist('editimg')):
            member.img = request.FILES.getlist('editimg')[0]
        member.name = request.POST.get('editname')
        member.email = request.POST.get('editemail')
        member.phone = request.POST.get('editphone')
        member.gender = request.POST.get('editgender')
        member.save()
    return HttpResponse('OK')


@login_required(login_url='login')
def remove_member(request):
    if request.POST["id"]:
        member = TeamMembers.objects.filter(id=request.POST["id"]).first()
        team=Team.objects.get(leader=request.user)
        team.members.remove(member)
        team.save()
        member.delete()
        return HttpResponse("ok")
