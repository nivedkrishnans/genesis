from django.shortcuts import render
from django.utils import timezone
from .models import ArchiveImage,ScienceQuizzine,LetsTalkScience


def archives(request):
	images =  ArchiveImage.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'originals/archives.html', {'images':images})

def originals(request):
	images =  ScienceQuizzine.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	videos =  LetsTalkScience.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'originals/originals.html', {'images':images, 'videos':videos})
