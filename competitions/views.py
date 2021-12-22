from django.http.response import BadHeaderError
from django.shortcuts import render, redirect,HttpResponse
from django.template.loader import render_to_string
from competitions.forms import CreateTeamForm
from django.contrib import messages
from competitions.models import CompTeam, Competition
from django.contrib.auth.decorators import login_required
from teams.models import Team, TeamMembers
from django.core.mail import send_mail
import json
# Create your views here.


@login_required(login_url='login')
def showallcompetitions(request):
    # print(request.GET.get('module'))
    if(request.GET.get('module')):
        module_comp = Competition.objects.filter(module = request.GET.get('module'))
    else:
        module_comp = Competition.objects.filter(module = 'Dance')
    
    return render(request, 'competitions/allcomp.html', {'allcomp': module_comp, 'modulename' : request.GET.get('module')})


@login_required(login_url='login')
def registercompetition(request, slug):
    comp = Competition.objects.get(id=slug)
    check_unique = CompTeam.objects.filter(leader=request.user, event=comp)
    team_members = Team.objects.get(leader=request.user).members.all()
    if request.method != 'POST' and len(check_unique) > 0:
        messages.error(
            request, 'You have already registered your team for this event')
        return redirect('showallcompetitions')
    else:
        if request.method == 'POST':
            print(request.user)
            print(request.POST.get('members'))
            compteams = CompTeam.objects.create(event=comp, leader=request.user, teamname=request.POST['teamname'])
            team_members=[]
            for member in json.loads(request.POST.get('members')):
                print(str(member['id']))
                compteams.members.add(TeamMembers.objects.get(id=str(member['id'])))
                compteams.save()
                
            ######################### mail system ####################################
            # emailsend(comp, request.POST.get('members'))
            for user in json.loads(request.POST.get('members')):
                subject = "Event Registration Successful"
                email_template_name = "competitions/registration_email.txt"
                c = {
                        "name": user['name'],
                        "event": comp.event_name
                    }
                print(user['name'])
                print(comp.event_name)
                email = render_to_string(email_template_name, c)
                try:
                    send_mail(subject, email, 'Alcheringa Registration Portal', [
                                    user['email']], fail_silently=False)
                    print("done")
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            ##################################################################
            
            messages.success(request, 'You have registered your team for this event successfully')
            return HttpResponse("OK")
    return render(request, 'competitions/compreg.html', {'comp': comp,'team_members': team_members})


