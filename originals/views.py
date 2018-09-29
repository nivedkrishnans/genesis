from django.shortcuts import render, redirect, get_object_or_404, reverse, Http404
from django.utils import timezone
from .models import *
from .forms import *
from registration.models import UserData
from django.contrib import messages
from .response_submitted_mails import response_submitted_mail

def archive(request):
	images =  ArchiveImage.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
	return render(request, 'originals/archive.html', {'images':images})

def originals(request):
	images =  ScienceQuizzine.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
	videos =  LetsTalkScience.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
	return render(request, 'originals/originals.html', {'images':images, 'videos':videos})

def InOtherWords(request):
    IOW_active = InOtherWord.objects.filter(publish_date__lte=timezone.now(), active=True).order_by('-publish_date')
    IOW_inactive = InOtherWord.objects.filter(publish_date__lte=timezone.now(), active=False).order_by('-publish_date')
    return render(request, 'originals/inotherwords.html', {'IOW_active':IOW_active , 'IOW_inactive':IOW_inactive})


def IOW_challenge01(request):
	thisEvent = get_object_or_404(InOtherWord, challengeNo=1)
	if thisEvent.active:
		if request.user.is_authenticated:
			allResponses = InOtherWordsChallenge01.objects.all()
			allUserData = UserData.objects.all()
			isResponded = False
			thisInstance = False
			thisUserData = False
			for i in allResponses:
				if (request.user == i.user):
					isResponded = True
					thisInstance = i
			for i in allUserData:
				if (request.user == i.user):
					thisUserData = i
			if isResponded:
				if thisInstance.isSubmit:
					return render(request, 'originals/iow_responded.html',{})
				else:
					f = InOtherWordsChallengeForm01(instance=thisInstance)
					if request.method == "POST":
						#request.FILES if needed
						f = InOtherWordsChallengeForm01(request.POST, instance=thisInstance)
						if f.is_valid():
							thisInstance = f.save(commit=False)
							if request.POST.get("submit"):
								thisInstance.isSubmit = True
								thisInstance.submit_date = timezone.now()
								if response_submitted_mail(thisEvent.title,thisUserData.email,request):
								    thisInstance.confirmation_email_sent = True
								thisInstance.user = thisUserData.user
								thisInstance.name = thisUserData.full_name
								thisInstance.institution = thisUserData.institution
								thisInstance.city = thisUserData.city
								thisInstance.email = thisUserData.email
								thisInstance.contact = thisUserData.contact
								thisInstance.save()
								messages.add_message(request, messages.INFO, 'You have succesfully submitted your \'In Other Words\' Challenge \'' + thisEvent.title + '\' Responses')
								return redirect('registration')
							else:
								thisInstance.last_modify_date = timezone.now()
								thisInstance.user = thisUserData.user
								thisInstance.name = thisUserData.full_name
								thisInstance.institution = thisUserData.institution
								thisInstance.city = thisUserData.city
								thisInstance.email = thisUserData.email
								thisInstance.contact = thisUserData.contact
								thisInstance.save()
								messages.add_message(request, messages.INFO, 'You have succesfully modified your  \'In Other Words\' Challenge \'' + thisEvent.title + '\' Responses')
								f =InOtherWordsChallengeForm01(instance=thisInstance)
								return render(request, 'originals/iow_challenge01.html', {'form': f})
			else:
				if request.method == "POST":
					#request.FILES if needed
					f = InOtherWordsChallengeForm01(request.POST)
					if f.is_valid():
						reg = f.save(commit=False)
						reg.user = request.user
						if request.POST.get("submit"):
							reg.isSubmit = True
							reg.submit_date = timezone.now()
							if response_submitted_mail(thisEvent.title,thisUserData.email,request):
							    reg.confirmation_email_sent = True
							reg.user = thisUserData.user
							reg.name = thisUserData.full_name
							reg.institution = thisUserData.institution
							reg.city = thisUserData.city
							reg.email = thisUserData.email
							reg.contact = thisUserData.contact
							reg.save()
							messages.add_message(request, messages.INFO, 'You have succesfully submitted your \'In Other Words\' Challenge \'' + thisEvent.title + '\' Responses')
						else:
							reg.last_modify_date = timezone.now()
							reg.user = thisUserData.user
							reg.name = thisUserData.full_name
							reg.institution = thisUserData.institution
							reg.city = thisUserData.city
							reg.email = thisUserData.email
							reg.contact = thisUserData.contact
							reg.save()
							messages.add_message(request, messages.INFO, 'You have succesfully saved your \'In Other Words\' Challenge \'' + thisEvent.title + '\' Responses')
							return render(request, 'originals/iow_challenge01.html', {'form': f})
						return redirect('registration')
				else:
					f = InOtherWordsChallengeForm01()
			return render(request, 'originals/iow_challenge01.html', {'form': f})
		else:
			messages.add_message(request, messages.INFO, 'Please log in to participate in \'In Other Words\' ')
			return redirect('login')
	else:
		return render(request, 'originals/iow_closed.html',{})




