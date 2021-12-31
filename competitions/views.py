from django.http.response import BadHeaderError
from django.shortcuts import render, redirect, HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from competitions.models import CompTeam, Competition, Module, SubmitPerformance
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import json
from teams.models import Team, TeamMembers

# Create your views here.


@login_required(login_url='login')
def showallcompetitions(request):
    modulequery = request.GET.get('module') or 'dance'
    module_comp = Competition.objects.all()
    module = None
    if modulequery:
        module = Module.objects.get(
            module_query_name_without_spaces_all_small=modulequery)
        module_comp = module_comp.filter(module=module)

    modules = Module.objects.all()
    if module:
        modulename = module.module_query_name_without_spaces_all_small
    return render(request, 'competitions/allcomp.html', {'allmod': modules, 'allcomp': module_comp, 'modulename': modulename,'active_page':'competitions'})


@login_required(login_url='login')
def viewrules(request, slug):
    comp = Competition.objects.get(id=slug)
    return render(request, 'competitions/rules.html', {'comp': comp,'active_page':'rulebook'})


@login_required(login_url='login')
def registercompetition(request, slug):
    comp = Competition.objects.get(id=slug)
    reg_teams = CompTeam.objects.filter(leader=request.user, event=comp)
    team = Team.objects.get(leader=request.user)
    members_reg = []
    for rteam in reg_teams.all():
        members_reg += [member.id for member in rteam.members.all()]

    members_reg = set(members_reg)
    team_members = team.members.exclude(id__in=members_reg)
    if(len(team_members)<comp.min_members or len(team_members)==0):
        messages.error(request,'Not enough members to register')
        return redirect('showallcompetitions')
    if request.method == 'POST':
        ######################### saving team ####################################

        compteams = CompTeam.objects.create(
            event=comp, leader=request.user)
        team_members = []
        for member in json.loads(request.POST.get('members')):
            print(str(member['id']))
            compteams.members.add(
                TeamMembers.objects.get(id=str(member['id'])))
            compteams.save()

        ######################### saving previpus performance form ####################################
        if request.POST.get('link') or request.POST.get('description'):
            prev = SubmitPerformance.objects.create(event=comp, team=compteams, link=request.POST.get(
                'link'), description=request.POST.get('description'))
            prev.save()
        ######################### mail system ####################################
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

        messages.success(
            request, 'You have registered your team for this event successfully')
        return HttpResponse("OK")
    return render(request, 'competitions/compreg.html', {'comp': comp, 'team_members': team_members,'active_page':'competitions' })
