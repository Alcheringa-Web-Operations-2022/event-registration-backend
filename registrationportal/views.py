from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def home(request):
    return redirect('showallcompetitions')

@login_required(login_url='login')
def rulebook(request):
<<<<<<< HEAD
    return render(request, 'competitions/rules.html',{'active_page':'rulebooklet'})
=======
    return render(request, 'rules.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'contactus.html')
>>>>>>> 9498543f694601d239e306246a6adc25ce41dd06
