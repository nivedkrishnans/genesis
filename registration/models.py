from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from .field_helpers import PhoneNumberField,ibmhackathon_file_validation,sciencejournalism_file_validation,lasya_file_validation,proscenium_file_validation,battleofbands_file_validation
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

#for user full name or username display
from django.contrib.auth.models import User
import random
import string
import os.path

from django import forms
from django.utils import timezone

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


class LasyaGroupRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    teamName = models.CharField(blank=True, max_length=144)
    teamLeader = models.CharField(blank=True, max_length=144)
    institution = models.CharField(max_length=144)
    city = models.CharField(max_length=144)
    email = models.EmailField(max_length=144, null=False, blank=False)
    contact1 = models.CharField(max_length=20)
    contact2 = models.CharField(max_length=20,blank=False)
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



class LasyaSoloRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    full_name = models.CharField(max_length=144)
    institution = models.CharField(max_length=144)
    city = models.CharField(max_length=144)
    email = models.EmailField(max_length=144, null=False, blank=False)
    contact = models.CharField(max_length=20)
    videoFileLink = models.URLField(max_length=300, null=False, blank=True)
    #function to generate a path to upload the file
    def filePathGenerate(instance,filename):
        temp = 'private/lasya/' + str(instance.full_name) + '_' + str(instance.user) + '_' + str(instance.institution) + '/'
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
        return self.full_name + self.institution


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

class ChemisticonRegistration(models.Model):
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
    participant3 = models.CharField(max_length=200, blank=True)
    qualification3 = models.CharField(max_length=200, blank=True)
    email3 = models.EmailField(max_length=144, null=False, blank=True)
    contact3 = models.CharField(max_length=20, blank=True)
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

class DebubularyRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    teamName = models.CharField(max_length=144)
    participant1 = models.CharField(max_length=200, blank=False)
    email1 = models.EmailField(max_length=144, null=False, blank=False)
    contact1 = models.CharField(max_length=20, blank=False)
    participant2 = models.CharField(max_length=200, blank=True)
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

class CryptothlonRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    teamName = models.CharField(max_length=144)
    participant1 = models.CharField(max_length=200, blank=False)
    email1 = models.EmailField(max_length=144, null=False, blank=False)
    contact1 = models.CharField(max_length=20, blank=False)
    participant2 = models.CharField(max_length=200, blank=True)
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


class VignettoraRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    #form details

    #user details
    full_name =  models.CharField(max_length=127)
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

class ScienceJournalismRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    #form details

    #user details
    full_name =  models.CharField(max_length=127)
    institution = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=False, blank=False)
    contact = models.CharField(max_length=20)

    def filePathGenerate(instance,filename):
        temp = 'private/sciencejournalism/' + str(instance.full_name) + '_' + str(instance.user) + '_' + str(instance.institution) + '/'
        temp2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        temp3 = '/' + os.path.split(filename)[1]
        temp = temp + temp2 + temp3
        return temp
    articleFile = models.FileField(validators=[sciencejournalism_file_validation], upload_to=filePathGenerate, null=False, blank=True, max_length=600)

    #how you got to know about this program/event
    howyouknow = models.CharField(blank=True, null=False, max_length=200)
    confirmation_email_sent = models.BooleanField(default=False)
    #whether or not the form was submitted
    isSubmit = models.BooleanField(default=False)
    last_modify_date = models.DateTimeField( null=True, blank=True)
    submit_date = models.DateTimeField( null=True, blank=True)
    def __str__(self):
        return str(self.user)



class ETCRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    #user details
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=False, blank=False)
    contact = models.CharField(max_length=20)
    #form details

    physics=models.BooleanField(default=False)
    mathematics=models.BooleanField(default=False)
    chemistry=models.BooleanField(default=False)
    biology=models.BooleanField(default=False)
    psychology=models.BooleanField(default=False)
    economics=models.BooleanField(default=False)
    other_subjects = models.CharField(max_length=200,blank=True, null=False)
    topic = models.CharField(max_length=800,blank=True, null=False)

    #how you got to know about this program/event
    howyouknow = models.CharField(blank=True, null=False, max_length=200)
    confirmation_email_sent = models.BooleanField(default=False)
    #whether or not the form was submitted
    isSubmit = models.BooleanField(default=False)
    last_modify_date = models.DateTimeField( null=True, blank=True)
    submit_date = models.DateTimeField( null=True, blank=True)
    def __str__(self):
        return str(self.user)

class ISCRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    #form details

    #user details
    full_name =  models.CharField(max_length=127)
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

class IBMHackathonRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    #form details

    #user details
    teamName = models.CharField(max_length=144)
    member1 = models.CharField(max_length=200, blank=False)
    qualification1 = models.CharField(max_length=200, blank=False)
    email1 = models.EmailField(max_length=144, null=False, blank=False)
    contact1 = models.CharField(max_length=20, blank=False)
    member2 = models.CharField(max_length=200, blank=True)
    qualification2 = models.CharField(max_length=200, blank=True)
    email2 = models.EmailField(max_length=144, null=False, blank=True)
    contact2 = models.CharField(max_length=20, blank=True)
    member3 = models.CharField(max_length=200, blank=True)
    qualification3 = models.CharField(max_length=200, blank=True)
    email3 = models.EmailField(max_length=144, null=False, blank=True)
    contact3 = models.CharField(max_length=20, blank=True)
    member4 = models.CharField(max_length=200, blank=True)
    qualification4 = models.CharField(max_length=200, blank=True)
    email4 = models.EmailField(max_length=144, null=False, blank=True)
    contact4 = models.CharField(max_length=20, blank=True)
    institution = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=False, blank=False)
    contact = models.CharField(max_length=20)

    #questions
    question1=models.TextField(blank=True, null=False)
    question2=models.TextField(blank=True, null=False)
    question3=models.TextField(blank=True, null=False)
    question4=models.TextField(blank=True, null=False)

    def filePathGenerate(instance,filename):
        temp = 'private/ibmhackathon/' + str(instance.full_name) + '_' + str(instance.user) + '_' + str(instance.institution) + '/'
        temp2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        temp3 = '/' + os.path.split(filename)[1]
        temp = temp + temp2 + temp3
        return temp
    responseFile = models.FileField(validators=[ibmhackathon_file_validation], upload_to=filePathGenerate, null=False, blank=True, max_length=600)

    #how you got to know about this program/event
    howyouknow = models.CharField(blank=True, null=False, max_length=200)
    confirmation_email_sent = models.BooleanField(default=False)
    #whether or not the form was submitted
    isSubmit = models.BooleanField(default=False)
    last_modify_date = models.DateTimeField( null=True, blank=True)
    submit_date = models.DateTimeField( null=True, blank=True)
    def __str__(self):
        return str(self.user)

    def clean(self):
        question_filled=(self.question1 and self.question2 and self.question3)
        file_uploaded=self.responseFile
        if not question_filled and not file_uploaded :
            raise ValidationError("Please fill out the responses, or upload a .pdf file containing the responses")

class PISRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    #form details
    #team details
    teamName = models.CharField(max_length=200)
    member1name = models.CharField(max_length=200)
    member1mobile = models.CharField(max_length=20, null=False, blank=False)
    member1email = models.EmailField(max_length=200, null=False, blank=False)
    member2name = models.CharField(max_length=200, null=False, blank=True)
    member2mobile = models.CharField(max_length=20, null=False, blank=True)
    member2email = models.EmailField(max_length=200, null=False, blank=True)
    member3name = models.CharField(max_length=200, null=False, blank=True)
    member3mobile = models.CharField(max_length=20, null=False, blank=True)
    member3email = models.EmailField(max_length=200, null=False, blank=True)
    #project details
    ideaAbstract = models.TextField(null=False, blank=True)
    motivation = models.TextField(null=False, blank=True)
    prospects = models.TextField(null=False, blank=True)
    marketResearch = models.TextField(null=False, blank=True)
    prototyping = models.TextField(null=False, blank=True)
    #def filePathGenerate(instance,filename):
    #    temp = 'private/pis/' + str(instance.full_name) + '_' + str(instance.user) + '_' + str(instance.institution) + '/'
    #    temp2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    #    temp3 = '/' + os.path.split(filename)[1]
    #    temp = temp + temp2 + temp3
    #    return temp
    #responseFile = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])], upload_to=filePathGenerate, null=False, blank=True, max_length=600)

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

class DecoherenceObjectiveQuestion(models.Model):
    qNo = models.IntegerField(unique=True, null=False, blank=True, default=-1)
    title = models.CharField(null=False, blank=True, max_length=400)
    fakeText =  models.TextField(default="Please wait", null=False, blank=True)
    text =  models.TextField(null=False, blank=True)
    choice1 = models.CharField(null=False, blank=True, max_length=600)
    choice2 = models.CharField(null=False, blank=True, max_length=600)
    choice3 = models.CharField(null=False, blank=True, max_length=600)
    choice4 = models.CharField(null=False, blank=True, max_length=600)
    def filePathGenerate(instance,filename):
        temp = 'private/decoherence/questions/' + str(instance.qNo) + ' ' + str(instance.title)  + '/'
        temp2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        temp3 = '/' + os.path.split(filename)[1]
        temp = temp + temp2 + temp3
        return temp
    image = models.ImageField(null=False, blank=True, upload_to=filePathGenerate)
    def __str__(self):
        return str(self.qNo) + str(self.title) + str(self.text)


