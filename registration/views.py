from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,LasyaForm
from django.shortcuts import render, redirect, get_object_or_404, reverse, Http404
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from . import helpers
from .models import UserData,AdminEvent,LasyaRegistration
from django.utils import timezone

def closed(request):
    return render(request, 'registration/closed.html', {})

def registered(request):
    return render(request, 'registration/registered.html', {})

def lasyaRegistration(request):
    lasyaEvent = get_object_or_404(AdminEvent, title='lasya')
    if lasyaEvent.registrationActive:
        if request.user.is_authenticated:
            allRegistrations = LasyaRegistration.objects.all()
            isRegistered=False;
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered=True
            if isRegistered:
                return render(request, 'registration/registered.html',{})
            else:
                if request.method == "POST":
                    f = LasyaForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        reg.event = lasyaEvent
                        reg.save()
                        messages.add_message(request, messages.INFO, 'You have succesfully registered for Lasya')
                        return redirect('registration')
                else:
                    f = LasyaForm()
                return render(request, 'registration/lasyaRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for Lasya')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def redirectLogin(request):
    return redirect(to="login")


def signup(request):
    if request.method == 'POST':
        f = SignUpForm(request.POST)
        if f.is_valid():
            # send email verification now
            activation_key = helpers.generate_activation_key(username=request.POST['username'])

            subject = "Pravega Account Verification"

            message = '''\n
            Please visit the following link to verify your Pravega account \n\n{0}://{1}/registration/activate/account/?key={2}
                        '''.format(request.scheme, request.get_host(), activation_key)

            error = False

            try:
                send_mail(subject, message, settings.SERVER_EMAIL, [request.POST['email']])
                messages.add_message(request, messages.INFO, 'Account created! Click on the link sent to your email to activate the account')

            except:
                error = True
                messages.add_message(request, messages.INFO, 'Unable to send email verification. Please try again')

            if not error:
                u = User.objects.create_user(
                        request.POST['username'],
                        request.POST['email'],
                        request.POST['password1'],
                        is_active = 0
                )

                userdata = UserData.objects.create()
                userdata.activation_key = activation_key
                userdata.user = u
                userdata.save()

            return redirect('login')

    else:
        f = SignUpForm()

    return render(request, 'registration/signup.html', {'form': f})

def activateAccount(request):
    key = request.GET['key']
    if not key:
        raise Http404()

    r = get_object_or_404(UserData, activation_key=key, email_validated=False)
    r.user.is_active = True
    r.user.save()
    r.email_validated = True
    r.save()
    temp = 'Your account ' + r.user.username + ' is active!'

    messages.add_message(request, messages.INFO,  temp)
    return redirect('login')
