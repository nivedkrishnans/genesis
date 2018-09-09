from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from .field_helpers import PhoneNumberField,lasya_file_validation,proscenium_file_validation
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
    place =  models.CharField(max_length=127, default='unknown_place')
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
    description = models.TextField()
    registrationLink = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.title


class LasyaRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    teamName = models.CharField(max_length=144)
    teamLeader = models.CharField(max_length=144)
    institution = models.CharField(max_length=144)
    place = models.CharField(max_length=144)
    email = models.EmailField(max_length=144, null=False, blank=False)
    contact1 = PhoneNumberField.get_field()
    contact2 = PhoneNumberField.get_field(blank=True)
    participantList =  models.TextField()
    videoFileLink = models.URLField(max_length=300, null=False, blank=True)
    #function to generate a path to upload the file
    def filePathGenerate(instance,filename):
        temp = 'lasya/' + str(instance.teamName) + '_' + str(instance.user) + '_' + str(instance.institution) + '/'
        temp2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        temp3 = '/' + os.path.split(filename)[1]
        temp = temp + temp2 + temp3
        return temp
    videoFile = models.FileField(validators=[lasya_file_validation], upload_to=filePathGenerate, null=False, blank=True, max_length=600)
    confirmation_email_sent = models.BooleanField(default=False)
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
    place = models.CharField(max_length=144)
    email = models.EmailField(max_length=144, null=False, blank=False)
    contact1 = PhoneNumberField.get_field()
    contact2 = PhoneNumberField.get_field(blank=True)
    participantList =  models.TextField()
    videoFileLink = models.URLField(max_length=300, null=False, blank=True)
    #function to generate a path to upload the file
    def filePathGenerate(instance,filename):
        temp = 'proscenium/' + str(instance.language) + '/' + str(instance.teamName) + '_' + str(instance.user) + '_' + str(instance.institution) + '/'
        temp2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        temp3 = '/' + os.path.split(filename)[1]
        temp = temp + temp2 + temp3
        return temp
    videoFile = models.FileField(validators=[proscenium_file_validation], upload_to=filePathGenerate, null=False, blank=True, max_length=600)
    confirmation_email_sent = models.BooleanField(default=False)
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
    place = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=False, blank=False)
    contact1 = PhoneNumberField.get_field()
    contact2 = PhoneNumberField.get_field(blank=True)
    participantList =  models.TextField()
    confirmation_email_sent = models.BooleanField(default=False)
    def __str__(self):
        return self.teamName
