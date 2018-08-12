from django.shortcuts import render
from django.utils import timezone
from .models import ArchiveImage,ScienceQuizzine,Image,Article,Video


def archives(request):
	images =  ArchiveImage.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'originals/archives.html', {'images':images})

def sciencequizzine(request):
	images =  ScienceQuizzine.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'originals/sciencequizzine.html', {'images':images})

def memes(request):
	#images =  Images.objects.filer(content_type='I6').filter(publish_date__lte=timezone.now()).order_by('publish_date')
	images =  Image.objects.all()
	length =  image.count()
	return render(request, 'originals/gallery.html', {'images':images, 'length' : length})
