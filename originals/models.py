from django.db import models
from django.utils import timezone

#are the properties enough? too many? are arguments right?
class ArchiveImage(models.Model):
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	publish_date = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False, blank=True, null=True)
	title = models.CharField(max_length=200)
	OCCASION_CHOICES = (
				('P8','Pravega 2018'),
				('P7','Pravega 2017'),
				('P6','Pravega 2016'),
				('I0','Hidden'),
			)
	content_type = models.CharField(
		max_length=2,
		choices = OCCASION_CHOICES,
		 )
	description = models.CharField(max_length=280)
	image_file = models.ImageField(upload_to='archiveimages/%Y/%m/%d')
	
	def __str__(self):
	 	return self.title

class ScienceQuizzine(models.Model):
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	publish_date = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False, blank=True, null=True)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=280)
	image_file = models.ImageField(upload_to='sciencequizzine')
	#winners??
	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
 		return self.title


class LetsTalkScience(models.Model):
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	publish_date = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False, blank=True, null=True)
	title = models.CharField(max_length=200)
	description = models.TextField()
	youtube_id = models.CharField(max_length=200)

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
