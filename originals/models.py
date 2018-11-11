from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

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


class InOtherWord(models.Model):
	title = models.CharField(max_length=255)
	challengeNo = models.IntegerField(default=0)
	description = models.TextField()
	snippet = models.ImageField(upload_to = 'InOtherWords/snippets', blank=True)
	question_PDF = models.FileField(upload_to = 'InOtherWords/Question_PDF' , validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])])
	answer_PDF = models.FileField(upload_to = "InOtherWords/answer_PDF" , blank=True , validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])])
	link_form = models.CharField(max_length = 255 , default='#')
	active = models.BooleanField(default = False)
	create_date = models.DateTimeField(auto_now_add=True)
	publish_date = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False, blank=True, null=True)
	def __str__(self):
		return str(self.challengeNo) + " " + self.title

class InOtherWordsChallenge01(models.Model):
	#The answers:
	city01 = models.CharField(max_length=200, blank=True, null=True)
	city02 = models.CharField(max_length=200, blank=True, null=True)
	city03 = models.CharField(max_length=200, blank=True, null=True)
	city04 = models.CharField(max_length=200, blank=True, null=True)
	city05 = models.CharField(max_length=200, blank=True, null=True)
	city06 = models.CharField(max_length=200, blank=True, null=True)
	city07 = models.CharField(max_length=200, blank=True, null=True)
	city08 = models.CharField(max_length=200, blank=True, null=True)
	city09 = models.CharField(max_length=200, blank=True, null=True)
	city10 = models.CharField(max_length=200, blank=True, null=True)
	bonusquestion = models.TextField(max_length=200, blank=True, null=True)
	#user info:
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_modify_date = models.DateTimeField( null=True, blank=True)
	submit_date = models.DateTimeField( null=True, blank=True)
	name = models.CharField(max_length=200)
	institution = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	email = models.EmailField(max_length=200, null=False, blank=False)
	contact = models.CharField(max_length=20)
	confirmation_email_sent = models.BooleanField(default=False)
	isSubmit = models.BooleanField(default=False)
	def __str__(self):
		return self.name


class InOtherWordsChallenge02(models.Model):
	#The answers:
	placesOrder = models.CharField(max_length=20, blank=True, null=True)
	question2 = models.TextField(max_length=400, blank=True, null=True)
	#user info:
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_modify_date = models.DateTimeField( null=True, blank=True)
	submit_date = models.DateTimeField( null=True, blank=True)
	name = models.CharField(max_length=200)
	institution = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	email = models.EmailField(max_length=200, null=False, blank=False)
	contact = models.CharField(max_length=20)
	confirmation_email_sent = models.BooleanField(default=False)
	isSubmit = models.BooleanField(default=False)
	def __str__(self):
		return self.name


class InOtherWordsChallenge03(models.Model):
	#The answers:
	question1 = models.TextField(max_length=400, blank=True, null=True)
	question2a = models.CharField(max_length=30, blank=True, null=True)
	question2b = models.CharField(max_length=30, blank=True, null=True)
	question2c = models.CharField(max_length=30, blank=True, null=True)
	question2d = models.CharField(max_length=30, blank=True, null=True)
	question2e = models.CharField(max_length=30, blank=True, null=True)
	#user info:
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_modify_date = models.DateTimeField( null=True, blank=True)
	submit_date = models.DateTimeField( null=True, blank=True)
	name = models.CharField(max_length=200)
	institution = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	email = models.EmailField(max_length=200, null=False, blank=False)
	contact = models.CharField(max_length=20)
	confirmation_email_sent = models.BooleanField(default=False)
	isSubmit = models.BooleanField(default=False)
	def __str__(self):
		return self.name




class InOtherWordsChallenge04(models.Model):
	#The answers:
	question1 = models.TextField(max_length=400, blank=True, null=True)
	question2 = models.TextField(max_length=400, blank=True, null=True)
	question3 = models.TextField(max_length=400, blank=True, null=True)
	question4 = models.TextField(max_length=400, blank=True, null=True)
	question5 = models.TextField(max_length=400, blank=True, null=True)
	#user info:
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_modify_date = models.DateTimeField( null=True, blank=True)
	submit_date = models.DateTimeField( null=True, blank=True)
	name = models.CharField(max_length=200)
	institution = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	email = models.EmailField(max_length=200, null=False, blank=False)
	contact = models.CharField(max_length=20)
	confirmation_email_sent = models.BooleanField(default=False)
	isSubmit = models.BooleanField(default=False)
	def __str__(self):
		return self.name


class InOtherWordsChallenge05(models.Model):
	#The answers:
	question1 = models.CharField(max_length=50, blank=True, null=True)
	question2 = models.CharField(max_length=50, blank=True, null=True)
	question3 = models.CharField(max_length=50, blank=True, null=True)
	question4 = models.CharField(max_length=50, blank=True, null=True)
	question5 = models.CharField(max_length=50, blank=True, null=True)
	question6 = models.CharField(max_length=50, blank=True, null=True)
	question7 = models.CharField(max_length=50, blank=True, null=True)
	question8 = models.CharField(max_length=50, blank=True, null=True)
	question9 = models.CharField(max_length=50, blank=True, null=True)
	question10 = models.CharField(max_length=50, blank=True, null=True)
	question11 = models.CharField(max_length=50, blank=True, null=True)
	question12 = models.CharField(max_length=50, blank=True, null=True)
	question13 = models.CharField(max_length=50, blank=True, null=True)
	question14 = models.CharField(max_length=50, blank=True, null=True)
	question15 = models.CharField(max_length=50, blank=True, null=True)
	#user info:
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_modify_date = models.DateTimeField( null=True, blank=True)
	submit_date = models.DateTimeField( null=True, blank=True)
	name = models.CharField(max_length=200)
	institution = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	email = models.EmailField(max_length=200, null=False, blank=False)
	contact = models.CharField(max_length=20)
	confirmation_email_sent = models.BooleanField(default=False)
	isSubmit = models.BooleanField(default=False)
	def __str__(self):
		return self.name


class InOtherWordsChallenge06(models.Model):
	#The answers:
	question1 = models.TextField(max_length=600, blank=True, null=True)
	question2a = models.TextField(max_length=100, blank=True, null=True)
	question2b = models.TextField(max_length=100, blank=True, null=True)
	question2c = models.TextField(max_length=100, blank=True, null=True)
	#user info:
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_modify_date = models.DateTimeField( null=True, blank=True)
	submit_date = models.DateTimeField( null=True, blank=True)
	name = models.CharField(max_length=200)
	institution = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	email = models.EmailField(max_length=200, null=False, blank=False)
	contact = models.CharField(max_length=20)
	confirmation_email_sent = models.BooleanField(default=False)
	isSubmit = models.BooleanField(default=False)
	def __str__(self):
		return self.name
