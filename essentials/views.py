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

def register(request):
	return render(request, 'essentials/register.html', {})

def carousel(request):
	return render(request, 'essentials/carousel.html', {})

def proscenium(request):
	return render(request, 'essentials/proscenium.html', {})

def battleofbands(request):
	return render(request, 'essentials/battleofbands.html', {})

def footprints(request):
	return render(request, 'essentials/footprints.html', {})

def lasya(request):
	return render(request, 'essentials/lasya.html', {})


#def archive(request):
#	return render(request, 'essentials/archive.html', {})

def partners(request):
	return render(request, 'essentials/partners.html', {})

def comingsoon(request):
	return render(request, 'essentials/comingsoon.html', {})
