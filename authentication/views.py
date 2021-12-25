from competitions.models import Module
from django.utils.html import strip_tags
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views import View
from .utils import token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from .forms import UserRegisterForm, UserUpdateForm
from django.core.mail import send_mail
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

    return render(request, 'authentication/login.html', {'title': 'log in'})


def password_reset_request(request):
    User = get_user_model()
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(
                Q(email=data, provider="email"))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "authentication/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': get_current_site(request).domain,
                        'site_name': 'Alcheringa Web Operations',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'https',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'Alcheringa Registration Portal', [
                                  user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(
                        request, ("Password reset mail sent successfully."))
            else:
                messages.error(request, ("Email not registered with us"))
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="authentication/password/password_reset.html", context={"password_reset_form": password_reset_form})


@login_required(login_url='login')
def profile(request):
    modules=Module.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(
            request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your Profile has been updated!')
            return redirect('profile')
        print(u_form.errors)
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'authentication/profile.html', {'heading': 'Profile', 'form': u_form,'modules':modules,'totalmodules':modules.count()})

def logout(request):
    django_logout(request)
    return redirect('home')
