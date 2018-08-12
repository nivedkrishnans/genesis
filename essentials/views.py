from django.shortcuts import render
from django.utils import timezone

def home(request):
	return render(request, 'essentials/home.html', {})

def updates(request):
	return render(request, 'essentials/updates.html', {})

def help(request):
	return render(request, 'essentials/help.html', {})

def contact(request):
	return render(request, 'essentials/contact.html', {})

#def archive(request):
#	return render(request, 'essentials/archive.html', {})

def partners(request):
	return render(request, 'essentials/partners.html', {})

def comingsoon(request):
	return render(request, 'essentials/comingsoon.html', {})
