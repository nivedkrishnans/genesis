from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Update,Faq
from registration.field_helpers import videoFileSupportMessage,audioVideoFileSupportMessage,lasyaSizeLimit,battleofbandsSizeLimit,prosceniumSizeLimit
from registration.models import AdminEvent
from django.views import generic
from django.contrib import messages

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
	return render(request, 'essentials/events_v2.html', {})

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

def decoherenceprelimsresult(request):
	return render(request, 'essentials/decoherencePrelimsResult.html', {})

def footprints(request):
	return render(request, 'essentials/footprints.html', {})

def openQuizzes(request):
	return render(request, 'essentials/openQuizzes.html', {})

def collegeQuizzes(request):
	return render(request, 'essentials/collegeQuizzes.html', {})

def scienceQuizzine(request):
	return render(request, 'essentials/scienceQuizzine.html', {})

def lasya(request):
	return render(request, 'essentials/lasya.html', {'file_info' : videoFileSupportMessage(lasyaSizeLimit),})

def wikimediaphotography(request):
	return render(request, 'essentials/wikimediaphotography.html', {})


def pis(request):
	return render(request, 'essentials/pis.html', {})

def pisResults(request):
	return render(request, 'essentials/pisResults.html', {})

def sciencejournalism(request):
	return render(request, 'essentials/sciencejournalism.html', {})

def molecularmurals(request):
	return render(request, 'essentials/molecularmurals.html', {})

def chemisticon(request):
	return render(request, 'essentials/chemisticon.html', {})

def interschool(request):
	return render(request, 'essentials/interschool.html', {})

def whodunnit(request):
	return render(request, 'essentials/whodunnit.html', {})

def debubulary(request):
	return render(request, 'essentials/debubulary.html', {})

def cryptothlon(request):
	return render(request, 'essentials/cryptothlon.html', {})

def vignettora(request):
	return render(request, 'essentials/vignettora.html', {})

def etc(request):
	return render(request, 'essentials/etc.html', {})

def ibm_hackathon(request):
	return render(request, 'essentials/ibm_hackathon.html', {})

def ibmhackathonprelimsresult(request):
	return render(request, 'essentials/IBMHackathonPrelimsResult.html', {})

def kryptochase(request):
	return render(request, 'essentials/kryptochase.html', {})

def gaming(request):
	return render(request, 'essentials/gaming.html', {})

def ifp(request):
	return render(request, 'essentials/IFP.html', {})

def integrationbee(request):
	return render(request, 'essentials/integrationbee.html', {})

def sandhi(request):
	return render(request, 'essentials/sandhi.html', {})

def workshops(request):
	return render(request, 'essentials/workshops.html', {})


def partners(request):
	return render(request, 'essentials/partners.html', {})

def sponsors(request):
	return render(request, 'essentials/sponsors.html', {})

def team(request):
	return render(request, 'essentials/team.html', {})

def sponsorsRedirect(request):
	return redirect('partners')

def homeRedirect(request):
	return redirect('home')

class FaqListView(generic.ListView):
	faqInfo=Faq
	context_object_name = 'faq_list'
	queryset=faqInfo.objects.all().order_by('-create_date').order_by('-priority')
	template_name = 'essentials/faq.html'


def comingsoon(request):
	return render(request, 'essentials/comingsoon.html', {})


def policy(request):
	return render(request, 'essentials/privacypolicy.html', {})

def notify_pronites(request):
	if request.user.is_authenticated:
		messages.add_message(request, messages.INFO, 'You will receive updates about TesseracT\'s concert at Pravega')
	else:
		messages.add_message(request, messages.INFO, 'Please Sign Up (if you haven\'t already) to get updates about TesseracT\'s concert at Pravega')
	return redirect('registration')
