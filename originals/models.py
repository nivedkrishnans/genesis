from django.db import models
from django.utils import timezone

#are the properties enough? too many? are arguments right?

class Images(models.Model):
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	title = models.CharField(max_length=200)
	CONTENT_CHOICES = (
				('I1','Science Quizzine'),
				('I2','Comic Strip'),
				('I3','Gallery'),
				('I4','Tuesday Trivia'),
				('I5','Throwback Thursdays'),
				('I6','Meme'),
				('I0','Hidden'),
			)
	content_type = models.CharField(
		max_length=2,
		choices = CONTENT_CHOICES,
		 )
	description = models.CharField(max_length=280)
	image_file = models.ImageField(upload_to='images/%Y/%m/%d')

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
 		return self.title



class Articles(models.Model):
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	title = models.CharField(max_length=200)
	CONTENT_CHOICES =	(
				('A1','Blog'),
				('A2','Articles'),
				('A0','Hidden'),
			)
	content_type = models.CharField(
		max_length=2,
		choices = CONTENT_CHOICES ,
		 )
	description = models.CharField(max_length=280)
	author = models.CharField(max_length=60)
	text = models.TextField()
	cover_image = models.ImageField(upload_to='images/%Y/%m/%d' , null=True)
	number_of_views = models.PositiveIntegerField(default=0)
	mail_id = models.EmailField(max_length=60, null=True, blank=True)			#I dont know

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title



class Videos(models.Model):
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	title = models.CharField(max_length=200)
	CONTENT_CHOICES = (
				('V1','Interview'),
				('V0' , 'Hidden'),
			)
	content_type = models.CharField(
		max_length=2,
		choices = CONTENT_CHOICES,
		 )
	description = models.CharField(max_length=280)
	text = models.TextField()
	youtube_id = models.CharField(max_length=200)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
