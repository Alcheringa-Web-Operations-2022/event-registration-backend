from django.shortcuts import render, redirect
from competitions.forms import CreateTeamForm
from django.contrib import messages
from competitions.models import CompTeam, Competition

# Create your views here.


def showallcompetitions(request):
    allcomp = Competition.objects.all()
    return render(request, 'competitions/allcomp.html', {'allcomp': allcomp})


def registercompetition(request, slug):
    comp = Competition.objects.get(id=slug)
    check_unique=CompTeam.objects.filter(leader=request.user,event=comp)
    if request.method != 'POST' and len(check_unique) > 0:
        messages.error(request, 'You have already registered your team for this event')
        return redirect('showallcompetitions')
    else:
        if request.method == 'POST':
            form = CreateTeamForm(request.user, request.POST)
            if form.is_valid():
                
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
    return render(request, 'competitions/compreg.html', {'comp': comp, 'form': form})