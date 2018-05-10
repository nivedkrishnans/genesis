from django.shortcuts import render
from django.utils import timezone
from .models import Images,Articles,Videos

def originals_all(request):
	images =  Images.objects.all()[:5]
	articles =  Articles.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')[:5]
	videos =  Videos.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')[:5]
	return render(request, 'originals/originals_all.html', {'images':images, 'articles': articles, 'videos': videos})
