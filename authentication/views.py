
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,get_user_model
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import NewUser
User = get_user_model()
########### register here #####################################


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            # htmly = get_template('authentication/Email.html')
            # d = {'username': username}
            # subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(
            #     subject, html_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            ##################################################################
            messages.success(
                request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'authentication/register.html', {'form': form, 'title': 'reqister here'})

################ login forms###################################################


def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        user = NewUser.objects.filter(email=email)

        if user:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', 'home'))
            else:
                print("errrr")
                messages.error(
                    request, 'Password is incorrect for the email address entered ')
        else:
            print("email not registered")
            messages.error(request, 'Email is not registered')

    
    return render(request, 'authentication/login.html', { 'title': 'log in'})


def logout(request):
    django_logout(request)
    return redirect('home')
