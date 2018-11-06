from django.shortcuts import render
from django.utils import timezone
from .models import Update,Faq
from registration.field_helpers import videoFileSupportMessage,audioVideoFileSupportMessage,lasyaSizeLimit,battleofbandsSizeLimit,prosceniumSizeLimit
from registration.models import AdminEvent
from django.views import generic

def home(request):
	allAdminEvents = AdminEvent.objects.all()
	campusAmbassadorOpen = False
	for i in allAdminEvents:
		if (i.title == 'Campus Ambassadors'):
			if (i.registrationStatus == 'opened'):
				campusAmbassadorOpen = True
	return render(request, 'essentials/home.html', {'campusAmbassadorOpen':campusAmbassadorOpen,})

def updates(request):
	monthDict={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
	updates =  Update.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
	updateMonth=[]
	updateDate=[]
	temp=0
	for i in updates:
		temp=i.publish_date.month
		updateMonth.append(monthDict[temp])

	return render(request, 'essentials/updates.html', {'updates':updates , 'monthDict':monthDict, 'updateMonth':updateMonth})

def help(request):
	return render(request, 'essentials/help.html', {})

def events(request):
	return render(request, 'essentials/events.html', {})


def eventstest(request):
	return render(request, 'essentials/eventstest.html', {})

def contact(request):
	return render(request, 'essentials/contact.html', {})

def register(request):
	return render(request, 'essentials/register.html', {})

def carousel(request):
	return render(request, 'essentials/carousel.html', {})

def proscenium(request):
	return render(request, 'essentials/proscenium.html', {'file_info' : videoFileSupportMessage(prosceniumSizeLimit),})

def battleofbands(request):
	return render(request, 'essentials/battleofbands.html', {'file_info' : audioVideoFileSupportMessage(battleofbandsSizeLimit),})

def decoherence(request):
	return render(request, 'essentials/decoherence.html', {})

def footprints(request):
	return render(request, 'essentials/footprints.html', {})

def lasya(request):
	return render(request, 'essentials/lasya.html', {'file_info' : videoFileSupportMessage(lasyaSizeLimit),})

def wikimediaphotography(request):
	return render(request, 'essentials/wikimediaphotography.html', {})

def partners(request):
	return render(request, 'essentials/partners.html', {})


class FaqListView(generic.ListView):
	faqInfo=Faq
	context_object_name = 'faq_list'
	queryset=faqInfo.objects.all().order_by('-create_date').order_by('-priority')
	template_name = 'essentials/faq.html'


def comingsoon(request):
	return render(request, 'essentials/comingsoon.html', {})


def policy(request):
	return render(request, 'essentials/privacypolicy.html', {})