class DecoherenceSubjectiveQuestion(models.Model):
    qNo = models.IntegerField(unique=True, null=False, blank=True, default=-1)
    title = models.CharField(null=False, blank=True, max_length=400)
    fakeText =  models.TextField(default="Please wait", null=False, blank=True)
    text =  models.TextField(null=False, blank=True)
    def filePathGenerate(instance,filename):
        temp = 'private/decoherence/questions/' + str(instance.qNo) + ' ' + str(instance.title)  + '/'
        temp2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        temp3 = '/' + os.path.split(filename)[1]
        temp = temp + temp2 + temp3
        return temp
    image = models.ImageField(null=False, blank=True, upload_to=filePathGenerate)
    def __str__(self):
        return str(self.qNo) + str(self.title) + str(self.text)

#used for daatetime like the opening of decoherence prelims portal
class StatusDates(models.Model):
    title = models.CharField(null=False, blank=True, max_length=400)
    description =  models.TextField(null=False, blank=True)
    dtValue = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.title) + str(self.dtValue) + str(self.description)

import registration.decoherence_helpers as decoherence_helpers

class DecoherencePrelim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    decoherenceRegistration = models.ForeignKey(DecoherenceRegistration, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    submit_date = models.DateTimeField( null=True, blank=True)
    #form details
    question01 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(1))
    question02 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(2))
    question03 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(3))
    question04 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(4))
    question05 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(5))
    question06 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(6))
    question07 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(7))
    question08 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(8))
    question09 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(9))
    question10 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(10))
    question11 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(11))
    question12 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(12))
    question13 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(13))
    question14 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(14))
    question15 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(15))
    question16 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(16))
    question17 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(17))
    question18 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(18))
    question19 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(19))
    question20 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(20))
    question21 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(21))
    question22 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(22))
    question23 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(23))
    question24 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(24))
    question25 = models.CharField(default='S', null=True, blank=False, max_length=600, choices=decoherence_helpers.getDecoherenceObjectiveOptions(25))
    def filePathGenerate(instance,filename):
        temp = 'private/decoherence/responses/' + str(instance.teamName) + '_' + str(instance.user) + '_' + str(instance.institution) + '/'
        temp2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        temp3 = '/' + os.path.split(filename)[1]
        temp = temp + temp2 + temp3
        return temp
    subjectiveAnswers = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf','zip'])], upload_to=filePathGenerate, null=False, blank=True, max_length=600)
    #team details
    teamName = models.CharField(max_length=144)
    institution = models.CharField(max_length=144)
    city = models.CharField(max_length=144)
    confirmation_email_sent = models.BooleanField(default=False)
    #whether or not the form was submitted
    isSubmit = models.BooleanField(default=False)
    modifyTimes = models.TextField(default=" ", null=False, blank=True)
    email = models.EmailField(max_length=200, null=False, blank=False)
    def __str__(self):
        return str(self.user)



class CryptothlonPrelim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cryptothlonRegistration = models.ForeignKey(CryptothlonRegistration, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    submit_date = models.DateTimeField( null=True, blank=True)
    #form details
    a01 = models.CharField(null=True, blank=True, max_length=24)
    a07 = models.CharField(null=True, blank=True, max_length=24)
    a08 = models.CharField(null=True, blank=True, max_length=24)
    a09 = models.CharField(null=True, blank=True, max_length=24)
    a10 = models.CharField(null=True, blank=True, max_length=24)
    a11 = models.CharField(null=True, blank=True, max_length=24)
    a13 = models.CharField(null=True, blank=True, max_length=24)
    a16 = models.CharField(null=True, blank=True, max_length=24)
    a17 = models.CharField(null=True, blank=True, max_length=24)
    d02 = models.CharField(null=True, blank=True, max_length=24)
    d03 = models.CharField(null=True, blank=True, max_length=24)
    d04 = models.CharField(null=True, blank=True, max_length=24)
    d05 = models.CharField(null=True, blank=True, max_length=24)
    d06 = models.CharField(null=True, blank=True, max_length=24)
    d12 = models.CharField(null=True, blank=True, max_length=24)
    d13 = models.CharField(null=True, blank=True, max_length=24)
    d14 = models.CharField(null=True, blank=True, max_length=24)
    #team details
    teamName = models.CharField(max_length=144)
    institution = models.CharField(max_length=144)
    city = models.CharField(max_length=144)
    confirmation_email_sent = models.BooleanField(default=False)
    #whether or not the form was submitted
    isSubmit = models.BooleanField(default=False)
    modifyTimes = models.TextField(default=" ",max_length=1200, null=False, blank=True)
    email = models.EmailField(max_length=200, null=False, blank=False)
    def __str__(self):
        return str(self.user)

class CryptothlonPrelimDump(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    dumpString = models.TextField(default=" ",max_length=2000, null=True, blank=True)
    def __str__(self):
        return str(self.user) + str(self.create_date)
