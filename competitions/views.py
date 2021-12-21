from django.shortcuts import render, redirect
from competitions.forms import CreateTeamForm
from django.contrib import messages
from competitions.models import CompTeam, Competition
from django.contrib.auth.decorators import login_required
from teams.models import Team
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
            form = CreateTeamForm(request.user, request.POST)
            if form.is_valid():
                if ((len(form.cleaned_data['members'])+1) > comp.max_members or (len(form.cleaned_data['members'])+1) < comp.min_members):
                    print(len(form.cleaned_data['members']))
                    print(comp.max_members)
                    messages.error(request, 'Not a valid range')
                else:
                    result = form.save(commit=False)
                    result.event = comp
                    result.leader = request.user
                    result.save()

                    form.save_m2m()
                    messages.success(
                        request, 'You have registered your team for this event successfully')
                    return redirect('showallcompetitions')

        else:
            form = CreateTeamForm(request.user)
    return render(request, 'competitions/compreg.html', {'comp': comp, 'form': form, 'team_members': team_members})
