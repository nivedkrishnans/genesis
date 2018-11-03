from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from .field_helpers import PhoneNumberField,lasya_file_validation,proscenium_file_validation,battleofbands_file_validation
#for user full name or username display
from django.contrib.auth.models import User
import random
import string
import os.path


def get_first_name(self):
    name='friend'
    try:
        if (self.userdata_link.full_name != 'unknown_name') and (self.userdata_link.full_name):
            name=self.userdata_link.full_name
    except:
        name=self.username
    return name

User.add_to_class("__str__", get_first_name)


class UserData(models.Model):
    #associates Author model with User model (Important)
    user = models.OneToOneField(User, related_name='userdata_link', on_delete=models.CASCADE, null=True, blank=True)
    full_name =  models.CharField(max_length=127, default='unknown_name')
    institution =  models.CharField(max_length=127, default='unknown_institution')
    city =  models.CharField(max_length=127, default='unknown_city')
    email = models.EmailField(max_length=144, null=True, blank=True)
    contact = models.CharField(max_length=20, default='NO_NUMBER')
    create_date = models.DateTimeField( null=True, blank=True)
    # additional fields
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)
    #events Registered
    #lasya = models.BooleanField(default=False)
    #proscenium = models.BooleanField(default=False)
    #footprints = models.BooleanField(default=False)
    def __str__(self):
        return self.full_name

class AdminEvent(models.Model):
    REGISTRATION_STATUS_CHOICES=(
        ('notyet','Not Yet'),
        ('opened','Open'),
        ('closed','Closed'),
    )
    registrationStatus = models.CharField(default="notyet", max_length=200, choices=REGISTRATION_STATUS_CHOICES)
    title = models.CharField(max_length=200)
    displayTitle = models.CharField(blank=True, null=False, max_length=200)
    description = models.TextField()
    priority = models.IntegerField(default=0)
    registrationLink = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.title

class CampusAmbassador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    full_name =  models.CharField(max_length=127, default='unknown_name')
    institution = models.CharField(max_length=144)
    city = models.CharField(max_length=144)
    email = models.EmailField(max_length=144, null=False, blank=False)
    contactForCalls = models.CharField(max_length=20)
    contactForWhatsapp = models.CharField(max_length=20)
    #how you got to know about this program/event
    howyouknow = models.CharField(blank=True, null=False, max_length=200)
    isSubmit = models.BooleanField(default=False)
    last_modify_date = models.DateTimeField( null=True, blank=True)
    submit_date = models.DateTimeField( null=True, blank=True)

class LasyaRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    teamName = models.CharField(blank=True, max_length=144)
    teamLeader = models.CharField(blank=True, max_length=144)
    institution = models.CharField(max_length=144)
    city = models.CharField(max_length=144)
    email = models.EmailField(max_length=144, null=False, blank=False)
    contact1 = models.CharField(max_length=20)
    contact2 = models.CharField(max_length=20,blank=False)
    CATEGORY_CHOICES=(
        ('solo','SOLO'),
        ('duet','DUET'),
        ('group','GROUP'),
    )
    category = models.CharField(default="GROUP", max_length=10, choices=CATEGORY_CHOICES)
    participantList =  models.TextField(blank=True)
    videoFileLink = models.URLField(max_length=300, null=False, blank=True)
    #function to generate a path to upload the file
    def filePathGenerate(instance,filename):
        temp = 'private/lasya/' + str(instance.teamName) + '_' + str(instance.user) + '_' + str(instance.institution) + '/'
        temp2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        temp3 = '/' + os.path.split(filename)[1]
        temp = temp + temp2 + temp3
        return temp
    videoFile = models.FileField(validators=[lasya_file_validation], upload_to=filePathGenerate, null=False, blank=True, max_length=600)
    #how you got to know about this program/event
    howyouknow = models.CharField(blank=True, null=False, max_length=200)
    confirmation_email_sent = models.BooleanField(default=False)
    #whether or not the form was submitted
    isSubmit = models.BooleanField(default=False)
    last_modify_date = models.DateTimeField( null=True, blank=True)
    submit_date = models.DateTimeField( null=True, blank=True)
    def __str__(self):
        return self.teamName

class ProsceniumRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    teamName = models.CharField(max_length=144)
    teamLeader = models.CharField(max_length=144)
    LANGUAGE_CHOICES=(
        ('English','English'),
        ('Hindi','Hindi'),
        ('Kannada','Kannada'),
    )
    language = models.CharField(default="English", max_length=20, choices=LANGUAGE_CHOICES)
    institution = models.CharField(max_length=144)
    city = models.CharField(max_length=144)
    email = models.EmailField(max_length=144, null=False, blank=False)
    contact1 = models.CharField(max_length=20)
    contact2 = models.CharField(max_length=20,blank=False)
    participantList =  models.TextField()
    videoFileLink = models.URLField(max_length=300, null=False, blank=True)
    #function to generate a path to upload the file
    def filePathGenerate(instance,filename):
        temp = 'private/proscenium/' + str(instance.language) + '/' + str(instance.teamName) + '_' + str(instance.user) + '_' + str(instance.institution) + '/'
        temp2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        temp3 = '/' + os.path.split(filename)[1]
        temp = temp + temp2 + temp3
        return temp
    videoFile = models.FileField(validators=[proscenium_file_validation], upload_to=filePathGenerate, null=False, blank=True, max_length=600)
    #how you got to know about this program/event
    howyouknow = models.CharField(blank=True, null=False, max_length=200)
    confirmation_email_sent = models.BooleanField(default=False)
    #whether or not the form was submitted
    isSubmit = models.BooleanField(default=False)
    last_modify_date = models.DateTimeField( null=True, blank=True)
    submit_date = models.DateTimeField( null=True, blank=True)
    def __str__(self):
        return self.teamName


class BattleOfBandsRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    teamName = models.CharField(max_length=144)
    teamLeader = models.CharField(max_length=144)
    institution = models.CharField(max_length=144)
    city = models.CharField(max_length=144)
    REGIONAL_FINALS_CITY_CHOICES=(
        ('BANGALORE','BANGALORE'),
        ('CHENNAI','CHENNAI'),
        ('HYDERABAD','HYDERABAD'),
        ('KOCHI','KOCHI'),
        ('MUMBAI','MUMBAI'),
    )
    regionalfinalscity = models.CharField(default="BANGALORE", null=False, blank=False, max_length=20, choices=REGIONAL_FINALS_CITY_CHOICES)
    email = models.EmailField(max_length=144, null=False, blank=False)
    contact1 = models.CharField(max_length=20)
    contact2 = models.CharField(max_length=20,blank=False)
    participantList =  models.TextField()
    audioVideoFileLink = models.URLField(max_length=300, null=False, blank=True)
    #function to generate a path to upload the file
    def filePathGenerate(instance,filename):
        temp = 'private/battleofbands/' + '/' + str(instance.teamName) + '_' + str(instance.user) + '_' + str(instance.institution) + '/'
        temp2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        temp3 = '/' + os.path.split(filename)[1]
        temp = temp + temp2 + temp3
        return temp
    audioVideoFile = models.FileField(validators=[battleofbands_file_validation], upload_to=filePathGenerate, null=False, blank=True, max_length=600)
    #how you got to know about this program/event
    howyouknow = models.CharField(blank=True, null=False, max_length=200)
    confirmation_email_sent = models.BooleanField(default=False)
    #whether or not the form was submitted
    isSubmit = models.BooleanField(default=False)
    last_modify_date = models.DateTimeField( null=True, blank=True)
    submit_date = models.DateTimeField( null=True, blank=True)
    def __str__(self):
        return self.teamName

class FootprintsRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    teamName = models.CharField(max_length=200)
    teamLeader = models.CharField(max_length=200)
    LANGUAGE_CHOICES=(
        ('English','English'),
        ('Hindi','Hindi'),
        ('Kannada','Kannada'),
    )
    language = models.CharField(default="English", max_length=200, choices=LANGUAGE_CHOICES)
    institution = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=False, blank=False)
    contact1 = models.CharField(max_length=20)
    contact2 = models.CharField(max_length=20,blank=False)
    participantList =  models.TextField()
    #how you got to know about this program/event
    howyouknow = models.CharField(blank=True, null=False, max_length=200)
    confirmation_email_sent = models.BooleanField(default=False)
    #whether or not the form was submitted
    isSubmit = models.BooleanField(default=False)
    last_modify_date = models.DateTimeField( null=True, blank=True)
    submit_date = models.DateTimeField( null=True, blank=True)
    def __str__(self):
        return self.teamName



class DecoherenceRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    teamName = models.CharField(max_length=144)
    participant1 = models.CharField(max_length=200, blank=False)
    qualification1 = models.CharField(max_length=200, blank=False)
    email1 = models.EmailField(max_length=144, null=False, blank=False)
    contact1 = models.CharField(max_length=20, blank=False)
    participant2 = models.CharField(max_length=200, blank=True)
    qualification2 = models.CharField(max_length=200, blank=True)
    email2 = models.EmailField(max_length=144, null=False, blank=True)
    contact2 = models.CharField(max_length=20, blank=True)
    institution = models.CharField(max_length=144)
    city = models.CharField(max_length=144)
    #how you got to know about this program/event
    howyouknow = models.CharField(blank=True, null=False, max_length=200)
    confirmation_email_sent = models.BooleanField(default=False)
    #whether or not the form was submitted
    isSubmit = models.BooleanField(default=False)
    last_modify_date = models.DateTimeField( null=True, blank=True)
    submit_date = models.DateTimeField( null=True, blank=True)
    def __str__(self):
        return self.teamName


class WikimediaPhotographyRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    #form details
    wikimediaUsername = models.CharField(max_length=200)
    submission1 = models.URLField(max_length=300, null=False, blank=True)
    submission2 = models.URLField(max_length=300, null=False, blank=True)
    submission3 = models.URLField(max_length=300, null=False, blank=True)
    submission4 = models.URLField(max_length=300, null=False, blank=True)
    submission5 = models.URLField(max_length=300, null=False, blank=True)
    #user details
    institution = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=False, blank=False)
    contact = models.CharField(max_length=20)
    #how you got to know about this program/event
    howyouknow = models.CharField(blank=True, null=False, max_length=200)
    confirmation_email_sent = models.BooleanField(default=False)
    #whether or not the form was submitted
    isSubmit = models.BooleanField(default=False)
    last_modify_date = models.DateTimeField( null=True, blank=True)
    submit_date = models.DateTimeField( null=True, blank=True)
    def __str__(self):
        return str(self.user)
