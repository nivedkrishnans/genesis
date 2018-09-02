from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,LasyaForm,ProsceniumForm,FootprintsForm
from django.shortcuts import render, redirect, get_object_or_404, reverse, Http404
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from . import helpers
from .models import UserData,AdminEvent,LasyaRegistration,FootprintsRegistration,ProsceniumRegistration
from django.utils import timezone

def closed(request):
    return render(request, 'registration/closed.html', {})

def registered(request):
    return render(request, 'registration/registered.html', {})


def registration_index(request):
    eventDictionary=0
    userReg=[]
    openedEvents = AdminEvent.objects.filter(registrationStatus='opened')
    closedEvents = AdminEvent.objects.filter(registrationStatus='closed')
    notyetEvents = AdminEvent.objects.filter(registrationStatus='notyet')
    if request.user.is_authenticated:
        eventDictionary={
            'lasya':LasyaRegistration,
            'proscenium':ProsceniumRegistration,
            'footprints':FootprintsRegistration,
        }
        for i in openedEvents:
            eventTitle = i.title
            allRegistrations = eventDictionary[eventTitle].objects.all()
            isRegistered=False;
            for j in allRegistrations:
                if (request.user == j.user):
                    isRegistered=True
            userReg.append(isRegistered)

    return render(request, 'registration/registration_index.html', {'userReg':userReg, 'openedEvents':openedEvents, 'closedEvents':closedEvents, 'notyetEvents':notyetEvents })

def lasyaRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='lasya')
    if thisEvent.registrationStatus == 'opened':
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
                        reg.event = thisEvent
                        reg.save()
                        messages.add_message(request, messages.INFO, 'You have succesfully registered for Lasya')
                        subject = "Successfully registered for Lasya"
                        message = '''\n
                        You have successfully registered for Lasya. Will see you soon!
                        '''
                        send_mail(subject, message, settings.SERVER_EMAIL,[request.user.email])
                        return redirect('registration')
                else:
                    f = LasyaForm()
                return render(request, 'registration/lasyaRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for Lasya')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def prosceniumRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='proscenium')
    if thisEvent.registrationStatus == 'opened':
        if request.user.is_authenticated:
            allRegistrations = ProsceniumRegistration.objects.all()
            isRegistered=False;
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered=True
            if isRegistered:
                return render(request, 'registration/registered.html',{})
            else:
                if request.method == "POST":
                    f = ProsceniumForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        reg.event = thisEvent
                        reg.save()
                        messages.add_message(request, messages.INFO, 'You have succesfully registered for Proscenium')
                        subject = "Successfully registered for Proscenium"
                        message = '''\n
                        You have successfully registered for Proscenium. Will see you soon!
                        '''
                        send_mail(subject, message, settings.SERVER_EMAIL, [request.user.email])
                        return redirect('registration')
                else:
                    f = ProsceniumForm()
                return render(request, 'registration/prosceniumRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for Proscenium')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def footprintsRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='footprints')
    if thisEvent.registrationStatus == 'opened':
        if request.user.is_authenticated:
            allRegistrations = FootprintsRegistration.objects.all()
            isRegistered=False;
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered=True
            if isRegistered:
                return render(request, 'registration/registered.html',{})
            else:
                if request.method == "POST":
                    f = FootprintsForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        reg.event = thisEvent
                        reg.save()
                        messages.add_message(request, messages.INFO, 'You have succesfully registered for Footprints')
                        subject = "Successfully registered for Footprints"
                        message = '''\n
                        You have successfully registered for Footprints. Will see you soon!
                                    '''
                        send_mail(subject, message, settings.SERVER_EMAIL, [request.user.email])
                        return redirect('registration')
                else:
                    f = FootprintsForm()
                return render(request, 'registration/footprintsRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for Footprints')
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
