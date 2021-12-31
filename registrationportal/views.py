from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def home(request):
    return redirect('showallcompetitions')

@login_required(login_url='login')
def rulebook(request):
    return render(request, 'competitions/rules.html')
