from django.shortcuts import render
from django.utils import timezone
from .models import Images,Articles,Videos

def originals_all(request):
	images =  Images.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')[:5]
	articles =  Articles.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')[:5]
	videos =  Videos.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')[:5]
	return render(request, 'originals/originals_all.html', {'images':images, 'articles': articles, 'videos': videos})

def blogs(request):
	articles =  Articles.objects.filter(content_type='A1').filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'originals/originals_all.html', {'images':images, 'articles': articles, 'videos': videos})

def sciencequizzine(request):
	images =  Images.objects.filer(content_type='I1').filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'originals/originals_all.html', {'images':images, 'articles': articles, 'videos': videos})

def comicstrips(request):
	images =  Images.objects.filer(content_type='I2').filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'originals/originals_all.html', {'images':images, 'articles': articles, 'videos': videos})

def tuesdaytrivia(request):
	images =  Images.objects.filer(content_type='I4').filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'originals/originals_all.html', {'images':images, 'articles': articles, 'videos': videos})

def throwbackthursdays(request):
	images =  Images.objects.filer(content_type='I5').filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'originals/originals_all.html', {'images':images, 'articles': articles, 'videos': videos})


def memes(request):
	#images =  Images.objects.filer(content_type='I6').filter(publish_date__lte=timezone.now()).order_by('publish_date')
	images =  Images.objects.all()
	length =  images.count()
	return render(request, 'originals/gallery.html', {'images':images, 'length' : length})


def videos(request):
	videos =  Videos.objects.filer(content_type='V1').filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'originals/originals_all.html', {'images':images, 'articles': articles, 'videos': videos})
