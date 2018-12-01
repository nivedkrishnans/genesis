from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404, reverse, Http404
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from . import helpers
from .models import *
from originals.models import InOtherWord
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .event_confirmation_mails import event_confirmation_mail
from django.http import JsonResponse
from datetime import datetime
import json



def closed(request):
    return render(request, 'registration/closed.html', {})

def decoherencePrelimsCrashed(request):
    return render(request, 'registration/decoherencePrelimsCrashed.html', {})

def registered(request):
    return render(request, 'registration/registered.html', {})

def redirectRegistrationIndex(request):
    return redirect('registration')

def registration_index(request):
    # campusAmbassador is not an event
    campusAmbassadorEvent = AdminEvent.objects.filter(title='Campus Ambassadors').first()

    #distionary of events and their models
    eventDictionary={
        'ibmhackathon':IBMHackathonRegistration,
        'isc':ISCRegistration,
        'Campus Ambassadors':CampusAmbassador,
        'lasya':LasyaRegistration,
        'lasyaSolo':LasyaSoloRegistration,
        'lasyaGroup':LasyaGroupRegistration,
        'proscenium':ProsceniumRegistration,
        'footprints':FootprintsRegistration,
        'battle of bands':BattleOfBandsRegistration,
        'decoherence':DecoherenceRegistration,
        'debubulary':DebubularyRegistration,
        'wikimediaphotography':WikimediaPhotographyRegistration,
        'pis':PISRegistration,
        'vignettora':VignettoraRegistration,
        'etc':ETCRegistration,
        'cryptothlon':CryptothlonRegistration,
        'chemisticon':ChemisticonRegistration,
        'sciencejournalism':ScienceJournalismRegistration,
    }

    #inotherwords
    iow_isactive = list(InOtherWord.objects.filter(active=True))

    # converting the following querysets to list so that remove function  can be called
    openedEvents = list(AdminEvent.objects.filter(registrationStatus='opened').order_by('-priority'))
    closedEvents = list(AdminEvent.objects.filter(registrationStatus='closed').order_by('-priority'))
    notyetEvents = list(AdminEvent.objects.filter(registrationStatus='notyet').order_by('-priority'))

    #showing which events where Registered
    registeredEvents = []
    registeredEventsString = ''

    if request.user.is_authenticated:
        for i in openedEvents:
            allRegistrations = eventDictionary[i.title].objects.all()
            isRegistered=False;
            for j in allRegistrations:
                if (request.user == j.user) and j.isSubmit:
                    isRegistered=True
            if isRegistered:
                registeredEvents.append(i)

        for i in closedEvents:
            allRegistrations = eventDictionary[i.title].objects.all()
            isRegistered=False;
            for j in allRegistrations:
                if (request.user == j.user) and j.isSubmit:
                    isRegistered=True
            if isRegistered:
                registeredEvents.append(i)

        for i in notyetEvents:
            allRegistrations = eventDictionary[i.title].objects.all()
            isRegistered=False;
            for j in allRegistrations:
                if (request.user == j.user) and j.isSubmit:
                    isRegistered=True
            if isRegistered:
                registeredEvents.append(i)

        if len(registeredEvents) != 0:
            if len(registeredEvents) == 1:
                registeredEventsString = registeredEventsString + (registeredEvents[0].displayTitle)
            else:
                j = 1       #loop variable
                for i in registeredEvents:
                    registeredEventsString = registeredEventsString + (i.displayTitle)
                    if j == (len(registeredEvents) - 1):
                        registeredEventsString = registeredEventsString + " and "
                    elif j == len(registeredEvents):
                        continue
                    else:
                        registeredEventsString = registeredEventsString + ", "
                    j+=1
            registeredEventsString = "<p class='center'> You have successfully registered for " +  registeredEventsString + "</p>"

    #removes the campusAmbassador from the lists of Events
    if campusAmbassadorEvent in openedEvents :openedEvents.remove(campusAmbassadorEvent)
    if campusAmbassadorEvent in closedEvents :closedEvents.remove(campusAmbassadorEvent)
    if campusAmbassadorEvent in notyetEvents :notyetEvents.remove(campusAmbassadorEvent)

    return render(request, 'registration/registration_index.html', {'iow_isactive':iow_isactive,'campusAmbassadorEvent':campusAmbassadorEvent,'registeredEventsString':registeredEventsString, 'openedEvents':openedEvents, 'closedEvents':closedEvents, 'notyetEvents':notyetEvents })

def lasyaRegistrationRedirect(request):
    return redirect('lasya')

def lasyaRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='lasya')
    if thisEvent.registrationStatus == 'opened':
        if request.user.is_authenticated:
            allRegistrations = LasyaRegistration.objects.all()
            isRegistered = False
            thisInstance = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{})
                else:
                    f = LasyaForm(instance=thisInstance)
                    if request.method == "POST":
                        f = LasyaForm(request.POST, request.FILES,instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                #checking if the video file was uploaded.
                                if f["videoFileLink"].value() or f["videoFile"].value() :
                                    thisInstance.isSubmit = True
                                    thisInstance.submit_date = timezone.now()
                                    if event_confirmation_mail('Lasya',request.POST['email'],request):
                                        thisInstance.confirmation_email_sent = True
                                    thisInstance.save()
                                    messages.add_message(request, messages.INFO, 'You have succesfully submitted your Lasya Registration Form')
                                    return redirect('registration')
                                else:
                                    thisInstance.last_modify_date = timezone.now()
                                    thisInstance.save()
                                    f = LasyaForm(instance=thisInstance)
                                    messages.add_message(request, messages.INFO, 'Please upload video file or enter video link')
                                    return render(request, 'registration/lasyaRegistration.html', {'form': f})

                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Lasya Registration Form')
                                f = LasyaForm(instance=thisInstance)
                                return render(request, 'registration/lasyaRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = LasyaForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        if request.POST.get("submit"):
                            #checking if either the video file or the link was obtained
                            if f["videoFileLink"].value() or f["videoFile"].value():
                                reg.isSubmit = True
                                reg.submit_date = timezone.now()
                                if event_confirmation_mail('Lasya',request.POST['email'],request):
                                    reg.confirmation_email_sent = True
                                reg.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Lasya Registration Form')
                            else:
                                messages.add_message(request, messages.INFO, 'Please upload video file or enter video link' )
                                return render(request, 'registration/lasyaRegistration.html', {'form': f})
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Lasya Registration Form')
                            return render(request, 'registration/lasyaRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = LasyaForm()
            return render(request, 'registration/lasyaRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for Lasya')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def lasyaSoloRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='lasyaSolo')
    if thisEvent.registrationStatus == 'opened':
        if request.user.is_authenticated:
            initialValues={}
            allRegistrations = LasyaSoloRegistration.objects.all()
            allUserData = UserData.objects.all()
            isRegistered = False
            thisInstance = False
            thisUserData = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            for i in allUserData:
                if (request.user == i.user):
                    thisUserData = i
            if thisUserData:
                initialValues={"full_name": thisUserData.full_name,
                "institution": thisUserData.institution,
                "city":thisUserData.city ,
                "email": thisUserData.email,
                "contact": thisUserData.contact}
            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{})
                else:
                    f = LasyaSoloForm(instance=thisInstance)
                    if request.method == "POST":
                        f = LasyaSoloForm(request.POST, request.FILES,instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                #checking if the video file was uploaded.
                                if f["videoFileLink"].value() or f["videoFile"].value() :
                                    thisInstance.isSubmit = True
                                    thisInstance.submit_date = timezone.now()
                                    if event_confirmation_mail('Lasya (Solo)',request.POST['email'],request):
                                        thisInstance.confirmation_email_sent = True
                                    thisInstance.save()
                                    messages.add_message(request, messages.INFO, 'You have succesfully submitted your Lasya (Solo) Registration Form')
                                    return redirect('registration')
                                else:
                                    thisInstance.last_modify_date = timezone.now()
                                    thisInstance.save()
                                    f = LasyaSoloForm(instance=thisInstance)
                                    messages.add_message(request, messages.INFO, 'Please upload video file or enter video link')
                                    return render(request, 'registration/lasyaSoloRegistration.html', {'form': f})

                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Lasya (Solo) Registration Form')
                                f = LasyaSoloForm(instance=thisInstance)
                                return render(request, 'registration/lasyaSoloRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = LasyaSoloForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        if request.POST.get("submit"):
                            #checking if either the video file or the link was obtained
                            if f["videoFileLink"].value() or f["videoFile"].value():
                                reg.isSubmit = True
                                reg.submit_date = timezone.now()
                                if event_confirmation_mail('Lasya (Solo)',request.POST['email'],request):
                                    reg.confirmation_email_sent = True
                                reg.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Lasya (Solo) Registration Form')
                            else:
                                messages.add_message(request, messages.INFO, 'Please upload video file or enter video link' )
                                return render(request, 'registration/lasyaSoloRegistration.html', {'form': f})
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Lasya (Solo) Registration Form')
                            return render(request, 'registration/lasyaSoloRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = LasyaSoloForm(initial=initialValues)
            return render(request, 'registration/lasyaSoloRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for Lasya')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})


def lasyaGroupRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='lasyaGroup')
    if thisEvent.registrationStatus == 'opened':
        if request.user.is_authenticated:
            allRegistrations = LasyaGroupRegistration.objects.all()
            isRegistered = False
            thisInstance = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{})
                else:
                    f = LasyaGroupForm(instance=thisInstance)
                    if request.method == "POST":
                        f = LasyaGroupForm(request.POST, request.FILES,instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                #checking if the video file was uploaded.
                                if f["videoFileLink"].value() or f["videoFile"].value() :
                                    thisInstance.isSubmit = True
                                    thisInstance.submit_date = timezone.now()
                                    if event_confirmation_mail('Lasya (Group)',request.POST['email'],request):
                                        thisInstance.confirmation_email_sent = True
                                    thisInstance.save()
                                    messages.add_message(request, messages.INFO, 'You have succesfully submitted your Lasya (Group) Registration Form')
                                    return redirect('registration')
                                else:
                                    thisInstance.last_modify_date = timezone.now()
                                    thisInstance.save()
                                    f = LasyaGroupForm(instance=thisInstance)
                                    messages.add_message(request, messages.INFO, 'Please upload video file or enter video link')
                                    return render(request, 'registration/lasyaGroupRegistration.html', {'form': f})

                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Lasya (Group) Registration Form')
                                f = LasyaGroupForm(instance=thisInstance)
                                return render(request, 'registration/lasyaGroupRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = LasyaGroupForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        if request.POST.get("submit"):
                            #checking if either the video file or the link was obtained
                            if f["videoFileLink"].value() or f["videoFile"].value():
                                reg.isSubmit = True
                                reg.submit_date = timezone.now()
                                if event_confirmation_mail('Lasya (Group)',request.POST['email'],request):
                                    reg.confirmation_email_sent = True
                                reg.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Lasya (Group) Registration Form')
                            else:
                                messages.add_message(request, messages.INFO, 'Please upload video file or enter video link' )
                                return render(request, 'registration/lasyaGroupRegistration.html', {'form': f})
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Lasya (Group) Registration Form')
                            return render(request, 'registration/lasyaGroupRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = LasyaGroupForm()
            return render(request, 'registration/lasyaGroupRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for Lasya')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def chemisticonRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='chemisticon')

    if thisEvent.registrationStatus == 'opened':
        f=ChemisticonForm()
        if request.user.is_authenticated:
            allRegistrations =ChemisticonRegistration.objects.all()
            allUserData = UserData.objects.all()
            isRegistered = False
            thisInstance = False
            thisUserData = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            for i in allUserData:
                if (request.user == i.user):
                    thisUserData = i

            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{'form':f})
                else:
                    f = ChemisticonForm(instance=thisInstance)
                    if request.method == "POST":
                        f = ChemisticonForm(request.POST, request.FILES,instance=thisInstance )
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                thisInstance.isSubmit = True
                                thisInstance.submit_date = timezone.now()
                                if event_confirmation_mail('Chemisticon',request.POST['email1'],request,request.POST['email2'],request.POST['email3']):
                                    thisInstance.confirmation_email_sent = True
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Chemisticon Event Registration Form')
                                return redirect('registration')
                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Chemisticon Event Registration Form')
                                f =ChemisticonForm(instance=thisInstance)
                                return render(request, 'registration/chemisticonRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = ChemisticonForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user

                        if request.POST.get("submit"):
                            reg.isSubmit = True
                            reg.submit_date = timezone.now()
                            if event_confirmation_mail('Chemisticon',request.POST['email1'],request.POST['email2'],request.POST['email3'],request):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your Chemisticon Event Registration Form')
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Chemisticon Event Registration Form')
                            return render(request, 'registration/chemisticonRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = ChemisticonForm(initial={
                    "institution": thisUserData.institution,
                    "city":thisUserData.city ,
                    "email": thisUserData.email,
                    "contact": thisUserData.contact})
            return render(request, 'registration/chemisticonRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for the Chemisticon')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})


def sciencejournalismRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='sciencejournalism')

    if thisEvent.registrationStatus == 'opened':
        f = ScienceJournalismForm()
        if request.user.is_authenticated:
            allRegistrations = ScienceJournalismRegistration.objects.all()
            allUserData = UserData.objects.all()
            isRegistered = False
            isSubmit = False
            thisInstance = False
            thisUserData = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            for i in allUserData:
                if (request.user == i.user):
                    thisUserData = i
            if isRegistered:
                if thisInstance.isSubmit:
                    isSubmit = True
                    return render(request, 'registration/registered.html',{ 'form':f})
                else:
                    f = ScienceJournalismForm(instance=thisInstance)
                    if request.method == "POST":
                        f = ScienceJournalismForm(request.POST, instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                if f['articleFile'].value():
                                    thisInstance.isSubmit = True
                                    thisInstance.submit_date = timezone.now()
                                    if event_confirmation_mail('Science Journalism',request.POST['email'],request):
                                        thisInstance.confirmation_email_sent = True
                                    thisInstance.save()
                                    messages.add_message(request, messages.INFO, 'You have succesfully submitted your Science Journalism Registration Form')
                                    return redirect('registration')
                                else:
                                    messages.add_message(request, messages.INFO, 'Please upload an article' )
                                    return render(request, 'registration/sciencejournalismRegistration.html', {'form': f})
                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Science Journalism Registration Form')
                                f = ScienceJournalismForm(instance=thisInstance)
                                return render(request, 'registration/sciencejournalismRegistration.html',{'form':f})
            else:
                if request.method == "POST":
                    f = ScienceJournalismForm(request.POST)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        if request.POST.get("submit"):
                            reg.isSubmit = True
                            reg.submit_date = timezone.now()
                            if event_confirmation_mail('Science Journalism',request.POST['email'],request):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your Science Journalism Registration Form')
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Science Journalism Registration Form')
                            return render(request, 'registration/sciencejournalismRegistration.html',{'form':f})
                        return redirect('registration')
                else:
                    f = ScienceJournalismForm(initial = {"full_name":thisUserData.full_name,"institution":thisUserData.institution,"city":thisUserData.city,"email":thisUserData.email})
            return render(request, 'registration/ScienceJournalismRegistration.html',{'form':f})

        return render(request, 'registration/ScienceJournalismRegistration.html',{'form':f})
    else:
        return render(request, 'registration/closed.html',{})


def prosceniumRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='proscenium')
    if thisEvent.registrationStatus == 'opened':
        if request.user.is_authenticated:
            allRegistrations = ProsceniumRegistration.objects.all()
            isRegistered = False
            thisInstance = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{})
                else:
                    f = ProsceniumForm(instance=thisInstance)
                    if request.method == "POST":
                        f = ProsceniumForm(request.POST, request.FILES,instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                #checking if the video file was uploaded.
                                if f["videoFileLink"].value() or f["videoFile"].value() :
                                    thisInstance.isSubmit = True
                                    thisInstance.submit_date = timezone.now()
                                    if event_confirmation_mail('Proscenium',request.POST['email'],request):
                                        thisInstance.confirmation_email_sent = True
                                    thisInstance.save()
                                    messages.add_message(request, messages.INFO, 'You have succesfully submitted your Proscenium Registration Form')
                                    return redirect('registration')
                                else:
                                    thisInstance.last_modify_date = timezone.now()
                                    thisInstance.save()
                                    f = ProsceniumForm(instance=thisInstance)
                                    messages.add_message(request, messages.INFO, 'Please upload video file or enter video link')
                                    return render(request, 'registration/prosceniumRegistration.html', {'form': f})

                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Proscenium Registration Form')
                                f =ProsceniumForm(instance=thisInstance)
                                return render(request, 'registration/prosceniumRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = ProsceniumForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        if request.POST.get("submit"):
                            #checking if either the video file or the link was obtained
                            if f["videoFileLink"].value() or f["videoFile"].value():
                                reg.isSubmit = True
                                reg.submit_date = timezone.now()
                                if event_confirmation_mail('Proscenium',request.POST['email'],request):
                                    reg.confirmation_email_sent = True
                                reg.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Proscenium Registration Form')
                            else:
                                messages.add_message(request, messages.INFO, 'Please upload video file or enter video link' )
                                return render(request, 'registration/prosceniumRegistration.html', {'form': f})
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Proscenium Registration Form')
                            return render(request, 'registration/prosceniumRegistration.html', {'form': f})
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
            isRegistered = False
            thisInstance = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{})
                else:
                    f = FootprintsForm(instance=thisInstance)
                    if request.method == "POST":
                        f = FootprintsForm(request.POST, request.FILES,instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                thisInstance.isSubmit = True
                                thisInstance.submit_date = timezone.now()
                                if event_confirmation_mail('Footprints',request.POST['email'],request):
                                    thisInstance.confirmation_email_sent = True
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Footprints Registration Form')
                                return redirect('registration')
                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Footprints Registration Form')
                                f =FootprintsForm(instance=thisInstance)
                                return render(request, 'registration/footprintsRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = FootprintsForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        if request.POST.get("submit"):
                            reg.isSubmit = True
                            reg.submit_date = timezone.now()
                            if event_confirmation_mail('Footprints',request.POST['email'],request):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your Footprints Registration Form')
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Footprints Registration Form')
                            return render(request, 'registration/footprintsRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = FootprintsForm()
            return render(request, 'registration/footprintsRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for Footprints')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def battleofbandsRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='battle of bands')
    if thisEvent.registrationStatus == 'opened':
        if request.user.is_authenticated:
            allRegistrations = BattleOfBandsRegistration.objects.all()
            isRegistered = False
            thisInstance = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{})
                else:
                    f = BattleOfBandsForm(instance=thisInstance)
                    if request.method == "POST":
                        f = BattleOfBandsForm(request.POST, request.FILES,instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                #checking if the audio/video file was uploaded.
                                if f["audioVideoFileLink"].value() or f["audioVideoFile"].value() :
                                    thisInstance.isSubmit = True
                                    thisInstance.submit_date = timezone.now()
                                    if event_confirmation_mail('Battle Of Bands',request.POST['email'],request):
                                        thisInstance.confirmation_email_sent = True
                                    thisInstance.save()
                                    messages.add_message(request, messages.INFO, 'You have succesfully submitted your Battle Of Bands Registration Form')
                                    return redirect('registration')
                                else:
                                    thisInstance.last_modify_date = timezone.now()
                                    thisInstance.save()
                                    f = BattleOfBandsForm(instance=thisInstance)
                                    messages.add_message(request, messages.INFO, 'Please upload audio/video file or enter audio/video link')
                                    return render(request, 'registration/battleofbandsRegistration.html', {'form': f})

                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Battle Of Bands Registration Form')
                                f =BattleOfBandsForm(instance=thisInstance)
                                return render(request, 'registration/battleofbandsRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = BattleOfBandsForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        if request.POST.get("submit"):
                            #checking if either the audio/video file or the link was obtained
                            if f["audioVideoFileLink"].value() or f["audioVideoFile"].value():
                                reg.isSubmit = True
                                reg.submit_date = timezone.now()
                                if event_confirmation_mail('BattleOfBands',request.POST['email'],request):
                                    reg.confirmation_email_sent = True
                                reg.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Battle Of Bands Registration Form')
                            else:
                                messages.add_message(request, messages.INFO, 'Please upload audio/video file or enter audio/video link' )
                                return render(request, 'registration/battleofbandsRegistration.html', {'form': f})
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Battle Of Bands Registration Form')
                            return render(request, 'registration/battleofbandsRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = BattleOfBandsForm()
            return render(request, 'registration/battleofbandsRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for Battle Of Bands')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def decoherenceRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='decoherence')
    if thisEvent.registrationStatus == 'opened':
        if request.user.is_authenticated:
            allRegistrations = DecoherenceRegistration.objects.all()
            isRegistered = False
            thisInstance = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{})
                else:
                    f = DecoherenceForm(instance=thisInstance)
                    if request.method == "POST":
                        f = DecoherenceForm(request.POST, request.FILES,instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                thisInstance.isSubmit = True
                                thisInstance.submit_date = timezone.now()
                                if event_confirmation_mail('Vignettora',request.POST['email1'],request,request.POST['email2']):
                                    thisInstance.confirmation_email_sent = True
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Decoherence Registration Form')
                                return redirect('registration')
                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Decoherence Registration Form')
                                f =DecoherenceForm(instance=thisInstance)
                                return render(request, 'registration/decoherenceRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = DecoherenceForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        if request.POST.get("submit"):
                            reg.isSubmit = True
                            reg.submit_date = timezone.now()
                            if event_confirmation_mail('Vignettora',request.POST['email1'],request,request.POST['email2']):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your Decoherence Registration Form')
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Decoherence Registration Form')
                            return render(request, 'registration/decoherenceRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = DecoherenceForm()
            return render(request, 'registration/decoherenceRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for Decoherence')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def debubularyRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='debubulary')

    if thisEvent.registrationStatus == 'opened':
        f=DebubularyForm()
        if request.user.is_authenticated:
            allRegistrations = DebubularyRegistration.objects.all()
            allUserData = UserData.objects.all()
            isRegistered = False
            thisInstance = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            for i in allUserData:
                if (request.user == i.user):
                    thisUserData = i

            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{'form':f})
                else:
                    f = DebubularyForm(instance=thisInstance)
                    if request.method == "POST":
                        f = DebubularyForm(request.POST, request.FILES,instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                thisInstance.isSubmit = True
                                thisInstance.submit_date = timezone.now()
                                if event_confirmation_mail('Debubulary',request.POST['email1'],request,request.POST['email2']):
                                    thisInstance.confirmation_email_sent = True
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Debubulary Registration Form')
                                return redirect('registration')
                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Debubulary Registration Form')
                                f =DebubularyForm(instance=thisInstance)
                                return render(request, 'registration/debubularyRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = DebubularyForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        if request.POST.get("submit"):
                            reg.isSubmit = True
                            reg.submit_date = timezone.now()
                            if event_confirmation_mail('Debubulary',request.POST['email1'],request,request.POST['email2']):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your Debubulary Registration Form')
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Debubulary Registration Form')
                            return render(request, 'registration/debubularyRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = DebubularyForm(initial={
                    "institution": thisUserData.institution,
                    "city":thisUserData.city ,
                    "email": thisUserData.email,
                    "contact": thisUserData.contact})
            return render(request, 'registration/debubularyRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for Debubulary')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def cryptothlonRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='cryptothlon')
    if thisEvent.registrationStatus == 'opened':
        f=CryptothlonForm()
        if request.user.is_authenticated:
            allRegistrations = CryptothlonRegistration.objects.all()
            allUserData = UserData.objects.all()
            isRegistered = False
            thisInstance = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            for i in allUserData:
                if (request.user == i.user):
                    thisUserData = i

            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{'form':f})
                else:
                    f = CryptothlonForm(instance=thisInstance)
                    if request.method == "POST":
                        f = CryptothlonForm(request.POST, request.FILES,instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                thisInstance.isSubmit = True
                                thisInstance.submit_date = timezone.now()
                                if event_confirmation_mail('Cryptothlon',request.POST['email1'],request,request.POST['email2']):
                                    thisInstance.confirmation_email_sent = True
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Cryptothlon Registration Form')
                                return redirect('registration')
                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Cryptothlon Registration Form')
                                f =CryptothlonForm(instance=thisInstance)
                                return render(request, 'registration/cryptothlonRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = CryptothlonForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        if request.POST.get("submit"):
                            reg.isSubmit = True
                            reg.submit_date = timezone.now()
                            if event_confirmation_mail('Cryptothlon',request.POST['email1'],request,request.POST['email2']):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your Cryptothlon Registration Form')
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Cryptothlon Registration Form')
                            return render(request, 'registration/cryptothlonRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = CryptothlonForm(initial={})
            return render(request, 'registration/cryptothlonRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for Debubulary')
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

def campusambassadors(request):
    thisEvent = get_object_or_404(AdminEvent, title='Campus Ambassadors')
    isRegistered = False
    isSubmit = False
    isOpen = thisEvent.registrationStatus == 'opened'
    f = CampusAmbassadorForm()
    if request.user.is_authenticated:
        allRegistrations = CampusAmbassador.objects.all()
        allUserData = UserData.objects.all()
        thisInstance = False
        thisUserData = False
        for i in allRegistrations:
            if (request.user == i.user):
                isRegistered = True
                thisInstance = i
        for i in allUserData:
            if (request.user == i.user):
                thisUserData = i
        if isRegistered:
            if thisInstance.isSubmit:
                isSubmit = True
                return render(request, 'registration/campusAmbassador.html',{'isSubmit':isSubmit, 'isOpen':isOpen, 'form':f})
            else:
                f = CampusAmbassadorForm(instance=thisInstance)
                if request.method == "POST":
                    f = CampusAmbassadorForm(request.POST, instance=thisInstance)
                    if f.is_valid():
                        thisInstance = f.save(commit=False)
                        if request.POST.get("submit"):
                            thisInstance.isSubmit = True
                            thisInstance.submit_date = timezone.now()
                            if event_confirmation_mail('Campus Ambassador Program',request.POST['email'],request):
                                thisInstance.confirmation_email_sent = True
                            thisInstance.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your Campus Ambassador Registration Form')
                            return redirect('registration')
                        else:
                            thisInstance.last_modify_date = timezone.now()
                            thisInstance.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully modified your Campus Ambassador Registration Form')
                            f = CampusAmbassadorForm(instance=thisInstance)
                            return render(request, 'registration/campusAmbassador.html',{'isSubmit':isSubmit, 'isOpen':isOpen,'form':f})
        else:
            if request.method == "POST":
                f = CampusAmbassadorForm(request.POST)
                if f.is_valid():
                    reg = f.save(commit=False)
                    reg.user = request.user
                    if request.POST.get("submit"):
                        reg.isSubmit = True
                        reg.submit_date = timezone.now()
                        if event_confirmation_mail('Campus Ambassador Program',request.POST['email'],request):
                            reg.confirmation_email_sent = True
                        reg.save()
                        messages.add_message(request, messages.INFO, 'You have succesfully submitted your Campus Ambassador Registration Form')
                    else:
                        reg.last_modify_date = timezone.now()
                        reg.save()
                        messages.add_message(request, messages.INFO, 'You have succesfully saved your Campus Ambassador Registration Form')
                        return render(request, 'registration/campusAmbassador.html',{'isSubmit':isSubmit, 'isOpen':isOpen,'form':f})
                    return redirect('registration')
            else:
                f = CampusAmbassadorForm(initial = {"full_name":thisUserData.full_name,"institution":thisUserData.institution,"city":thisUserData.city,"email":thisUserData.email,"contactForCalls":thisUserData.contact,})
        return render(request, 'registration/campusAmbassador.html',{'isSubmit':isSubmit,'isOpen':isOpen, 'form':f})

    return render(request, 'registration/campusAmbassador.html',{'isSubmit':isSubmit, 'isOpen':isOpen, 'form':f})

def wikimediaphotographyRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='wikimediaphotography')
    if thisEvent.registrationStatus == 'opened':
        if request.user.is_authenticated:
            allRegistrations = WikimediaPhotographyRegistration.objects.all()
            allUserData = UserData.objects.all()
            isRegistered = False
            thisInstance = False
            thisUserData = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            for i in allUserData:
                if (request.user == i.user):
                    thisUserData = i
            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{})
                else:
                    f = WikimediaPhotographyForm(instance=thisInstance)
                    if request.method == "POST":
                        f = WikimediaPhotographyForm(request.POST, request.FILES,instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                thisInstance.isSubmit = True
                                thisInstance.submit_date = timezone.now()
                                if event_confirmation_mail('Wikimedia Photography Event',thisUserData.email,request):
                                    thisInstance.confirmation_email_sent = True
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Wikimedia Photography Event Registration Form')
                                return redirect('registration')
                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Wikimedia Photography Event Registration Form')
                                f =WikimediaPhotographyForm(instance=thisInstance)
                                return render(request, 'registration/wikimediaPhotographyRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = WikimediaPhotographyForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        reg.institution = thisUserData.institution
                        reg.city = thisUserData.city
                        reg.email = thisUserData.email
                        reg.contact = thisUserData.contact
                        if request.POST.get("submit"):
                            reg.isSubmit = True
                            reg.submit_date = timezone.now()
                            if event_confirmation_mail('Wikimedia Photography Event',thisUserData.email,request):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your Wikimedia Photography Event Registration Form')
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Wikimedia Photography Event Registration Form')
                            return render(request, 'registration/wikimediaPhotographyRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = WikimediaPhotographyForm()
            return render(request, 'registration/wikimediaPhotographyRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for the Wikimedia Photography Event')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def vignettoraRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='vignettora')

    if thisEvent.registrationStatus == 'opened':
        f=VignettoraForm()
        if request.user.is_authenticated:

            allRegistrations =VignettoraRegistration.objects.all()
            allUserData = UserData.objects.all()
            isRegistered = False
            thisInstance = False
            thisUserData=False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            for i in allUserData:
                if (request.user == i.user):
                    thisUserData = i

            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{'form':f})
                else:
                    f = VignettoraForm(instance=thisInstance)
                    if request.method == "POST":
                        f =  VignettoraForm(request.POST, request.FILES)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                thisInstance.isSubmit = True
                                thisInstance.submit_date = timezone.now()
                                if event_confirmation_mail(' Vignettora Event',thisUserData.email,request):
                                    thisInstance.confirmation_email_sent = True
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Vignettora Registration Form')
                                return redirect('registration')
                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Vignettora Registration Form')
                                f =VignettoraForm()
                                return render(request, 'registration/vignettoraRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f =VignettoraForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        if request.POST.get("submit"):
                            reg.isSubmit = True
                            reg.submit_date = timezone.now()
                            if event_confirmation_mail('Vignettora Event',request.POST['email'],request):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your Vignettora Registration Form')
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Vignettora Registration Form')
                            return render(request, 'registration/vignettoraRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = VignettoraForm(initial= {"full_name":thisUserData.full_name,"institution":thisUserData.institution,"city":thisUserData.city,"email":thisUserData.email,"contactForCalls":thisUserData.contact,})
            return render(request, 'registration/vignettoraRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for the Vignettora Event')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def etcRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='etc')
    if thisEvent.registrationStatus == 'opened':
        f=ETCForm()
        if request.user.is_authenticated:
            allRegistrations =ETCRegistration.objects.all()
            allUserData = UserData.objects.all()
            isRegistered = False
            thisInstance = False
            thisUserData = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            for i in allUserData:
                if (request.user == i.user):
                    thisUserData = i
            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{'form':f})
                else:
                    f = ETCForm(instance=thisInstance)
                    if request.method == "POST":
                        f = ETCForm(request.POST, request.FILES,instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                thisInstance.isSubmit = True
                                thisInstance.submit_date = timezone.now()
                                if event_confirmation_mail('Explain The Concept Event',request.POST['email'],request):
                                    thisInstance.confirmation_email_sent = True
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Explain The Concept Event Registration Form')
                                return redirect('registration')
                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Explain The Concept Event Registration Form')
                                f =ETCForm(instance=thisInstance)
                                return render(request, 'registration/etcRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = ETCForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user

                        if request.POST.get("submit"):
                            reg.isSubmit = True
                            reg.submit_date = timezone.now()
                            if event_confirmation_mail('Explain The Concept Event',thisUserData.email,request):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your Explain The Concept Event Registration Form')
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Explain The Concept Event Registration Form')
                            return render(request, 'registration/etcRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = ETCForm(initial= {"full_name":thisUserData.full_name,"institution":thisUserData.institution,"city":thisUserData.city,"email":thisUserData.email,"contactForCalls":thisUserData.contact,})
            return render(request, 'registration/etcRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for the Explain The Concept Event')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def iscRegistration(request):

    thisEvent = get_object_or_404(AdminEvent, title='isc')
    if thisEvent.registrationStatus == 'opened':
        f=ISCForm()
        if request.user.is_authenticated:
            allRegistrations =ISCRegistration.objects.all()
            allUserData = UserData.objects.all()
            isRegistered = False
            thisInstance = False
            thisUserData = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            for i in allUserData:
                if (request.user == i.user):
                    thisUserData = i
            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{'form':f})
                else:
                    f = ISCForm(instance=thisInstance)
                    if request.method == "POST":
                        f = ISCForm(request.POST, request.FILES,instance=thisInstance )
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                thisInstance.isSubmit = True
                                thisInstance.submit_date = timezone.now()
                                if event_confirmation_mail('Inter-School Talent Contest',request.POST['email'],request):
                                    thisInstance.confirmation_email_sent = True
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Inter-School Talent Contest Event Registration Form')
                                return redirect('registration')
                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Inter-School Talent Contest Event Registration Form')
                                f =ISCForm(instance=thisInstance)
                                return render(request, 'registration/iscRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = ISCForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user

                        if request.POST.get("submit"):
                            reg.isSubmit = True
                            reg.submit_date = timezone.now()
                            if event_confirmation_mail('Inter-School Talent Contest',thisUserData.email,request):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your Inter-School Talent Contest Event Registration Form')
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Inter-School Talent Contest Event Registration Form')
                            return render(request, 'registration/iscRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = ISCForm(initial= {"full_name":thisUserData.full_name,"institution":thisUserData.institution,"city":thisUserData.city,"email":thisUserData.email,"contactForCalls":thisUserData.contact,})
            return render(request, 'registration/iscRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for the Inter-School Talent Contest')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def ibmhackathonRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='ibmhackathon')

    if thisEvent.registrationStatus == 'opened':
        f = IBMHackathonForm()
        if request.user.is_authenticated:
            allRegistrations = IBMHackathonRegistration.objects.all()
            allUserData = UserData.objects.all()
            isRegistered = False
            isSubmit = False
            thisInstance = False
            thisUserData = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i

            for i in allUserData:
                if (request.user == i.user):
                    thisUserData = i
            if isRegistered:
                if thisInstance.isSubmit:
                    isSubmit = True
                    return render(request, 'registration/registered.html',{'form':f})
                else:
                    f = IBMHackathonForm(instance=thisInstance)
                    if request.method == "POST":
                        f = IBMHackathonForm(request.POST, instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                thisInstance.isSubmit = True
                                thisInstance.submit_date = timezone.now()
                                if event_confirmation_mail('IBM Hackathon',request.POST['email'],request):
                                    thisInstance.confirmation_email_sent = True
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your IBM Hackathon Registration Form')
                                return redirect('registration')
                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your IBM Hackathon Registration Form')
                                f = IBMHackathonForm(instance=thisInstance)
                                return render(request, 'registration/ibmhackathonRegistration.html',{'form':f})
            else:
                if request.method == "POST":
                    f = IBMHackathonForm(request.POST)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        if request.POST.get("submit"):
                            reg.isSubmit = True
                            reg.submit_date = timezone.now()
                            if event_confirmation_mail('IBM Hackathon',request.POST['email'],request):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your IBM Hackathon Registration Form')
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your IBM Hackathon Registration Form')
                            return render(request, 'registration/ibmhackathonRegistration.html',{'form':f})
                        return redirect('registration')
                else:
                    f = IBMHackathonForm(initial = {"full_name":thisUserData.full_name,"institution":thisUserData.institution,"city":thisUserData.city,"email":thisUserData.email,"contactForCalls":thisUserData.contact,})
            return render(request, 'registration/ibmhackathonRegistration.html',{ 'form':f})

        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for the IBM Hackathon')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})


def pisRegistration(request):
    thisEvent = get_object_or_404(AdminEvent, title='pis')
    if thisEvent.registrationStatus == 'opened':
        if request.user.is_authenticated:
            allRegistrations = PISRegistration.objects.all()
            allUserData = UserData.objects.all()
            isRegistered = False
            thisInstance = False
            thisUserData = False
            for i in allRegistrations:
                if (request.user == i.user):
                    isRegistered = True
                    thisInstance = i
            for i in allUserData:
                if (request.user == i.user):
                    thisUserData = i
            if isRegistered:
                if thisInstance.isSubmit:
                    return render(request, 'registration/registered.html',{})
                else:
                    f = PISForm(instance=thisInstance)
                    if request.method == "POST":
                        f = PISForm(request.POST, request.FILES,instance=thisInstance)
                        if f.is_valid():
                            thisInstance = f.save(commit=False)
                            if request.POST.get("submit"):
                                thisInstance.isSubmit = True
                                thisInstance.submit_date = timezone.now()
                                if event_confirmation_mail('Pravega Innovation Summit',thisUserData.email,request,thisInstance.member1email,thisInstance.member2email,thisInstance.member3email,thisInstance.member1name,thisInstance.member2name,thisInstance.member3name,):
                                    thisInstance.confirmation_email_sent = True
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Pravega Innovation Summit Registration Form')
                                return redirect('registration')
                            else:
                                thisInstance.last_modify_date = timezone.now()
                                thisInstance.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully modified your Pravega Innovation Summit Registration Form')
                                f =PISForm(instance=thisInstance)
                                return render(request, 'registration/pisRegistration.html', {'form': f})
            else:
                if request.method == "POST":
                    f = PISForm(request.POST, request.FILES)
                    if f.is_valid():
                        reg = f.save(commit=False)
                        reg.user = request.user
                        reg.institution = thisUserData.institution
                        reg.city = thisUserData.city
                        reg.email = thisUserData.email
                        reg.contact = thisUserData.contact
                        if request.POST.get("submit"):
                            reg.isSubmit = True
                            reg.submit_date = timezone.now()
                            if event_confirmation_mail('Pravega Innovation Summit',thisUserData.email,request,reg.member1email,reg.member2email,reg.member3email,reg.member1name,reg.member2name,reg.member3name,):
                                reg.confirmation_email_sent = True
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully submitted your Pravega Innovation Summit Registration Form')
                        else:
                            reg.last_modify_date = timezone.now()
                            reg.save()
                            messages.add_message(request, messages.INFO, 'You have succesfully saved your Pravega Innovation Summit Registration Form')
                            return render(request, 'registration/pisRegistration.html', {'form': f})
                        return redirect('registration')
                else:
                    f = PISForm()
            return render(request, 'registration/pisRegistration.html', {'form': f})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to register for the Pravega Innovation Summit')
            return redirect('login')
    else:
        return render(request, 'registration/closed.html',{})

def decoherencePrelims(request):
    try:
        startTime = list(StatusDates.objects.filter(title='decoherencePrelimsStart'))[0].dtValue
    except:
        startTime = 0
    try:
        endTime = list(StatusDates.objects.filter(title='decoherencePrelimsEnd'))[0].dtValue
    except:
        endTime = 0
    currentTime = timezone.now();
    subjectiveQuestions = list(DecoherenceSubjectiveQuestion.objects.order_by('qNo'))

    # we want objectiveQuestions[25] with false if the qNo is absent
    objectiveQuestions = [False]*25
    for i in range(0,24):
        try:
            objectiveQuestions[i] = list(DecoherenceObjectiveQuestion.objects.filter(qNo = (i+1)))[0]
        except:
            objectiveQuestions[i] = False

    objectiveQuestionsImages = [False] * 26     #so that in the 26th loop, ie., subjective question, no error occurs
    for i in range(0,24):
        if objectiveQuestions[i]:
            if objectiveQuestions[i].image:
                objectiveQuestionsImages[i] = (objectiveQuestions[i].image.url)

    #whether or not the exam is activate
    examStarted = False
    examEnded = False
    if startTime<=currentTime:
        examStarted = True
    if endTime<=currentTime:
        examEnded = True
    dateBegin=json.dumps(startTime.isoformat())
    dateEnd=json.dumps(endTime.isoformat())
    f = DecoherencePrelimsForm()        #keeping this line here to maintain f as an iterable
    if examStarted:
        if request.user.is_authenticated:
            allResponses = DecoherencePrelim.objects.all()
            allUserData = UserData.objects.all()
            allDecoherenceRegistrations = DecoherenceRegistration.objects.all()
            isResponded = False
            isDecoherenceRegistered = False
            thisInstance = False
            thisDecoherenceRegistration = False
            thisUserData = False
            for i in allDecoherenceRegistrations:
                if (request.user == i.user):
                    isDecoherenceRegistered = True
                    thisDecoherenceRegistration = i
            if isDecoherenceRegistered:
                for i in allResponses:
                    if (request.user == i.user):
                        isResponded = True
                        thisInstance = i
                for i in allUserData:
                    if (request.user == i.user):
                        thisUserData = i
                if isResponded:
                    if thisInstance.isSubmit:
                        return render(request, 'registration/decoherencePrelimsSubmitted.html',{})
                    else:
                        f = DecoherencePrelimsForm(instance=thisInstance)
                        if request.method == "POST":
                            f = DecoherencePrelimsForm(request.POST, request.FILES,instance=thisInstance)
                            if f.is_valid():
                                thisInstance = f.save(commit=False)
                                if request.POST.get("submit"):
                                    thisInstance.isSubmit = True
                                    thisInstance.submit_date = timezone.now()
                                    #if event_confirmation_mail('Pravega Innovation Summit',thisUserData.email,request,thisInstance.member1email,thisInstance.member2email,thisInstance.member3email,thisInstance.member1name,thisInstance.member2name,thisInstance.member3name,):
                                    #    thisInstance.confirmation_email_sent = True
                                    thisInstance.save()
                                    messages.add_message(request, messages.INFO, 'You have succesfully submitted your Decoherence Prelims Responses')
                                    return redirect('registration')
                                else:
                                    thisInstance.modifyTimes = thisInstance.modifyTimes + "\n" + str(timezone.now())
                                    thisInstance.save()
                                    messages.add_message(request, messages.INFO, 'You have succesfully saved your Decoherence Prelims Responses')
                                    f = DecoherencePrelimsForm(instance=thisInstance)
                                    return render(request, 'registration/decoherencePrelims.html', {'form': f,'dateBegin':dateBegin,'dateEnd':dateEnd, 'examEnded':examEnded, 'examStarted':examStarted, 'startTime':startTime, 'endTime':endTime, 'currentTime':currentTime, 'objectiveQuestions':objectiveQuestions, 'subjectiveQuestions':subjectiveQuestions, 'objectiveQuestionsImages':objectiveQuestionsImages})
                else:
                    if request.method == "POST":
                        f = DecoherencePrelimsForm(request.POST, request.FILES)
                        if f.is_valid():
                            reg = f.save(commit=False)
                            reg.user = request.user
                            reg.institution = thisUserData.institution
                            reg.city = thisUserData.city
                            reg.email = thisUserData.email
                            reg.decoherenceRegistration = thisDecoherenceRegistration
                            reg.teamName = thisDecoherenceRegistration.teamName
                            if request.POST.get("submit"):
                                reg.isSubmit = True
                                reg.submit_date = timezone.now()
                                #if event_confirmation_mail('Pravega Innovation Summit',thisUserData.email,request,reg.member1email,reg.member2email,reg.member3email,reg.member1name,reg.member2name,reg.member3name,):
                                #    reg.confirmation_email_sent = True
                                reg.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully submitted your Decoherence Prelims Responses')
                            else:
                                reg.modifyTimes = reg.modifyTimes + "\n" + str(timezone.now())
                                reg.save()
                                messages.add_message(request, messages.INFO, 'You have succesfully saved your Decoherence Prelims Responses')
                                return render(request, 'registration/decoherencePrelims.html', {'form': f,'dateBegin':dateBegin,'dateEnd':dateEnd, 'examEnded':examEnded, 'examStarted':examStarted, 'startTime':startTime, 'endTime':endTime, 'currentTime':currentTime, 'objectiveQuestions':objectiveQuestions, 'subjectiveQuestions':subjectiveQuestions, 'objectiveQuestionsImages':objectiveQuestionsImages})
                            return redirect('registration')
                    else:
                        f = DecoherencePrelimsForm()
                return render(request, 'registration/decoherencePrelims.html', {'form': f,'dateBegin':dateBegin,'dateEnd':dateEnd, 'examEnded':examEnded, 'examStarted':examStarted, 'startTime':startTime, 'endTime':endTime, 'currentTime':currentTime, 'objectiveQuestions':objectiveQuestions, 'subjectiveQuestions':subjectiveQuestions, 'objectiveQuestionsImages':objectiveQuestionsImages})
            else:
                return render(request, 'registration/decoherenceNotRegistered.html',{})

        else:
            messages.add_message(request, messages.INFO, 'Please log in to participate in the Decoherence Prelims')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return render(request, 'registration/decoherencePrelims.html',{'form': f,'dateBegin':dateBegin,'dateEnd':dateEnd, 'examEnded':examEnded, 'examStarted':examStarted, 'startTime':startTime, 'endTime':endTime, 'currentTime':currentTime, 'objectiveQuestions':objectiveQuestions, 'subjectiveQuestions':subjectiveQuestions, 'objectiveQuestionsImages':objectiveQuestionsImages})
        else:
            messages.add_message(request, messages.INFO, 'Please log in to participate in the Decoherence Prelims')
            return redirect('login')

def time(request):
    try:
        startTime = list(StatusDates.objects.filter(title='decoherencePrelimsStart'))[0].dtValue
    except:
        startTime = 0
    try:
        endTime = list(StatusDates.objects.filter(title='decoherencePrelimsEnd'))[0].dtValue
    except:
        endTime = 0
    dateBegin=json.dumps(startTime.isoformat())
    dateEnd=json.dumps(endTime.isoformat())
    return render(request,'registration/time.html',{'dateBegin':dateBegin,'dateEnd':dateEnd})

def getServerTime(request):
    return JsonResponse({'serverTime': timezone.now().isoformat()})
