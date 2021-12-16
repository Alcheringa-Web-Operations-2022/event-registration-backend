from django.shortcuts import render,redirect
from competitions.forms import CreateTeamForm
from django.contrib import messages
from competitions.models import Competition

# Create your views here.


def showallcompetitions(request):
    allcomp = Competition.objects.all()
    return render(request, 'competitions/allcomp.html', {'allcomp': allcomp})


def registercompetition(request, slug):
    comp = Competition.objects.get(id=slug)
    
    if request.method == 'POST':
        form = CreateTeamForm(request.user,request.POST)
        if form.is_valid():
            if (len(request.POST.get('members'))<=comp.max_members):
                print(comp.max_members)
                messages.error(request,'Maxmimum member limit exceeded')
            else:
                result=form.save(commit=False)
                result.event = comp
            
                result.save()
                form.save_m2m()
                return redirect(request.META['HTTP_REFERER'])
        
    else:
        form = CreateTeamForm(request.user)
    return render(request, 'competitions/compreg.html', {'comp': comp, 'form': form})
