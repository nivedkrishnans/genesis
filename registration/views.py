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
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .event_confirmation_mails import event_confirmation_mail

def closed(request):
    return render(request, 'registration/closed.html', {})

def registered(request):
    return render(request, 'registration/registered.html', {})

def redirectRegistrationIndex(request):
    return redirect('registration')

def registration_index(request):
    eventDictionary=0
    userRegOpen=[]
    userRegClosed=[]
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
            userRegOpen.append(isRegistered)

        for i in closedEvents:
            eventTitle = i.title
            allRegistrations = eventDictionary[eventTitle].objects.all()
            isRegistered=False;
            for j in allRegistrations:
                if (request.user == j.user):
                    isRegistered=True
            userRegClosed.append(isRegistered)

    return render(request, 'registration/registration_index.html', {'userRegOpen':userRegOpen, 'userRegClosed':userRegClosed, 'openedEvents':openedEvents, 'closedEvents':closedEvents, 'notyetEvents':notyetEvents })

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
                        #checking if the video file was uploaded. if yes, we expect a MultiValueDictKeyError
                        videoFileAvailable = False
                        try:
                            if request.POST['videoFile']:
                                videoFileAvailable = False;
                        except:
                            videoFileAvailable = True;
                        #checking if either the video file or the link was obtained
                        if request.POST['videoFileLink'] or videoFileAvailable:
                            reg = f.save(commit=False)
                            reg.user = request.user
                            if event_confirmation_mail('Lasya',request):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully registered for Lasya')
                            return redirect('registration')
                        else:
                            messages.add_message(request, messages.INFO, 'Please upload video file or enter video link')
                            return render(request, 'registration/lasyaRegistration.html', {'form': f})
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
                        #checking if the video file was uploaded. if yes, we expect a MultiValueDictKeyError
                        videoFileAvailable = False
                        try:
                            if request.POST['videoFile']:
                                videoFileAvailable = False;
                        except:
                            videoFileAvailable = True;
                        #checking if either the video file or the link was obtained
                        if request.POST['videoFileLink'] or videoFileAvailable:
                            reg = f.save(commit=False)
                            reg.user = request.user
                            if event_confirmation_mail('Proscenium',request):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully registered for Proscenium')
                            return redirect('registration')
                        else:
                            messages.add_message(request, messages.INFO, 'Please upload video file or enter video link')
                            return render(request, 'registration/prosceniumRegistration.html', {'form': f})
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
                        if event_confirmation_mail('Footprints',request):
                            reg.confirmation_email_sent = True
                        reg.save()
                        messages.add_message(request, messages.INFO, 'You have succesfully registered for Footprints')
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
            activation_key = helpers.generate_activation_key(username=request.POST['email'])
            base_location = "{0}://{1}".format(request.scheme, request.get_host())
            subject = "Pravega Account Verification"
            name = str(request.POST['full_name'])
            confirm_url = "{0}://{1}/registration/activate/account/?key={2}".format(request.scheme, request.get_host(), activation_key)
            html_content = render_to_string('registration/email_templates/confirm_email.html', {'base_location':base_location,'confirm_url':confirm_url,'name':name}) # render with dynamic value
            #for text version of mail
            text_content = '''\n
                            Welcome, {3}. Glad to have you as a part of Pravega 2019!
                            Please activate your Pravega account by clicking on the link below
                            \n\n
                            {0}://{1}/registration/activate/account/?key={2}
                            \n \n Once confirmed you will be able to log into your Pravega account.
                            \n\n Best wishes,
                            \n Pravega Team.
                            '''.format(request.scheme, request.get_host(), activation_key,name)
            error = False

            try:
                msg = EmailMultiAlternatives(subject, text_content, settings.SERVER_EMAIL, [request.POST['email']])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                messages.add_message(request, messages.INFO, 'Account created! Click on the link sent to your email to activate your Pravega account')

            except:
                error = True
                messages.add_message(request, messages.INFO, 'Unable to send activation link. Please try again')

            if not error:
                u = User.objects.create_user(
                        request.POST['email'],
                        request.POST['email'],
                        request.POST['password1'],
                        is_active = 0
                )

                userdata = UserData.objects.create()
                userdata.activation_key = activation_key
                userdata.full_name = request.POST['full_name']
                userdata.institution = request.POST['institution']
                userdata.city = request.POST['city']
                userdata.email = request.POST['email']
                userdata.contact = request.POST['contact']
                userdata.create_date = timezone.now()
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
    temp = 'Your account ' + r.user.email + ' is active!'
    messages.add_message(request, messages.INFO,  temp)

    #email confirmation
    base_location = "{0}://{1}".format(request.scheme, request.get_host())
    subject = "Pravega Account Confirmed"
    name = str(r.user)
    html_content = render_to_string('registration/email_templates/account_confirmed.html', {'base_location':base_location,'name':name}) # render with dynamic value
    #for text version of mail
    text_content = '''\n
                    Hello, {2}. Your Pravega account is activated!
                    \n\n
                    You have successfully registered your account with us on Pravega.
                    \n\n Best wishes,
                    \n Pravega Team.
                    '''.format(request.scheme, request.get_host(),name)
    error = False
    msg = EmailMultiAlternatives(subject, text_content, settings.SERVER_EMAIL, [r.user.email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return redirect('login')