def IOW_challenge02(request):
	thisEvent = get_object_or_404(InOtherWord, challengeNo=2)
	if thisEvent.active:
		if request.user.is_authenticated:
			allResponses = InOtherWordsChallenge02.objects.all()
			allUserData = UserData.objects.all()
			isResponded = False
			thisInstance = False
			thisUserData = False
			for i in allResponses:
				if (request.user == i.user):
					isResponded = True
					thisInstance = i
			for i in allUserData:
				if (request.user == i.user):
					thisUserData = i
			if isResponded:
				if thisInstance.isSubmit:
					return render(request, 'originals/iow_responded.html',{})
				else:
					f = InOtherWordsChallengeForm02(instance=thisInstance)
					if request.method == "POST":
						#request.FILES if needed
						f = InOtherWordsChallengeForm02(request.POST, instance=thisInstance)
						if f.is_valid():
							thisInstance = f.save(commit=False)
							if request.POST.get("submit"):
								thisInstance.isSubmit = True
								thisInstance.submit_date = timezone.now()
								if response_submitted_mail(thisEvent.title,thisUserData.email,request):
								    thisInstance.confirmation_email_sent = True
								thisInstance.user = thisUserData.user
								thisInstance.name = thisUserData.full_name
								thisInstance.institution = thisUserData.institution
								thisInstance.city = thisUserData.city
								thisInstance.email = thisUserData.email
								thisInstance.contact = thisUserData.contact
								thisInstance.save()
								messages.add_message(request, messages.INFO, 'You have succesfully submitted your \'In Other Words\' Challenge \' ' + (thisEvent.title) + ' \' Responses')
								return redirect('registration')
							else:
								thisInstance.last_modify_date = timezone.now()
								thisInstance.user = thisUserData.user
								thisInstance.name = thisUserData.full_name
								thisInstance.institution = thisUserData.institution
								thisInstance.city = thisUserData.city
								thisInstance.email = thisUserData.email
								thisInstance.contact = thisUserData.contact
								thisInstance.save()
								messages.add_message(request, messages.INFO, 'You have succesfully modified your  \'In Other Words\' Challenge \' ' + (thisEvent.title) + ' \' Responses')
								f =InOtherWordsChallengeForm02(instance=thisInstance)
								return render(request, 'originals/iow_challenge02.html', {'form': f})
			else:
				if request.method == "POST":
					#request.FILES if needed
					f = InOtherWordsChallengeForm02(request.POST)
					if f.is_valid():
						reg = f.save(commit=False)
						reg.user = request.user
						if request.POST.get("submit"):
							reg.isSubmit = True
							reg.submit_date = timezone.now()
							if response_submitted_mail(thisEvent.title,thisUserData.email,request):
							    reg.confirmation_email_sent = True
							reg.user = thisUserData.user
							reg.name = thisUserData.full_name
							reg.institution = thisUserData.institution
							reg.city = thisUserData.city
							reg.email = thisUserData.email
							reg.contact = thisUserData.contact
							reg.save()
							messages.add_message(request, messages.INFO, 'You have succesfully submitted your \'In Other Words\' Challenge \' ' + (thisEvent.title) + ' \' Responses')
						else:
							reg.last_modify_date = timezone.now()
							reg.user = thisUserData.user
							reg.name = thisUserData.full_name
							reg.institution = thisUserData.institution
							reg.city = thisUserData.city
							reg.email = thisUserData.email
							reg.contact = thisUserData.contact
							reg.save()
							messages.add_message(request, messages.INFO, 'You have succesfully saved your \'In Other Words\' Challenge \' ' + (thisEvent.title) + ' \' Responses')
							return render(request, 'originals/iow_challenge02.html', {'form': f})
						return redirect('registration')
				else:
					f = InOtherWordsChallengeForm02()
			return render(request, 'originals/iow_challenge02.html', {'form': f})
		else:
			messages.add_message(request, messages.INFO, 'Please log in to participate in \'In Other Words\' ')
			return redirect('login')
	else:
		return render(request, 'originals/iow_closed.html',{})
